import sys
import requests
import json
import urllib.parse
import pycountry
import os
import time
import threading

from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QIcon, QBrush, QPixmap


class Breathing(QWidget):
    def __init__(self,parent):
        super(Breathing, self).__init__()
        self.setParent(parent)
        self.image_path = './mirror/widgets/breathing/icons/beach.jpg'

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()

        self.background = QLabel()
        self.background.setParent(self)
        self.background.setPixmap(QPixmap(self.image_path).scaled(self.width, self.height))
        self.background.setScaledContents(True)

        self.show()


def hide(self):
    self.icon_label.hide()
    self.temperature_label.hide()
    self.location_label.hide()


def show(self):
    self.icon_label.hide()
    self.temperature_label.hide()
    self.location_label.hide()