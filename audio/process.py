#!/usr/bin/env python3
import random
from audio.journal import *

def joke():
    jokes = [
        "What do you call a computer floating in the ocean? A Dell Rolling in the Deep",
        "There are 10 types of people in the world: those who understand binary, and those who don’t",
        "An SQL statement walks into a bar and sees two tables. It approaches, and asks “may I join you?”",
        "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
        "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat",
        "A programmer’s wife tells him, “While you’re at the grocery store, buy some eggs.” He never comes back"
    ]
    index = random.randint(0,5)
    print(jokes[index])

def breathe():
    print("Beginning breathing exercises")
    # Display visual aide and play exercise audio
    # OR display youtube video

def medication():
    print("Okay, what time would you like to set the medication for?")
    # Listen again for time
    print("Okay, how often do you want the medication reminder?")
    # Listen again for frequency
    # Set reminder

def light_on():
    print("Okay, turning on lights")
    # Turn on lights

def light_off():
    print("Okay, turning off lights")
    # Turn off lights

def talk():
    print("Okay, what's up?")
    # Record (maybe on a loop) and hit therapy api

def journal():
    handle_journal()