import socket
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLabel,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon, QFont
import random
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
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


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):


	#File upload method
        self.lbl = QLabel(self)


        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open file')
        openFile.triggered.connect(self.showDialog)

	

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
	
	#image correction method

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

	image = Image.open("image.jpg")
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()


        for i in range(width):
            for j in range(height):

                 a = pix[i, j][0]

                 b = pix[i, j][1]

                 c = pix[i, j][2]

                 S = (a + b + c) // 2

                 draw.point((i, j), (S, S, S))


        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()

	#font options
	
	self.textEdit = QTextEdit()
        
        self.setCentralWidget(self.textEdit)


        bold = QAction(QIcon('b.jpg'),'Bold', self)

        bold.triggered.connect(self.actionBold)

        italic = QAction(QIcon('i.jpg'), 'Italic', self)

        italic.triggered.connect(self.actionItalic)

        underlined = QAction(QIcon('u.jpg'), 'Underlined', self)

        underlined.triggered.connect(self.actionUnderlined)


        toolbar = self.addToolBar('Formatting')

        toolbar.addAction(bold)

        toolbar.addAction(italic)

        toolbar.addAction(underlined)


        self.setGeometry(300, 300, 350, 250)

        self.setWindowTitle('Main window')

        self.show()


    def actionBold(self):

        myFont = QFont()

        myFont.setBold(True)

        # myFont.setWeight(700)

        self.textEdit.setFont(myFont)


    def actionItalic(self):

        myFont = QFont()

        myFont.setItalic(True)

        self.textEdit.setFont(myFont)


    def actionUnderlined(self):

        myFont = QFont()

        myFont.setUnderline(True)

        self.textEdit.setFont(myFont)

	#smiles

	self.textEdit = QTextEdit()

        self.setCentralWidget(self.textEdit)


        smile = QAction(QIcon('ab.gif'),'Smile', self)

        smile.triggered.connect(self.actionSmile)

        melancholy = QAction(QIcon('ac.gif'), 'Melancholy', self)

        melancholy.triggered.connect(self.actionMelancholy)

        surprise = QAction(QIcon('ai.gif'), 'Surprise', self)

        surprise.triggered.connect(self.actionSurprise)


        send = QAction('Send', self)

        send.triggered.connect(self.send_text)


        toolbar = self.addToolBar('Formatting')

        toolbar.addAction(smile)

        toolbar.addAction(melancholy)

        toolbar.addAction(surprise)


        toolbar.addAction(send)



        self.setGeometry(300, 300, 350, 250)

        self.setWindowTitle('Main window')

        self.show()


    def actionSmile(self):

        url = 'ab.gif'

        self.textEdit.setHtml('<img src="%s" />' % url)


    def actionMelancholy(self):

        url = 'ac.gif'

        self.textEdit.setHtml('<img src="%s" />' % url)

    def actionSurprise(self):

        url = 'ai.gif'

        self.textEdit.setHtml('<img src="%s" />' % url)


    def send_text(self):

        data = self.textEdit.toHtml()

        print(data.encode())

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Close file', '/home')[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(300,300)
        self.lbl.setPixmap(pixmap)

       # lbl.setPixmap(pixmap)



if __name__ == '__main__':
    client = EchoClient()

    client.run()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







