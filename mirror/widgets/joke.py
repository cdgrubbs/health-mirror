import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer
import random

clocktimer = QTimer()

class Joke(QWidget):
    def __init__(self, parent):
        super(Joke, self).__init__()
        self.setParent(parent)
        jokes = [
            "What do you call a computer floating in the ocean? A Dell Rolling in the Deep",
            "There are 10 types of people in the world: those who understand binary, and those who don’t",
            "An SQL statement walks into a bar and sees two tables. It approaches, and asks “may I join you?”",
            "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
            "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat",
            "A programmer’s wife tells him, “While you’re at the grocery store, buy some eggs.” He never comes back"
        ]
        index = random.randint(0,5)

        self.label = QLabel(jokes[index])
        self.label.setWordWrap(True)
        self.label.setParent(self)
        self.label.setStyleSheet('color: white; font-size: 18px')

    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()
        