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
        backgroundImage = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons/beach.jpg")
        print(backgroundImage)
        self.background.setPixmap(QPixmap(backgroundImage).scaled(self.width, self.height))
        self.background.setScaledContents(True)

        self.start = 0
        self.labelDirection = QLabel("Breathing")
        self.labelDirection.setParent(self)
        # self.label.move(QPoint(0 + 175, 450))
        self.labelDirection.move(0, 450)
        self.labelDirection.setStyleSheet('color: white; font-size: 75px')

        # self.labelCounter = QLabel()
        # self.labelCounter.setParent(self)
        # self.label.move(QPoint(0 + 175, 450))
        # self.labelCounter.move(600, 600)
        # self.labelCounter.setStyleSheet('color: white; font-size: 75px')
        self.breathin = 0
        breathingtimer.timeout.connect(self.breath)

    def do_breathing(self):
        self.show()
        self.counter = 30
        breathingtimer.start(1500)

    def breath(self):

        if self.counter > 0:
            if (self.start > 0):
                # self.labelCounter.show()
                self.labelDirection.setText(str(self.start))
                self.start -= 1
            else:
                self.start = 3
                # self.labelCounter.hide()
                if (self.breathin == 0):
                    self.labelDirection.setText("inhale")
                    self.breathin = 1
                else:
                    self.labelDirection.setText("exhale")
                    self.breathin = 0
            self.counter -= 1
        else:
            breathingtimer.stop()
            self.labelDirection.setText("Nice Job")
            self.hide()
            self.labelDirection.setText("Breathing")


    def hide(self):
        self.background.hide()
        self.labelDirection.hide()
        #self.labelCounter.hide()
        breathingtimer.stop()

    def show(self):
        self.resize(1000, 1000)
        self.setVisible(True)
        self.background.show()
        self.labelDirection.show()
