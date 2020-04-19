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


class SimpleWidget(QWidget):
    def __init__(self, parent, color):
        # QWidget.__init__(self, parent=parent)
        super(SimpleWidget, self).__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)