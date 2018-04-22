"""This is a settings file"""

HOST = 'localhost'

ENCODING = 'utf-8'

PORT = 8000

BUFFER_SIZE = 1024

N_CLIENTS = 10

TIMEOUT = 0

ACTIONS = ['presence',
           'authenticate',
           'join',
           'leave',
           'quit',
           'msg',
           'get_contacts',
           'add_contact',
           'del_contact',
           'response',
           'probe']
TYPES = ['text', 'img', 'video', 'audio', 'doc', 'status']

# Значения
PRESENCE = 'presence'
MSG = 'msg'

# Коды ответов (будут дополняться)
BASIC_NOTICE = 100
OK = 200
ACCEPTED = 202
WRONG_REQUEST = 400  # неправильный запрос/json объект
SERVER_ERROR = 500

# Кортеж из кодов ответов
RESPONSE_CODES = (BASIC_NOTICE, OK, ACCEPTED, WRONG_REQUEST, SERVER_ERROR)