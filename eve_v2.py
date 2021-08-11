from hashlib import new
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os, sys
import time
import subprocess
import wolframalpha
import json
import requests
import pyaudio
import eve_v1

# Speech engine

r = sr.Recognizer()
r.energy_threshold = 1000

# converts text to speech
def speak(text):
    # eve_v1.tts(text)
    print(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()
    del engine


def greet_me():
    if time.localtime().tm_hour >= 12:
        if time.localtime().tm_hour <= 18:
            greeting = "Good afternoon Adam,"
        else:
            greeting = "Good evening Adam,"
    else:
        greeting = "Good morning Adam,"
    greeting += " how may I help you?"
    speak(greeting)


def main():
    greet_me()
    global globalvar
    globalvar = [1, 20]
    r.listen_in_background(sr.Microphone(), takeCommand, phrase_time_limit=5)
    print("Listening...")


def takeCommand(r, audio):
    try:
        results = r.recognize_google(audio, language="en-in").lower()
        print("\n" + results)
        if results == "stop":
            speak("I have stopped listening and will terminate. Goodbye.")
            os._exit(0)
        if results == "lock" or "lock computer" in results:
            cmd = "rundll32.exe user32.dll, LockWorkStation"
            subprocess.call(cmd)
        elif "open" in results:
            count = 0
            response = "Opening "
            if " chrome" in results:
                webbrowser.open_new_tab("https://google.com")
                response += "chrome, "
                count += 1

            if " spotify" in results:
                os.system("Spotify")
                response += "spotify, "
                count += 1

            if " calendar" in results:
                webbrowser.open_new_tab("https://calendar.google.com")
                response += "calendar, "
                count += 1

            if " email" in results:
                webbrowser.open_new_tab("https://gmail.google.com")
                response += "email, "
                count += 1

            if " discord" in results:
                os.startfile(
                    "C:/Users/adamw/AppData/Local/Discord/app-1.0.9002/Discord"
                )
                response += "discord, "
                count += 1

            if " valorant" in results:
                os.startfile(
                    "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Riot Games/VALORANT"
                )
                response += "valorant, "
                count += 1

            if " vs code" in results:
                os.startfile(
                    "C:/Users/adamw/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code"
                )
                response += "VS code, "
                count += 1

            if count == 0:
                speak("No programs opened.")
            else:
                response = response.split(",")
                if count > 1:
                    response[-2] = " and" + response[-2]
                combined_response = ""
                for i in range(len(response) - 1):
                    combined_response += response[i]
                speak(combined_response)
    except Exception as e:
        global globalvar
        sys.stdout.write(
            "\r[{0}{1}] ".format(
                "=" * globalvar[0], " " * (globalvar[1] - globalvar[0])
            )
        )
        if globalvar[0] > globalvar[1]:
            sys.stdout.write("\r[{0}] ".format(" " * (globalvar[0] - 1)))
            globalvar[0] = 1
        else:
            globalvar[0] += 1
        sys.stdout.flush()


if __name__ == "__main__":
    main()

while True:
    time.sleep(0.01)
