import sys
import requests
import json

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer


class Weather():
    city = 'Chelsea'
    state = 'Michigan'
    country_code = 1 # US

    OPEN_WEATHER_API_KEY = '455a8cae3fea29e7e2e61e3dcdee84e3'
    # https://openweathermap.org/
    # Ex uri: api.openweathermap.org/data/2.5/weather?q=Chelsea,Michigan,1&units=imperial&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # template: api.openweathermap.org/data/2.5/weather?q={city,state,country code}&units=[imperial, metric]&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # Condtion codes: https://openweathermap.org/weather-conditions
    def __init__(self):
        # super(Weather, self).__init__()
        # self.setParent(parent)

        self.get_weather()

    def get_weather(self):
        request_string = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.city + ',' + self.state + ',' + str(self.country_code) + '&units=imperial&appid=' + self.OPEN_WEATHER_API_KEY
        response = requests.get(request_string)
        print(response.status_code)
        print(json.dumps(response.json(), sort_keys=True, indent=4))


    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()

print('running python file...')

obj = Weather()