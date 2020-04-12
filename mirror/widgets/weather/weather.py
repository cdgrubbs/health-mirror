import sys
import requests
import json
import urllib.parse
import pycountry

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon


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
    request_str = 'https://api.openweathermap.org/data/2.5/weather?'


    def __init__(self, api_key='455a8cae3fea29e7e2e61e3dcdee84e3'):
        self.OPEN_WEATHER_API_KEY = api_key


    def set_location(self,zip_code = 48104, country_code = 'us'):
        # Encode into UTF-8 (UTF-8 is the default option)
        self.request_str +=  ('zip=' + str(zip_code) + ',' + str(country_code))
        return self


    def set_units(self, units='imperial'):
        self.request_str += '&units=imperial'
        return self


    def get(self):
        # Add the API key to the request
        self.request_str += '&appid=' + self.OPEN_WEATHER_API_KEY
        print('sending the request: ' + self.request_str)
        return WeatherResponse(requests.get(self.request_str))


class Weather():
    zip_code = 60607
    country_code = 'us' # US

    weather_data = None

    # https://openweathermap.org/
    # Ex uri: https://api.openweathermap.org/data/2.5/weather?zip=48118,us&units=imperial&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # template: api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid=455a8cae3fea29e7e2e61e3dcdee84e3
    # Condtion codes: https://openweathermap.org/weather-conditions
    def __init__(self):
        # super(Weather, self).__init__()
        # self.setParent(parent)

        self.weather_data = self.get_weather()
        print('Current weather data we keep track of from the request:\n' + self.weather_data.get_json())


    def get_weather(self):
        builder = WeatherRequestBuilder()
        response = builder.set_location(self.zip_code, self.country_code).set_units().get()
        return response.get_weather_data()


    def change_location(self, zip_code, country):
        try:
            self.country_code = pycountry.countries.search_fuzzy(country)[0].alpha_2
        except LookupError:
            print('could not find the country with the name ' + country)
            return
        self.zip_code = zip_code
    



class WeatherGUI(QWidget):
    weather = Weather()
    
    def __init__(self, parent):
        super().__init__()
        image = 'sun.png'
        self.setParent(parent)

        self.label = QLabel(image)
        self.label.setStyleSheet('color: white; font-size: 100px')
        self.label.setText(image)
        # pixmap = QPixmap(image)
        # print(str(pixmap))
        # self.label.setPixmap(pixmap)

    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()
