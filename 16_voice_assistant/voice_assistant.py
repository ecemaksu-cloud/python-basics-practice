# Voice Assistant using Speech Recognition and Text-to-Speech

import os
import random
import time
import webbrowser
from datetime import datetime

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


recognizer = sr.Recognizer()


def speak(text):
    tts = gTTS(text, lang="tr")

    random_number = random.randint(1, 10000)
    file_name = f"voice-{random_number}.mp3"

    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)


def listen(prompt=False):
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)

        audio = recognizer.listen(source)
        voice_text = ""

        try:
            voice_text = recognizer.recognize_google(
                audio,
                language="tr-TR"
            )

        except sr.UnknownValueError:
            speak("Anlayamadım")

        except sr.RequestError:
            speak("Sistem çalışmıyor")

        return voice_text.lower()


def check_command(voice_text):
    if "nasılsın" in voice_text:
        speak("İyiyim, teşekkür ederim")

    elif "saat kaç" in voice_text:
        current_time = datetime.now().strftime("%H:%M")
        speak(current_time)

    elif "ara" in voice_text:
        time.sleep(1)

        search_query = listen("Ne aramak istiyorsun?")
        url = "https://google.com/search?q=" + search_query

        webbrowser.get().open(url)
        speak(search_query + " için bulduklarım")

    elif (
        "tamamdır" in voice_text
        or "kapa" in voice_text
        or "çık" in voice_text
    ):
        speak("Görüşmek üzere")
        exit()


speak("Nasıl yardımcı olabilirim?")
time.sleep(1)

while True:
    voice_text = listen()
    print(voice_text)
    check_command(voice_text)
