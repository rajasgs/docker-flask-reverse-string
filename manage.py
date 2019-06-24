#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://realpython.com/testing-third-party-apis-with-mocks/
'''

# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_true
import requests

# Third-party imports...
from nose.tools import assert_is_not_none


def test_request_response():
    
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)