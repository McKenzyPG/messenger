import json

import socket

from utility.configuration.configuration import ConfigMetaclass, ConfigAttribute


class SocketConfig(metaclass=ConfigMetaclass):

    buffer_size = ConfigAttribute('buffer_size', int, 1024)

    encoding = ConfigAttribute('encoding', str, 'utf-8')

    host = ConfigAttribute('host', str, 'localhost')

    port = ConfigAttribute('port', int, 8000)


    def __init__(self, path=None):

        if path:

            with open(path, 'r') as file:

                config_json = json.load(file)

                for name, value in config_json.items():

                    setattr(self, name, value)


class SocketManager(metaclass=ConfigMetaclass):

    def __init__(self):

        self._config = SocketConfig()


    @property
    def address(self):

        return (self._config.host, self._config.port)


    def send_request_message(self, **kwargs):

        with socket.socket() as sock:

            sock.connect(self.address)

            context = {'action':'sendall', 'message':kwargs}

            response_str = json.dumps(context)

            response_bytes = response_str.encode(self._config.encoding)

            sock.send(response_bytes)


    def receive_response_message(self):

        with socket.socket() as sock:

            sock.connect(self.address)

            while True:

                response_bytes = sock.recvmsg(self._config.buffer_size)[0]

                return response_bytes.decode(self._config.encoding)
