import json

import threading

from guicore.appwindow.appwindow import AppWindow

from appcore.socketmanager import SocketManager


def __plugin__(app):

    app.window = AppWindow()

    app.manager = SocketManager()


    def press_event():

        enter = app.window.input.text()

        app.manager.send_request_message(user=app.config.username, message=enter)

        app.window.input.clear()


    def read_messages(manager):

        while True:

            message = app.manager.receive_response_message()

            message_json = json.loads(message)

            code = message_json.get('code')

            body = message_json.get('message')

            text = body.get('message')

            username = body.get('user')

            display_txt = '%s: %s' % (username, text)

            app.window.display.append(display_txt)


    app.window.input.returnPressed.connect(press_event)

    reader_thread = threading.Thread(target=read_messages, args=(app.manager,), daemon=True)

    reader_thread.start()

    app.window.show()