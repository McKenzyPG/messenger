import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QLabel,
    QAction, QFileDialog, QApplication, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPixmap, QImage, qRgb
import random
from PIL import Image, ImageDraw 
from PIL.ImageQt import ImageQt
import random
from sqlalchemy import Column, ForeignKey, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TextDisplay(QTextEdit):

    def __init__(self):
        super(TextDisplay, self).__init__()

        self.setReadOnly(True)


class CentralWidget(QWidget):

    def __init__(self):
        super(CentralWidget, self).__init__()

        self._lay = QVBoxLayout()

        self.setLayout(self._lay)

    def addWidget(self, widget):
        self._lay.addWidget(widget)


class AppWindow(QMainWindow):

    def __init__(self):
        super(AppWindow, self).__init__()

        widget = CentralWidget()

        self.display = TextDisplay()

        self.input = QLineEdit()

        widget.addWidget(self.display)

        widget.addWidget(self.input)

        self.setCentralWidget(widget)

class Image(Base):

    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)

    # name = Column(String)

    Data = Column(BLOB)

    # entension = Column(String)

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
	# Crop function
        width = 500

        height = 347

        # x_left = 50

        # y_top = 50

        # x_right = x_left + 150

        # y_bottom = y_top + 150


        x_center = width // 2

        y_center = height // 2


        x_left = x_center - 75

        y_top = y_center - 75

        x_right = x_left + 150

        y_bottom = y_top + 150


        imageFile = "image.jpg"

        image = Image.open(imageFile)

        image = image.crop((x_left, y_top, x_right, y_bottom))

        draw = ImageDraw.Draw(image)

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


	# Image save to db (binary using ORM)
    def __render__(self):

        engine = create_engine('sqlite:///image.db')

        engine.echo = True

        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)

        file = open("image.jpg", "rb")

        img = file.read()

        file.close()

        s = session()
        images = Image( Data = img )
        s.add(images)
        s.commit()



        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

