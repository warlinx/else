import speech_recognition as sr
import pyttsx3
import os

start = pyttsx3.init()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("скажи что-нибудь")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task


def request(task):
    if "блокнот" in task:
        text = "открываю ваш блокнот"
        start.say(text)
        start.runAndWait()
        os.system('notepad')


while True:
    request(listen())