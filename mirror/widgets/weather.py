import sys
import requests
import json
import urllib.parse

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer


class WeatherData():
    weather_dict = {}

    def __init__(self, weather_dict):
        self.weather_dict = weather_dict
    
    def get_json(self):
        return json.dumps(self.weather_dict, indent=4)

    def get_item(self, item):
        return self.weather_dict.get(item)
    # TODO: Use the image_name to select the appropriate image to show on the screen
    # by returning a file path to the image stored in image_name
    def get_weather_icon(self):
        return self.get_item('icon')


    def get_description(self):
        return self.get_item('description')


    def get_weather_type(self):
        return self.get_item('main')

    def get_temperature(self):
        return self.get_item('temp')


class WeatherResponse():
    response = ''
    def __init__(self, response):
        self.response = response.json()


    def get_response(self):
        return self.response
    

    def get_weather_data(self):
        assert(len(self.response['weather']) == 1)
        weather_dict = self.response['weather'][0]
        weather_dict.update(self.response['main'])
        return WeatherData(weather_dict)
        


class WeatherRequestBuilder():
    OPEN_WEATHER_API_KEY = ''
    request_str = 'https://api.openweathermap.org/data/2.5/weather?q='


    def __init__(self, api_key='455a8cae3fea29e7e2e61e3dcdee84e3'):
        self.OPEN_WEATHER_API_KEY = api_key


    def set_location(self,city='Chicago', state='Illinois', country_code=1):
        # Encode into UTF-8 (UTF-8 is the default option)
        city = urllib.parse.quote(city)
        state = urllib.parse.quote(state)
        self.request_str +=  (city + ',' + state + ',' + str(country_code))
        return self


    def set_units(self, units='imperial'):
        self.request_str += '&units=imperial'
        return self


    def get(self):
        # Add the API key to the request
        self.request_str += '&appid=' + self.OPEN_WEATHER_API_KEY
        return WeatherResponse(requests.get(self.request_str))


class Weather():
    city = 'Ann Arbor'
    state = 'Michigan'
    country_code = 1 # US

    # https://openweathermap.org/
    # Ex uri: api.openweathermap.org/data/2.5/weather?q=Chelsea,Michigan,1&units=imperial&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # template: api.openweathermap.org/data/2.5/weather?q={city,state,country code}&units=[imperial, metric]&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # Condtion codes: https://openweathermap.org/weather-conditions
    def __init__(self):
        # super(Weather, self).__init__()
        # self.setParent(parent)

        weather_data = self.get_weather()
        print('Current weather data we keep track of from the request:\n' + weather_data.get_json())


    def get_weather(self):
        builder = WeatherRequestBuilder()
        response = builder.set_location(self.city, self.state, self.country_code).set_units().get()
        return response.get_weather_data()
        



    # def hide(self):
    #     self.label.hide()

    # def show(self):
    #     self.label.show()

print('running python file...')

obj = Weather()


