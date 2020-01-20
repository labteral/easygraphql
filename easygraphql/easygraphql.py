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

        response = requests.post(self.endpoint, json=payload, headers=headers).json()

        try:
            data = response['data']
        except KeyError:
            data = None

        try:
            errors = response['errors']
        except KeyError:
            errors = None

        return data, errors