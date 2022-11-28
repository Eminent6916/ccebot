"""
with pip
    install SpeechRecognition
    install PyAudio to use mic.
    install pywhatkit to search
    pyttxs3 text t speech
"""
from email.mime import audio
import pywhatkit
import pyaudio
import speech_recognition as s_r



def get_voice():
    voice_reciever = s_r.Recognizer()
    print("Speak up, I'm waiting...")
    with s_r.Microphone() as voice:
        audio= voice_reciever.listen(voice)
    words = voice_reciever.recognize_google(audio)
    print(f'you mean " {words}", Yes or No?')
    quest = input("  :> ")
    if quest.lower() == 'yes':
        pywhatkit.search(words)
    else:
        print("sorry, please re-count")
        voice_reciever = s_r.Recognizer()
        print("Speak up, I'm waiting...")
        with s_r.Microphone() as voice:
            audio= voice_reciever.listen(voice)
        words = voice_reciever.recognize_google(audio)
        print(f'you mean " {words}", Yes or No?')
        quest = input("  :> ")
        if quest.lower() == 'yes':
            pywhatkit.search(words)
        

get_voice()

import pyttsx3


