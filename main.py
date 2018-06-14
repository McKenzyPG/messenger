#!/usr/bin/python3
# -*- coding: utf-8 -*-

import ftplib
import MySQLdb

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb

from view import Example

from controller import ftp_send, sql_save


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ftp_send()

    sql_save()

    Example()

    sys.exit(app.exec_())