import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer, QUrl
from datetime import datetime
from PyQt5 import QtMultimedia
import os

clocktimer = QTimer()

class Clock(QWidget):
    def __init__(self, parent):
        super(Clock, self).__init__()
        self.setParent(parent)
        self.time = datetime.now()

        current_time = self.time.strftime("%I:%M %p")
        if current_time[0] == "0":
            current_time = current_time[1:]

        self.label = QLabel(current_time)
        self.label.setParent(self)
        self.label.setStyleSheet('color: white; font-size: 100px')

        # Delete Later Start
        print(os.getcwd())
        audio_path = QUrl.fromLocalFile("./mirror/widgets/breath.mp3")

        audio = QtMultimedia.QMediaContent(audio_path)
        audio_player = QtMultimedia.QMediaPlayer()
        audio_player.setMedia(audio)
        audio_player.play()
        # Delete Later End

        clocktimer.timeout.connect(self.update_time)
        clocktimer.start(1000)

    def update_time(self):
        new_time = datetime.now()
        if new_time.strftime("%I:%M %p") != self.time.strftime("%I:%M %p"):
            self.time = new_time

            current_time = self.time.strftime("%I:%M %p")
            if current_time[0] == "0":
                current_time = current_time[1:]

            self.label.setText(current_time)

    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()
        
