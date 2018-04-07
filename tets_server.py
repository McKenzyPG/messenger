import os

import json

import pytest

import settings


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")

@pytest.fixture
def get_host:
    return settings.HOST


@pytest.fixture
def get_port:
    return settings.PORT


@pytest.fixture
def get_clients:
    return settings.N_CLIENTS

@pytest.fixture
def get_timeout:
    return settings.TIMEOUT


def test_read:
    assert settings.BUFFERSIZE == 1024

def test_write:
    assert bytes_data({'test': 'test'}) == b'{"test": "test"}'


