import pyttsx3
import speech_recognition as sr

# initiate syntez cheech
speak_engine = pyttsx3.init()

# initiate speech recognize
r = sr.Recognizer()
m = sr.Microphone(device_index=1)


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

