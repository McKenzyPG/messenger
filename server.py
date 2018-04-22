import socket

import settings

import json

import JSON as jr

import zlib
import logging

log_server = logging.getLogger('messenger.server')


class EchoServer():

    def __init__(self):
        self._connections = list()
        self._requests = collections.deque()
        self._sock = socket.socket()
        self._sock.bind((settings.HOST, settings.PORT))
        self._sock.listen(settings.N_CLIENTS)
        self._sock.settimeout(settings.TIMEOUT)

    def connect(self):

        try:
            client, address = self._sock.accept()
            self._connections.append(client)

        except OSError:
            pass

    def read(self, client):

        try:

            # Получаем данные от клиента
            data = client.recv(settings.BUFFER_SIZE)

            # Если полученные данные не являются пустой строкой
            if data:
                # Передаем полученные данные в конструктор JSONRequest
                request = JSONRequest(data)

                # Сохраняем запрос на сервере
                self._requests.append(request)

        except ConnectionResetError:

             # В случае разрыва соединения с клиентом и наличии данного клиента в списке подключений
             if client in self._connections:
                # Удаляем соответствующего клиента из списка подключений
                self._connections.remove(client)

        def write(self, client, request):

            try:

                # Создаем JSONResponse на основании тела запроса
                response = JSONResponse(200, 'echo', request.body)

                # Переводим JSONResponse в bytes
                bytes_message = zlib.compress(response.to_bytes())

                # Отправляем данные на клиент
                client.send(bytes_message)

            except (ConnectionResetError, BrokenPipeError):

                # В случае разрыва соединения с клиентом и наличии данного клиента в списке подключений
                if client in self._connections:
                    # Удаляем соответствующего клиента из списка подключений
                    self._connections.remove(client)


    def do_mainloop(self, *args, **kwargs):
        pass

    def mainloop(self):

        try:

            while True:

                # Обрабатываем подключения к серверу

                self.do_mainloop()
                self.connect()

                for client in self._connections:

                    # Сохраняем запрос клиента к серверу
                    self.read(client)

                    # Если клиентом были отправлены запросы к серверу
                    if self._requests:
                        # Извлекаем первый запрос
                        request = self._requests.popleft()

                        # Отправляем запрос слиенту
                        self.write(client, request)


        except KeyboardInterrupt:

            # Обрабатываем сочетание клавишь Ctrl+C
            pass


if __name__ == '__main__':

    import select
    import collections
    connections = dict()

    with socket.socket() as sock:
        sock.bind((settings.HOST, settings.PORT))
        sock.listen(settings.N_CLIENTS)
        sock.settimeout(settings.TIMEOUT)

        while True:
            requests = dict()

            try:
                client, address = sock.accept()
                connections.update({address:client})

            except OSError:
                pass
            work_copy = connections.copy()
            clients = work_copy.values()

            rlist, wlist, xlist = select.select(clients, clients, [], 0)

            print('waiting')

            for address, client in work_copy.items():
                try:
                    if client in rlist:
                        str_address = address[0] + ':' + str(address[1])
                        data = client.recv(settings.BUFFER_SIZE)
                        if data:
                            str_data = data.decode(settings.ENCODING)
                            requests.update({str_address:str_data})
                    if client in wlist:
                        if requests:
                            message = json.dumps(requests)
                            bytes_message = message.encode(settings.ENCODING)
                            client.send(zlib.compress(bytes_message))
            except (ConnectionResetError, BrokenPipeError):
                    del connections[address]

    server = EchoServer()

    server.mainloop()

