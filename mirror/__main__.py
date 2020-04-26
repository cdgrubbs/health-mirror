import sys
import os

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer

from mirror.widgets.clock import Clock
from mirror.widgets.listener import Listener
from mirror.widgets.journal import Journal
from mirror.widgets.reflection import Reflection
from mirror.widgets.reminders import Reminders
from mirror.widgets.error import ErrorMSG

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock
from mirror.widgets.weather.weather import WeatherGUI
from mirror.widgets.simple_widget import SimpleWidget
from mirror.widgets.joke import Joke

from mirror.widgets.breathing.breathing import Breathing

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot


# gratitude journaling/reflection
# reminder: social outreach + medication reminder
# breathing exercise
# joke

# EVERY WIDGET NEEDS: doWidget(), show(), hide()
#       reminder specifically: setReminder()
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.l = Listener(self)
        self.grid_layout = QGridLayout()
        self.title = "Health Mirror"
        self.fullWidth = 2560 #2560 for hpSpectrex360
        self.fullHeight = 1440 #1440 for hpSpectrx360

        self.w1 = Clock(self)  # place holder
        self.w2 = WeatherGUI(self)  # place holder
        self.w3 = Journal(self)
        self.w4 = Reflection(self)
        self.w5 = Joke(self)
        self.w6 = Breathing(self)
        self.w7 = Reminders(self)
        self.w8 = ErrorMSG(self)
        self.initGUI()

    def initGUI(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)
        self.createLayout()
        self.createButtons()
        self.resize(1000, 1000)
        self.showFullScreen()

    def createLayout(self):
        self.grid_layout.addWidget(Clock(self), 0, 0)
        self.grid_layout.addWidget(WeatherGUI(self), 0, 2)

        self.grid_layout.addWidget(self.w1, 0, 1)
        self.grid_layout.addWidget(self.w2, 0, 1)
        self.grid_layout.addWidget(self.w3, 1, 1)
        self.grid_layout.addWidget(self.w4, 1, 1)
        self.grid_layout.addWidget(self.w5, 2, 1)
        self.grid_layout.addWidget(self.w6, 1, 1)
        self.grid_layout.addWidget(self.w7, 2, 1)
        self.grid_layout.addWidget(self.w8, 2, 1)

        #self.w3.move(self.fullWidth / 2 - 500, self.fullHeight / 2 - 500)
        #self.w4.move(self.fullWidth / 2 - 500, self.fullHeight / 2 - 500)
        #self.w5.move(self.fullWidth / 2 - 100, self.fullHeight - 400)
        #self.w6.move(self.fullWidth / 2 - 500, self.fullHeight / 2 - 500)
        #self.w7.move(self.fullWidth / 2 - 100, self.fullHeight - 400)
        #self.w8.move(400, 400)

        # self.grid_layout.setRowStretch(1, 0.3)

        self.hideAll()

        # self.w7.show()
        self.setLayout(self.grid_layout)

    def editLayout(self, widgetName):
        print('editing layout')
        # will be changed after other widgets are made

        self.hideAll()
        if widgetName == 'joke':
            self.w5.show()
        elif widgetName == 'breathe':
            self.w6.do_breathing()
        elif widgetName == 'journal':
            self.w3.show()
            self.w3.doJournal()
        elif widgetName == 'read_journal':
            self.w3.show()
            self.w3.readEntries()
        elif widgetName == 'reflection':
            self.w4.show()
            self.w4.doReflection()
        elif widgetName == "reminder":
            self.w7.show()
            self.w7.setReminder()
        elif widgetName == "clear":
            self.hideAll()
        else:
            self.w8.show()

    def createButtons(self):
        button = QPushButton(self)
        icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mic.png")
        button.setIcon(QtGui.QIcon(icon))
        button.setIconSize(QtCore.QSize(80, 80))
        button.clicked.connect(self.on_click)
        button.resize(button.sizeHint())
        button.move(self.fullWidth / 2 - 50, self.fullHeight - 200)

        full = QPushButton('full screen', self)
        full.clicked.connect(self.on_clickFULLSCREEN)
        full.resize(full.sizeHint())
        full.move(100, self.fullHeight - 200)

        small = QPushButton('small screen', self)
        small.resize(small.sizeHint())
        small.clicked.connect(self.on_clickSMALLSCREEN)
        small.move(300, self.fullHeight - 200)

    @pyqtSlot()
    def on_click(self):
        widgetName = self.l.doListener()
        print(widgetName)
        self.editLayout(widgetName)

    @pyqtSlot()
    def on_clickFULLSCREEN(self):
        self.showFullScreen()
        print(self.frameSize())
        print(self.width(), self.height())

    @pyqtSlot()
    def on_clickSMALLSCREEN(self):
        self.showNormal()
        print(self.frameSize())
        print(self.width(), self.height())

    def hideAll(self):
        self.w1.hide()
        self.w2.hide()
        self.w3.hide()
        self.w4.hide()
        self.w5.hide()
        self.w6.hide()
        self.w7.hide()
        self.w8.hide()

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
