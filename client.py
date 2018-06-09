import socket
import time
import settings
from JSON import JSONRequest, JSONResponse
import zlib
import logging

log_client = logging.getLogger('messenger.client')
log_debug = logging.getLogger('messenger.debug')

class EchoClient():
    def __init__(self):
        self._sock = socket.socket()
        self._sock.connect((settings.HOST, settings.PORT))

    def read(self, sock):

        # Получаем данные с сервера
        data = self._sock.recv(settings.BUFFER_SIZE)

        # Передаем полученные данные в конструктор JSONResponse
        response = JSONResponse(zlib.decompress(data))

        # Выводим тело запроса на экран
        print(response.body)

    def write(self):
        # Вводим данные с клавиатуры
        data = input('Enter data: ')

        # Создаем JSONRequest на основании введенных пользователем данных
        request = JSONRequest('echo', data)

        # Переводим JSONRequest в bytes
        bytes_data = request.to_bytes()

        # Отправляем данные на сервер
        self._sock.send(zlib.compress(bytes_data))

    def do_run(self, *args, **kwargs):
        pass

    def run(self):

        try:

            while True:
                # Вводим данны и отправляем на сервер
                self.write()

                # Получаем ответ сервера
                self.read(self._sock)

                self.do_run()

        except KeyboardInterrupt:

            # Обрабатываем сочетание клавишь Ctrl+C
            pass



if __name__ == '__main__':
    client = EchoClient()

    client.run()

 







