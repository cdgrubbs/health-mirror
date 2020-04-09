import pyaudio
import wave
import speech_recognition as sr
from os import path

def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

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


def record_and_parse_audio():
    record_audio()
    while True:
        AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../output.wav")
        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file
        # recognize speech using Google Speech Recognition
        try:
            print("You said:")
            print(r.recognize_google(audio))
            wordString = r.recognize_google(audio)
            return wordString

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            print("Please try again")
            record_audio()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            print("Please try again")
            record_audio()


journal_entries = []


def journal():
    numbers = ["first", "second", "third", "fourth", "fifth"]
    for number in numbers:
        print("Say the {} thing you are grateful for".format(number))
        word_string = record_and_parse_audio()
        journal_entries.append(word_string)
        if len(journal_entries) > 50:
            journal_entries = journal_entries[1:]
