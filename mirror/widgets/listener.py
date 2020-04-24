import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
from PyQt5.QtCore import Qt, QRect, QTimer
import pyaudio
import wave
from pprint import pprint
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
WAVE_OUTPUT_FILENAME = "audio_recording.wav"
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

READ_JOURNAL = [
    "read journal"
]

REFLECTION = [
    "reflection",
    "reflection time"
]

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../../output.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../../audio_recording.wav")

def record_audio():
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

    OUTPUT_FILE = path.join(path.dirname(path.realpath(__file__)), "../../audio_recording.wav")
    wf = wave.open(OUTPUT_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def record_and_parse_audio():
    while True:
        record_audio()

        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)

        try:
            print("You said:")
            wordString = r.recognize_google(audio)
            print(wordString)
            return wordString

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            print("Please try again")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            print("Please try again")

class Listener(QWidget):
    def __init__(self, parent):
        super(Listener, self).__init__()
        # self.record_audio()
        # time.sleep(5)
        # self.get_results()
        # self.setParent(parent)

    def doListener(self):
        record_audio()
        time.sleep(5)
        return self.get_results()

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

        print('searching for widget')
        widgetName = 'nothing found'
        for utterance in TELL_JOKE:
            if utterance.lower() == wordString.lower():
                widgetName = 'joke'

        for utterance in BREATHING:
            if utterance.lower() == wordString.lower():
                widgetName = 'breathe'

        for utterance in MEDICATION:
            if utterance.lower() == wordString.lower():
                widgetName = 'reminder'

        for utterance in TALK:
            if utterance.lower() == wordString.lower():
                widgetName = 'talk'

        for utterance in JOURNAL:
            if utterance.lower() == wordString.lower():
                widgetName = 'journal'
            
        for utterance in READ_JOURNAL:
            if utterance.lower() == wordString.lower():
                widgetName = 'read_journal'
        
        for utterance in REFLECTION:
            if utterance.lower() == wordString.lower():
                widgetName = 'reflection'

        return widgetName

    def hide(self):
        self.label.hide()

    def show(self):
        self.label.show()
