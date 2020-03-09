import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect

class Clock(QWidget):
    def __init__(self, parent):
        super(Clock, self).__init__()
        self.setParent(parent)


        self.label = QLabel("1:00 PM")
        self.label.setParent(self)
        self.label.setGeometry(QRect(10, 10, 500, 375))
        self.label.setStyleSheet('color: white; font-size: 100px')

    def show(self):
        self.label.show()
        