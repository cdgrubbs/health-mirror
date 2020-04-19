import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock
from mirror.widgets.listener import Listener

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock
from mirror.widgets.weather.weather import WeatherGUI
from mirror.widgets.simple_widget import SimpleWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        # Changes background to black
        self.title = "Health Mirror"
        self.init_window()

    
    def init_window(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

        self.create_layout()

        self.showFullScreen()


    def create_layout(self):
        grid_layout = QGridLayout()

        #grid_layout.addWidget(SimpleWidget(self,'red'), 0, 0)
        #grid_layout.addWidget(SimpleWidget(self,'blue'), 0, 1)
        #grid_layout.addWidget(SimpleWidget(self,'green'), 1, 1)
        grid_layout.addWidget(SimpleWidget(self,'Qt.gray'), 2, 2)
        grid_layout.addWidget(Clock(self), 0, 0)
        grid_layout.addWidget(Listener(self), 1, 1)

        self.setLayout(grid_layout)

def main():
    app = QApplication(sys.argv)
    
    ex = App()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()