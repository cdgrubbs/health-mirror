from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QRect, QTimer
import math

class Reflection(QWidget):
    def __init__(self, parent):
        super(Reflection, self).__init__()
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: white;')
        self.wordLabel.setGeometry(50, 50, 200, 100)
    
    def doReflection(self):
        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start(300)

    def onTimeout(self):
        if self.counter >= 30:
            self.timer.stop()
            self.wordLabel.hide()
            return

        self.wordLabel.setText("Reflection Time\n             " + str(math.ceil(30-self.counter)))
        self.counter += 0.3

    def show(self):
        self.wordLabel.show()
    
    def hide(self):
        self.wordLabel.hide()
