from audio.record import *

journal_entries = []

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

def handle_journal():
    numbers = ["first", "second", "third", "fourth", "fifth"]
    for number in numbers:
        print("Say the {} thing you are grateful for".format(number))
        word_string = record_and_parse_audio()
        journal_entries.append(word_string)
        if len(journal_entries) > 50:
            journal_entries = journal_entries[1:]
