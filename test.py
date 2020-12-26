from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class SomeCustomWidget(QWidget):

    def paintEvent(self, event):
        qp = QPainter(self)
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, qp, self)

class Win(QMainWindow):

    def __init__(self):
        super().__init__()

        with open('style.qss', 'r', encoding='utf-8') as file:
            str = file.read()
        self.setStyleSheet(str)

        self.__widget = SomeCustomWidget()
        self.setCentralWidget(self.__widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Win()
    win.show()
    app.exec_()