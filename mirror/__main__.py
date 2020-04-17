import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock
from mirror.widgets.listener import Listener
from audio.record import record_audio
from audio.results import get_results


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        # Changes background to black
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)
        self.setGeometry(0,0,200,200)

        layout = QGridLayout()
        clock_widget = Clock(self)
        listener = Listener(self)
        
        #Add widgets, can't get them to show up in different areas
        layout.addWidget(clock_widget, 0, 0, 100, -1)
        layout.addWidget(listener, 100, 0, 200, -1)

        #This will be unnecessary and switched once grid layout is figured out
        #clock_widget.hide()
        clock_widget.show()

        listener.show()

        print(layout.itemAt(0))
        print(layout.getItemPosition(0))
        print(layout.itemAt(1))
        print(layout.getItemPosition(1))

        self.setLayout(layout)
        self.showFullScreen()

def main():
    app = QApplication(sys.argv)
    
    ex = App()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()