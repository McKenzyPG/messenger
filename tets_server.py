import sys

import mock

import socket

from server import *

import pytest

import settings

@pytest.fixture
def client_host():
    return 'localhost'

@pytest.fixture
def client_port():
    return 8000

@pytest.fixture
def client_adress(client_host, client_port):
    return client_host, client_port

@pytest.fixture
def N_clients(client_host, client_port):
    return 10

def setup_module(module):
    module.default_host = settings.HOST
    module.default_port = settings.PORT
    settings.HOST = 'localhost'
    settings.PORT = 8000


def teardown_module(module):
    settings.HOST = module.default_host
    settings.PORT = module.default_port

@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
def test_bind(mocked_settimeout, mcoked_listen, mocked_bind):
    EchoServer()

    mocked_bind.assert_called_once_with(client_adress)


@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
def test_listen(mocked_settimeout, mcoked_listen, mocked_bind, N_clients):
    EchoServer()

    mocked_bind.assert_called_once_with(N_clients)

@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
def test_settimeout(mocked_settimeout, mcoked_listen, mocked_bind, server_timeout):
    EchoServer()

    mocked_settimeout.assert_called_once_with(server_timeout)

@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
@mock.patch ('socket.socket.accept')
def test_connect(mocked_accept, mocked_settimeout, mcoked_listen, mocked_bind, client_adress):
    mocked_accept.return_value = (client_adress, socket.socket())

    srv = EchoServer()
    srv.connect()
    mocked_accept.assert_call_once_with()

@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
@mock.patch ('socket.socket.accept')
def test_connect_timeout(mocked_accept, mocked_settimeout, mcoked_listen, mocked_bind, client_adress):
    mocked_accept.side_effect = OSError

    srv = EchoServer()
    srv.connect()
    mocked_accept.assert_call_once_with()


@mock.patch ('socket.socket.bind')
@mock.patch ('socket.socket.listen')
@mock.patch ('socket.socket.settimeout')
@mock.patch ('server.EchoServer.do_mainloop')
def test_mainloop(mocked_do_mainloop, mocked_accept, mocked_settimeout, mcoked_listen, mocked_bind, client_adress):
    mocked_do_mainloop.side_effect = KeyboardInterrupt
    mocked_accept.return_value = (client_adress, socket.socket())

    srv = EchoServer()
    srv.mainloop()
    mocked_accept.assert_call_once_with()

@pytest.fixture
def get_port:
    return settings.PORT


def test_read():
    assert settings.BUFFERSIZE == 1024

def test_write():
    assert bytes_data({'test': 'test'}) == b'{"test": "test"}'


