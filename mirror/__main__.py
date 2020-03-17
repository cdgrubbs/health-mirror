import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QTimer
from mirror.widgets.clock import Clock

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

        layout = QGridLayout()
        clock_widget = Clock(self)
        layout.addWidget(clock_widget, 0, 0)
        clock_widget.show()

        self.setLayout(layout)
        self.showFullScreen()

def main():
    app = QApplication(sys.argv)
    
    ex = App()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()