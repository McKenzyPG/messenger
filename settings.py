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