import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout


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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AppWindow()

    window.show()

    sys.exit(app.exec_())