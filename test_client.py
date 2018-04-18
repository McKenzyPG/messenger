import settings

import os

from client import *

import pytest


@pytest.fixture
def test_bind():
    print ('bind successful')

@pytest.fixture
def message_bytes():
    return b'{'sender': 'user1', 'receiver' : 'user2', 'message': 'mesaage'}'

@pytest.fixture
def message_string():
    return '{'sender': 'user1', 'receiver' : 'user2', 'message': 'mesaage'}'


@pytest.fixture
def mocked_connect(conenct_message, monkeypatch):
    def mock_connect(self, *args, **kwargs):

        print(conenct_message)

    monkeypatch.setattr(socket.socket, 'connect', mock_connect)

@pytest.fixture
def mocked_recv(message_bytes, monkeypatch):
    def mock_recv(self, *args, **kwargs):

        return message_bytes
    monkeypatch.setattr(socket.socket, 'recv', mock_recv)

@pytest.fixture
def mocked_do(monkeypatch):
    def mock_do(self, *args, **kwargs):
        raise KeyboardInterrupt()
    monkeypatch.setattr(EchoClient, 'do_run', mock_do)


def test_connect(mocked_connect, connect_message, capsys):
    EchoClient()

    out, err = capsys.readputerr()
    assert connect_message in out


def test_read(mocked_connect, mocked_recv, message_string, capsys):
    clt = EchoClient()
    clt.read()
    out, err = capsys.readputerr()
    assert message_string in out

def test_do(mocked_connect):
    clt = EchoClient()
    clt.run()

def test_run(mocked_connect, mocked_recv, mocked_do):
    clt = EchoClient()
    clt.run()

@pytest.fixture
def test_write():
    assert bytes_data({'test': 'test'}) == b'{"test": "test"}'




def test_get_message(monkeypatch):
    # подменяем настоящий сокет нашим классом заглушкой
    monkeypatch.setattr("socket.socket", EchoClient)
    # зоздаем сокет, он уже был подменен
    sock = socket.socket()
    # теперь можем протестировать работу метода
    assert get_message(sock) == {'response': 200}


def test_send_message(monkeypatch):
    # подменяем настоящий сокет нашим классом заглушкой
    monkeypatch.setattr("socket.socket", ClientSocket)
    # cоздаем сокет, он уже был подменен
    sock = socket.socket()
    # т.к. возвращаемого значения нету, можно просто проверить, что метод отрабатывает без ошибок
    assert send_message(sock, {'test': 'test'}) is None
    # и проверяем, чтобы обязательно передавали словарь на всякий пожарный
    with raises(TypeError):
        send_message(sock, 'test')