# this is a simple example of a rest client in Python
import logging

import requests


class RestClient:
    def __init__(self):
        logging.info('initialized RestClient')

    # returns all users
    def get_all_users(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users')

        if response.status_code != 200:
            logging.warning('whoops ' + self.handle_http_error_codes(response.status_code))
            return self.handle_http_error_codes(response.status_code)

        return response.json()

    # returns a single user based on an identifier
    def get_single_user(self, identifier):
        response = requests.get('https://jsonplaceholder.typicode.com/users/' + identifier)

        if response.status_code != 200:
            logging.warning('whoops ' + self.handle_http_error_codes(response.status_code))
            return self.handle_http_error_codes(response.status_code)

        return response.json()

    # handles error codes returned by REST API
    # Uses a simple implementation of pattern matching available in Python 3.10
    def handle_http_error_codes(self, status):
        logging.info('I am here')
        match status:
            case 400:
                return 'Bad request'
            case 404:
                return 'I cannot find what you are requesting'
            case 500:
                return 'Whoops...something bad happened!'
            case _:
                return 'Something catastrophic has occurred!'

