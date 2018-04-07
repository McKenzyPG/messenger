import os

import json

import client

import pytest


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")

@pytest.fixture
def test_read():
  assert data == client._sock.recv(1024)
  assert response = JSONRequest(data)


@pytest.fixture
def test_write():
    assert bytes_data({'test': 'test'}) == b'{"test": "test"}'

def test_get_message(monkeypatch):
    # подменяем настоящий сокет нашим классом заглушкой
    monkeypatch.setattr("socket.socket", ClientSocket)
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