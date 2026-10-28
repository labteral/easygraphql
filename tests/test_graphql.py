from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import unittest
from unittest.mock import MagicMock, patch

import requests
from easygraphql import GraphQL


class GraphQLTests(unittest.TestCase):
    def test_legacy_response_headers_and_bounded_timeout(self):
        for value in (0, -1, float('nan'), float('inf'), (), (1, 2, 3), True):
            with self.subTest(timeout=value), self.assertRaises(ValueError):
                GraphQL('http://127.0.0.1:9', timeout=value)

        headers = {'Authorization': 'Bearer fixture'}
        client = GraphQL('http://127.0.0.1:9', headers=headers)
        headers.clear()
        response = MagicMock()
        response.status_code = 400
        response.__enter__.return_value.json.return_value = {
            'errors': [{'message': 'legacy GraphQL error'}],
        }
        with patch('easygraphql.easygraphql.requests.post',
                   return_value=response) as post:
            self.assertEqual(client.execute('query  {  hello }', {'id': 1}),
                             (None, [{'message': 'legacy GraphQL error'}]))
        post.assert_called_once_with(
            'http://127.0.0.1:9',
            json={'query': 'query { hello }', 'variables': {'id': 1}},
            headers={'Authorization': 'Bearer fixture'},
            timeout=(3, 30), allow_redirects=False,
        )
        replacement = {'X-Fixture': 'kept'}
        client.set_headers(replacement)
        replacement.clear()
        self.assertEqual(client.headers, {'X-Fixture': 'kept'})

    def test_redirect_does_not_forward_authorization_or_payload(self):
        received = []

        class Sink(BaseHTTPRequestHandler):
            def do_POST(self):
                received.append(
                    self.rfile.read(int(self.headers['Content-Length'])))
                self.send_response(200)
                self.end_headers()

            def log_message(self, *_):
                pass

        sink = ThreadingHTTPServer(('127.0.0.1', 0), Sink)
        sink_thread = Thread(target=sink.serve_forever, daemon=True)
        sink_thread.start()
        self.addCleanup(
            lambda: (sink.shutdown(), sink_thread.join(), sink.server_close()))

        class Origin(BaseHTTPRequestHandler):
            def do_POST(self):
                self.rfile.read(int(self.headers['Content-Length']))
                self.send_response(307)
                self.send_header(
                    'Location', f'http://127.0.0.1:{sink.server_port}/copy')
                self.end_headers()

            def log_message(self, *_):
                pass

        origin = ThreadingHTTPServer(('127.0.0.1', 0), Origin)
        origin_thread = Thread(target=origin.serve_forever, daemon=True)
        origin_thread.start()
        self.addCleanup(lambda: (
            origin.shutdown(), origin_thread.join(), origin.server_close()))
        client = GraphQL(f'http://127.0.0.1:{origin.server_port}/graphql',
                         headers={'Authorization': 'Bearer private-fixture'})
        with self.assertRaises(requests.HTTPError):
            client.execute('mutation { privateOperation }',
                           {'private': 'fixture'})
        self.assertEqual(received, [])


if __name__ == '__main__':
    unittest.main()
