import os

import json

from JSON import *

import pytest

def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")

@pytest.fixture
def get_headers:
    return JSONRequest.headers


@pytest.fixture
def get_url:
    return JSONRequest.url


@pytest.fixture
def get_body:
    return JSONRequest.body

@pytest.fixture
def get_method:
    return JSONRequest.method


