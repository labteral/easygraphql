#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class GraphQL:
    def __init__(self, endpoint, headers=None):
        self.endpoint = endpoint
        self.headers = headers

    def set_headers(self, headers):
        self.headers = headers

    def unset_headers(self):
        self.headers = None

    def execute(self, operation, variables=None, headers=None):
        payload = {'query': operation}

        if variables is not None:
            payload['variables'] = variables

        if headers is None:
            headers = self.headers

        response = requests.post(self.endpoint, json=payload, headers=headers)

        try:
            return response.json()['data']
        except KeyError:
            return response.json()['errors']