import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer
import pyaudio
import wave
from pprint import pprint
import math
import random
import time
import webbrowser

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
TELL_JOKE = [
    "tell me a joke",
    "tell a joke",
    "tell me something funny",
    "joke",
    "jokes",
    "i need a joke",
    "i need a laugh",
    "i need to hear a joke"
]

BREATHING = [
    "help me breathe",
    "give me a breathing exercise",
    "take me through some breathing exercises"
]

MEDICATION = [
    "set a medication reminder"
]

LIGHTS_ON = [
    "turn the lights on",
    "turn the lights up"
    "lights on"
]

LIGHTS_OFF = [
    "turn the lights off",
    "lights off"
]

TALK = [
    "i need to talk to somebody",
    "talk to me"
]

JOURNAL = [
    "gratitude",
    "journal",
    "journaling",
    "gratitude journal",
    "add to gratitude journal"
    "i want to do some journaling",
    "i'd like to add to my gratitude journal",
    "i want to add to my gratitude journal"
]

REFLECTION = [
    "reflection",
    "reflection time"
]

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../../output.wav")

class Listener(QWidget):
    def __init__(self, parent):
        super(Listener, self).__init__()
        self.record_audio()
        time.sleep(5)
        self.get_results()
        self.setParent(parent)

    def record_audio(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    
    def record_and_parse_audio(self):
        while True:
            self.record_audio()

            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)

            try:
                print("You said:")
                print(r.recognize_google(audio))
                wordString = r.recognize_google(audio)
                return wordString

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                print("Please try again")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                print("Please try again")

    def get_results(self):
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
            # instead of `r.recognize_google(audio, show_all=True)`
            print("You said:")
            # print(r.recognize_google(audio))
            wordString = r.recognize_google(audio)
            print(wordString)
            #pprint(r.recognize_google(audio, show_all=True))  # pretty-print the recognition result
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return

        for utterance in TELL_JOKE:
            if utterance.lower() == wordString.lower():
                self.joke()

        for utterance in BREATHING:
            if utterance.lower() == wordString.lower():
                self.breathe()

        for utterance in MEDICATION:
            if utterance.lower() == wordString.lower():
                self.medication()

        for utterance in LIGHTS_ON:
            if utterance.lower() == wordString.lower():
                self.light_on()

        for utterance in LIGHTS_OFF:
            if utterance.lower() == wordString.lower():
                self.light_off()

        for utterance in TALK:
            if utterance.lower() == wordString.lower():
                self.talk()

        for utterance in JOURNAL:
            if utterance.lower() == wordString.lower():
                self.journal()

        for utterance in REFLECTION:
            if utterance.lower() == wordString.lower():
                self.reflection()

    def joke(self):
        jokes = [
            "What do you call a computer floating in the ocean? A Dell Rolling in the Deep",
            "There are 10 types of people in the world: those who understand binary, and those who don’t",
            "An SQL statement walks into a bar and sees two tables. It approaches, and asks “may I join you?”",
            "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
            "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat",
            "A programmer’s wife tells him, “While you’re at the grocery store, buy some eggs.” He never comes back"
        ]
        index = random.randint(0,5)
        self.label = QLabel(jokes[index])
        self.label.setParent(self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet('color: white; font-size: 18px')
    
    def breathe(self):
        print("Beginning breathing exercises")
        url = "https://www.youtube.com/watch?v=5DqTuWve9t8"
        #Display youtube video

    def medication(self):
        print("Okay, what time would you like to set the medication for?")
        # Listen again for time
        print("Okay, how often do you want the medication reminder?")
        # Listen again for frequency
        # Set reminder

    def light_on(self):
        print("Okay, turning on lights")
        # Turn on lights

    def light_off(self):
        print("Okay, turning off lights")
        # Turn off lights

    def talk(self):
        print("Okay, what's up?")
        # Record (maybe on a loop) and hit therapy api
        
    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()

    def journal(self):
        journal = []
        numbers = ["first", "second", "third"]
        for number in numbers:
            print("Say the {} thing you are grateful for".format(number))
            word_string = self.record_and_parse_audio()
            journal.append(word_string)
        output = "I am grateful for:\n"
        output += "1) " + journal[-3] + "\n"
        output += "2) " + journal[-2] + "\n"
        output += "3) " + journal[-1] + "\n"
        self.label = QLabel(output)
        self.label.setParent(self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet('color: white; font-size: 30px')
    
    def reflection(self):
        self.counter = 0

        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: white;')
        self.wordLabel.setGeometry(50, 50, 200, 100)

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
