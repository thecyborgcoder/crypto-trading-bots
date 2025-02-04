#!/usr/bin/env python3
# coding: utf-8


class BrokerApiException(Exception):

    def __init__(self, response):
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = 'Invalid JSON error message from Broker: {} http code: {}'.format(
                response.text, response.status_code)
        else:
            # try:
            self.code = json_res['status']
            self.message = json_res['error']
            # except:
            #     self.code = json_res['status']
            #     self.message = json_res['error']
        self.status_code = response.status_code
        self.response = response.text
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return 'APIError(code=%s): %s' % (self.code, self.message)


class BrokerRequestException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'BrokerRequestException: %s' % self.message