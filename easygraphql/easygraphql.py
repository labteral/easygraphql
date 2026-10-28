#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import requests


class GraphQL:
    def __init__(self, endpoint: str, headers: dict = None, timeout=(3, 30)):
        self.endpoint = endpoint
        values = timeout if isinstance(timeout, tuple) else (timeout,)
        if (len(values) not in (1, 2)
                or any(type(value) not in (int, float)
                       or not math.isfinite(value) or value <= 0
                       for value in values)):
            raise ValueError('timeout must contain positive finite seconds')
        self._timeout = timeout
        self._headers = dict(headers or {})

    @property
    def headers(self):
        return dict(self._headers)

    def add_headers(self, headers: dict):
        self._headers.update(headers)

    def set_headers(self, headers: dict):
        self._headers = dict(headers)

    def unset_headers(self):
        self._headers = {}

    def _post(self, operation, variables=None, headers=None, timeout=None):
        if headers is None:
            headers = self._headers
        request_data = {'query': ' '.join(operation.split())}
        if variables is not None:
            request_data['variables'] = variables
        response = requests.post(
            self.endpoint, json=request_data, headers=headers,
            timeout=self._timeout if timeout is None else timeout,
            allow_redirects=False,
        )
        if 300 <= response.status_code < 400:
            response.close()
            raise requests.HTTPError(
                'GraphQL endpoint redirected', response=response)
        return response

    def execute(self, operation: str, variables: dict = None,
                headers: dict = None):
        with self._post(operation, variables, headers) as request:
            response = request.json()
        try:
            response_data = response['data']
        except KeyError:
            response_data = None

        try:
            errors = response['errors']
        except KeyError:
            errors = None

        return response_data, errors
