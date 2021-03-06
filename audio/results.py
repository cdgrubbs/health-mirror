#!/usr/bin/env python3

from pprint import pprint
from audio.process import *
from audio.utterances import *
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../output.wav")

def get_results():
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
        print(r.recognize_google(audio))
        #pprint(r.recognize_google(audio, show_all=True))  # pretty-print the recognition result
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print("\nMirror responds: ")
    wordString = r.recognize_google(audio)

    for utterance in TELL_JOKE:
        if utterance.lower() == wordString.lower():
            joke()

    for utterance in BREATHING:
        if utterance.lower() == wordString.lower():
            breathe()

    for utterance in MEDICATION:
        if utterance.lower() == wordString.lower():
            medication()

    for utterance in LIGHTS_ON:
        if utterance.lower() == wordString.lower():
            light_on()

    for utterance in LIGHTS_OFF:
        if utterance.lower() == wordString.lower():
            light_off()

    for utterance in TALK:
        if utterance.lower() == wordString.lower():
            talk()

    for utterance in JOURNAL:
        if utterance.lower() == wordString.lower():
            journal()