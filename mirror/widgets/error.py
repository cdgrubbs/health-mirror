import sys
import requests
import json
import urllib.parse
import pycountry
import os
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QColor


class ErrorMSG(QWidget):
    def __init__(self, parent):
        super(ErrorMSG, self).__init__()
        self.label = QLabel("sorry, something went wrong, please try again")
        self.setParent(parent)
        self.label.setParent(self)
        self.label.setStyleSheet('color: white; font-size: 18px')

    def show(self):
        self.label.show()

    def hide(self):
        self.label.hide()
