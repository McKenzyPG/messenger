class JSONResponse():
    def __init__(self, message_bytes):
        message = message_bytes.decode(settings.ENDCODING)
        self._envelope = json.loads(message)
        self._startline = self._envelope.get('startline')

    @property
    def code(self):
        code = self._startline.get('code')

        return code
    @property
    def method(self):
        method = self._startline.get('method')

        return method

    @property
    def headers(self):
        headers = self._envelope.get('headers')
        for k,v in headers.items():
            yield k,v

        return headers

    def body(self):
        body = self._envelope.get('body')

        return body


class JSONRequest():

    def __init__(self,url,method, body,**headers):
        self._headers = headers
        self._url = url
        self._body = body
        self._method = method

    def add_header(self,k,v):
        self._headers.update({k:v})

    def rem_header(self,k):
        del self._header[k]

    def to_bytes(self):
        envelope = dict()
        start_line = dict()
        start_line.update({'url': self._url})
        start_line.update({'method': self._method})
        start_line.update({'method': self._method})
        envelope.update({'start_line': start_line})
        envelope.update({'headers': self._headers})
        envelope.update({'body': self._body})
        data_string = json.dumps(envelope)

        return data_string.encode(settings.ENCODING)