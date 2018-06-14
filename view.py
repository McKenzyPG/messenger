import ftplib
import MySQLdb

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()