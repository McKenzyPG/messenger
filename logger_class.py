import logging

class Logger_class():

    def __init__(self, message):
        self._message = message
        msg_format = '%(client)s - %(action)s - %(asctime)s'
        logging.basicConfig(format = msg_format, level='DEBUG', filename='messager.log')
        self._logger = logging.getLogger('ServerLogger')

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            extras = {'client':args[1].getpeernames()}
            self._logger.info(self._message, extras = extras)
            return func(*args, **kwargs)
        return wrapper