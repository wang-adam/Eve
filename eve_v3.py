import speech_recognition as sr
from word2number import w2n
import pyttsx3
import webbrowser
import os, sys
import time
import subprocess
import pyautogui
import psutil
import win32gui
import win32process
import win32con


# Speech engine
r = sr.Recognizer()
r.energy_threshold = 10000

# window object to focus applications
w=win32gui

# map of application name to set of application process ids.
open_applications = {}

running = True

# Converts text to speech
def speak(text):
    # eve_v1.tts(text)
    print(text)
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  
    engine.setProperty("rate", 250)
    engine.say(text)
    engine.runAndWait()
    del engine

# Greeting on start up
def greet_me():
    if time.localtime().tm_hour >= 12:
        if time.localtime().tm_hour <= 18:
            greeting = "Good afternoon Adam,"
        else:
            greeting = "Good evening Adam,"
    else:
        greeting = "Good morning Adam,"
    greeting += " how may I help you?"
    speak("Hello, I am Eve, Adam's Digital Assistant.")
    speak(greeting)


def main():
    w.EnumWindows(updateOpenApplications, None)
    greet_me()
    global globalvar
    globalvar = [1, 5]
    r.listen_in_background(sr.Microphone(), takeCommand, phrase_time_limit=5)


# Recreate mapping of open applications
def updateOpenApplications( hwnd, ctx ):
    if w.IsWindowVisible( hwnd ):
        pid = win32process.GetWindowThreadProcessId(hwnd)
        name = psutil.Process(pid[-1]).name()
        if name in open_applications:
            curr_processes = open_applications[name]
            curr_processes.add(hwnd)
        else:
            open_applications[name] = {hwnd}



def takeCommand(r, audio):
    try:
        global open_applications
        results = r.recognize_google(audio, language="en-in").lower()
        print("\n" + results)
        if results == "terminate":
            speak("I have stopped listening and will shut down. Goodbye.")
            global running
            running = False
            sys.exit()
            os._exit(0)
        elif results == "lock" or "lock computer" in results:
            cmd = "rundll32.exe user32.dll, LockWorkStation"
            subprocess.call(cmd)
        elif results == "rerun":
            speak("I am restarting, I'll be right back.")
            os.execv(sys.executable, ["python"] + sys.argv)
        elif "change window" in results:
            pyautogui.keyDown("alt")
            time.sleep(0.2)
            if "cycle" in results:
                pyautogui.keyDown("shift")
                time.sleep(0.2)
                results = results.replace("change window cycle","")
            else:
                results = results.replace("change window","")
            if results != "":
                try:
                    if "to" in results or "too" in results:
                        value = 2
                    else:
                        value = w2n.word_to_num(results)
                except Exception as e:
                    value = int(results)
            else:
                value = 1
            for i in range(value):
                pyautogui.press("tab")
            time.sleep(0.2)
            pyautogui.keyUp("alt")
            pyautogui.keyUp("shift")
        elif "focus" in results:
            focus_command(results)
        elif "search" in results:
            webbrowser.open_new_tab("https://www.google.com/search?q={}".format(results.replace("search", "")))
            open_applications = {}
            w.EnumWindows(updateOpenApplications, None)
        elif "open" in results:
            open_command(results)
        elif "close tab" in results:
            pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
            if psutil.Process(pid[-1]).name() == "chrome.exe":
                pyautogui.hotkey("ctrl","w")
                speak("Closing tab")
            else:
                speak("A web application is not focused")
        elif "toggle music" in results:
            pyautogui.press("playpause")
        elif "volume up" in results:
            results = results.replace("volume up","")
            if results != "":
                try:
                    value = w2n.word_to_num(results)
                except Exception as e:
                    value = int(results)
                value = int(value/2)
            else:
                value = 1
            print(value)
            for i in range(value):
                pyautogui.press("volumeup")
        elif "volume down" in results:
            results = results.replace("volume down","")
            if results != "":
                try:
                    value = w2n.word_to_num(results)
                except Exception as e:
                    value = int(results)
                value = int(value/2)
            else:
                value = 1
            print(value)
            for i in range(value):
                pyautogui.press("volumedown")
        elif "play next song" in results:
            pyautogui.press("nexttrack")
        elif "play previous song" in results:
            pyautogui.press("prevtrack")
            pyautogui.press("prevtrack")
        elif "list commands" in results:
            speak("Version 3 of me can perform the following actions: \n TERMINATE myself \n LOCK computer\n RERUN myself \n CHANGE WINDOW \n FOCUS <APPLICATION NAME> \n SEARCH the internet \n OPEN <APPLICATION NAME> \n TOGGLE MUSIC \n VOLUME UP or DOWN <AMOUNT> \n PLAY PREVIOUS or NEXT SONG \n LIST COMMANDS")



    except Exception as e:
        # global globalvar
        # sys.stdout.write(
        #     "\r[{0}{1}] ".format(
        #         "=" * globalvar[0], " " * (globalvar[1] - globalvar[0])
        #     )
        # )
        # if globalvar[0] > globalvar[1]:
        #     sys.stdout.write("\r[{0}] ".format(" " * (globalvar[0] - 1)))
        #     globalvar[0] = 1
        # else:
        #     globalvar[0] += 1
        # sys.stdout.flush()
        print("I'm listening...")
        print(e)


def open_command(results):
    global open_applications
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
    open_applications = {}
    w.EnumWindows(updateOpenApplications, None)
    


def focus_command(results):
    pyautogui.press("alt")
    if " chrome" in results:
        if "chrome.exe" in open_applications:
            w.ShowWindow(list(open_applications["chrome.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["chrome.exe"])[0])
        else:
            speak("Failed to focus Google Chrome.")
    elif " spotify" in results:
        if "Spotify.exe" in open_applications:
            w.ShowWindow(list(open_applications["Spotify.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["Spotify.exe"])[0])
        else:
            speak("Failed to focus Spotify.")
    elif " discord" in results:
        if "Discord.exe" in open_applications:
            w.ShowWindow(list(open_applications["Discord.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["Discord.exe"])[0])
        else:
            speak("Failed to focus Discord.")
    elif " valorant" in results:
        if "Valorant.exe" in open_applications:
            w.ShowWindow(list(open_applications["Valorant.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["Valorant.exe"])[0])
        else:
            speak("Failed to focus Valorant.")
    elif " vs code" in results:
        if "Code.exe" in open_applications:
            w.ShowWindow(list(open_applications["Code.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["Code.exe"])[0])
        else:
            speak("Failed to focus VS Code.")
    elif " powershell" in results:
        if "powershell.exe" in open_applications:
            w.ShowWindow(list(open_applications["powershell.exe"])[0], win32con.SW_SHOWMAXIMIZED)
            w.SetForegroundWindow(list(open_applications["powershell.exe"])[0])
        else:
            speak("Failed to focus Powershell.")
    else:
        speak("Failed to focus specified application")
    

if __name__ == "__main__":
    main()

while running:
    time.sleep(0.01)
    