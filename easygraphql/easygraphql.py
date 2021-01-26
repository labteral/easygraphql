#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class GraphQL:
    def __init__(self, endpoint: str, headers: dict = None):
        self.endpoint = endpoint
        self._headers = {}
        if headers is not None:
            self._headers = headers

    @property
    def headers(self):
        return dict(self._headers)

    def add_headers(self, headers: dict):
        self._headers.update(headers)

    def set_headers(self, headers: dict):
        self._headers = headers

    def unset_headers(self):
        self._headers = {}

    def execute(self, operation: str, variables: dict = None, headers: dict = None):
        if headers is None:
            headers = self._headers

        request_data = {'query': ' '.join(operation.split())}
        if variables is not None:
            request_data['variables'] = variables

        response = requests.post(self.endpoint, json=request_data, headers=headers).json()
        try:
            response_data = response['data']
        except KeyError:
            response_data = None

        try:
            errors = response['errors']
        except KeyError:
            errors = None

        return response_data, errors