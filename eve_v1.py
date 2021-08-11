from azure.cognitiveservices.speech import (
    AudioDataStream,
    SpeechConfig,
    SpeechSynthesizer,
    SpeechSynthesisOutputFormat,
    SpeechRecognizer,
)
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import os
import webbrowser
import time

subscriptionKey = "SUBSCRIPTION_KEY_HERE"
region = "eastus"

# Create a speech configuration
speech_config = SpeechConfig(subscription=subscriptionKey, region=region)
speech_config.speech_synthesis_voice_name = "en-GB-HazelRUS"
audio_config = AudioOutputConfig(use_default_speaker=True)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
speech_recognizer = SpeechRecognizer(speech_config=speech_config)


def tts(text):
    print(text)
    synthesizer.speak_text_async(text)


def from_mic():
    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    results = str(result.text).lower()
    if "open" in results:
        count = 0
        response = "Opening "
        if " chrome" in results:
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
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
            os.startfile("C:/Users/adamw/AppData/Local/Discord/app-1.0.9002/Discord")
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
            tts("No programs opened.")
        else:
            response = response.split(",")
            if count > 1:
                response[-2] = " and" + response[-2]
            combined_response = ""
            for i in range(len(response) - 1):
                combined_response += response[i]
            tts(combined_response)


# from_mic()


def main():
    if time.localtime().tm_hour >= 12:
        if time.localtime().tm_hour <= 18:
            greeting = "Good afternoon Adam,"
        else:
            greeting = "Good evening Adam,"
    else:
        greeting = "Good morning Adam,"
    greeting += " how may I help you?"
    tts(greeting)
    # from_mic()


if __name__ == "__main__":
    main()