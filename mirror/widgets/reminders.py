from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer
from datetime import datetime
from mirror.widgets.listener import record_and_parse_audio


reminderTimer = QTimer()

class Reminders(QWidget):
    reminders = []

    def __init__(self, parent):
        super(Reminders, self).__init__()
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: white;')
        self.wordLabel.setGeometry(0, 0, 1000, 1000)


        reminderTimer.timeout.connect(self.doReminders)
        reminderTimer.start(5000)

    def doReminders(self):
        # Gets current date
        time = datetime.now()
        dayOfWeek = time.strftime("%A")
        hour = time.strftime("%-H")
        output = ""
        if (dayOfWeek == "Friday"):
            output += "Remember to go outside today\n"
        # Reminds user to take their medicine
        for medication, hour_med in self.reminders:
            if (str(hour_med) == str(hour)):
                output += "Reminder to take " + medication + "\n"
        self.wordLabel.setText(output)

    def setReminder(self):
        # Has users set their medication and when they need to take it
        question = "What is your medication?"
        self.wordLabel.setText(question)
        self.wordLabel.repaint()
        medication = record_and_parse_audio()

        question = "What time do you need to take your medication?\n(Specify hour and AM/PM)"
        self.wordLabel.setText(question)
        self.wordLabel.repaint()
        timeResponse = record_and_parse_audio()
        newList = timeResponse.split()
        hour = int(newList[0])
        zone = newList[1]

        if (zone == "p.m."):
            hour += 12
        self.reminders.append((medication, hour))
        self.wordLabel.setText("Medication Reminder Set")

    def show(self):
        self.resize(1000,1000)
        self.setVisible(True)
        self.wordLabel.show()

    def hide(self):
        self.wordLabel.hide()
