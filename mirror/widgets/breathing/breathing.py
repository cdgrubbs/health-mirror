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

breathingtimer = QTimer()

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

        self.start = 0
        self.label = QLabel("Breath")
        self.label.setParent(self)
        self.label.move(QPoint(0 + 175, 450))
        self.label.setStyleSheet('color: white; font-size: 100px')

        breathingtimer.timeout.connect(self.breath)

    def do_breathing(self):
        self.show()
        self.counter = 13
        breathingtimer.start(1000)

    def breath(self):
        if self.counter > 0:
            if (self.start > 0):
                self.label.setText(str(self.start))
                self.start -= 1
            else:
                self.start = 3
                self.label.setText("Breath")
            self.counter -= 1
        else:
            self.hide()
            breathingtimer.stop()

    def hide(self):
        self.background.hide()
        self.label.hide()


    def show(self):
        self.background.show()
        self.label.show()