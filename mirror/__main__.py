import sys
import os

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QDesktopWidget
from PyQt5.QtCore import Qt, QTimer

from mirror.widgets.clock import Clock
from mirror.widgets.listener import Listener

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock
from mirror.widgets.weather.weather import WeatherGUI
from mirror.widgets.simple_widget import SimpleWidget

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
        self.title = "Health Mirror"
        self.fullWidth = 2560
        self.fullHeight = 1440

        self.initGUI()

    def initGUI(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)
        self.create_layout()
        self.createButtons()
        self.resize(1000, 1000)
        self.showFullScreen()

    def create_layout(self):
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(Clock(self), 0, 0)
        self.grid_layout.addWidget(WeatherGUI(self), 0, 2)
        self.l = Listener(self)

        self.w1 = Clock(self) # place holder
        self.w2 = WeatherGUI(self) # place holder

        self.grid_layout.addWidget(self.w1, 1, 1)
        self.grid_layout.addWidget(self.w2, 1, 1)

        self.w1.hide()
        self.w2.hide()
        # grid_layout.addWidget(self.l, 1, 1)
        self.setLayout(self.grid_layout)

    def editLayout(self, widgetName):
        print('editing layout')
        # will be changed after other widgets are made
        if widgetName == 'joke':
            self.w1.show()
            self.w2.hide()
        elif widgetName == 'breathe':
            self.w1.hide()
            self.w2.show()

    def createButtons(self):
        button = QPushButton(self)
        print(os.getcwd())
        icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mic.png")
        print(icon)
        print(os.path.join(os.path.dirname(os.path.realpath(__file__))))
        button.setIcon(QtGui.QIcon(icon))
        button.setIconSize(QtCore.QSize(80, 80))
        button.clicked.connect(self.on_click)
        button.resize(button.sizeHint())
        # button.resize(button.sizeHint())
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


def main():
    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
