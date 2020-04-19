import sys

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


        # self.main_window = QWidget(self)
        # self.setCentralWidget(self.main_window)

        # self.main_window.setLayout(self.layout)



        # self.main_window.show()
    
    def init_window(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(palette)

        
        self.create_layout()
        # window_layout = QVBoxLayout()
        # window_layout.addWidget(self.main_window)
        # print('my laout ' + str(self.layout))
        # self.setLayout(window_layout)

        self.showFullScreen()


    def create_layout(self):
        self.main_window = QWidget(self)
        grid_layout = QGridLayout()

        grid_layout.addWidget(SimpleWidget(self,'red'), 0, 0)
        grid_layout.addWidget(SimpleWidget(self,'blue'), 0, 1)
        grid_layout.addWidget(SimpleWidget(self,'green'), 1, 1)
        grid_layout.addWidget(SimpleWidget(self,'white'), 2, 2)
        grid_layout.addWidget(Clock(self.main_window), 1, 0)
        grid_layout.addWidget(WeatherGUI(self.main_window), 2, 0)
        # grid_layout.addWidget(SimpleWidget(self.main_window), 0, 0)
        # grid_layout.addWidget(QPushButton('1'), 0, 0)
        # grid_layout.addWidget(QPushButton('2'), 0, 1)

        self.setLayout(grid_layout)

def main():
    app = QApplication(sys.argv)
    
    ex = App()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()