# Eve
My personal digital assistant that can perform various tasks on my desktop using voice commands.

## Version 1 (Deprecated)
Uses Microsoft Azure [Cognitive Services](https://azure.microsoft.com/en-us/products/cognitive-services/?&ef_id=Cj0KCQiAx6ugBhCcARIsAGNmMbjzcBbWEp4sgB6VLshWLdsuN098SrsJi6BROeoOXpcSd814eqdEtkAaAvsfEALw_wcB:G:s&OCID=AIDcmm5edswduu_SEM_Cj0KCQiAx6ugBhCcARIsAGNmMbjzcBbWEp4sgB6VLshWLdsuN098SrsJi6BROeoOXpcSd814eqdEtkAaAvsfEALw_wcB:G:s&gclid=Cj0KCQiAx6ugBhCcARIsAGNmMbjzcBbWEp4sgB6VLshWLdsuN098SrsJi6BROeoOXpcSd814eqdEtkAaAvsfEALw_wcB#features) to perform speech to text synthesis to convert verbal commands into text. The text is used to perform actions, currently supports opening specific hardcoded applications such as Google Chrome, Spotify, Google Calendar, Gmail, Valorant, Visual Studio Code. Version 1 can also speak back to the user. It performs a greeting on startup and whether not application(s) were opened or not.


## Version 2 (Deprecated)
Moved away from Microsoft Azure and instead uses [Speech Recognition](https://pypi.org/project/SpeechRecognition/) and [pyttsx3](https://pypi.org/project/pyttsx3/) Python libraries to perform speech to text and text to speech synthesis. Added more commands such as terminating itself, rerunning itself, locking computer, cycling through foreground windows, and searching google. Messed around with energy threshold for the speech recognizer to determine good threshold for picking up microphone audio.  


## Version 3 (Current)
Added more commands, notably being able to focus a specific window using its name, ie "focus Chrome" or "focus Spotify". Eve brings the application to the foreground if it is running. I had to add a dictionary to store the application name with all the running instances of it so this could be achieved. I used [win32gui](https://pypi.org/project/win32gui/) and win32process Python libraries to access the running applications, and win32con to change the size of the application when brought to the foreground.

I also added music features: specifically playing and pausing music (using the "toggle music" command) and raising and lowering volume by a certain amount. It can also play the previous or next song. These commands are achieved by using [pyautogui](https://pyautogui.readthedocs.io/en/latest/) which mimics keyboard actions. 

Also supports closing the tab if a chrome application is currently in the foreground. 

Added "list commands" command that enumerates all the commands Eve can currently do.

## What's next?
- Add more commands
- Process input speech more efficiently, possibly have a wake up phrase.  
- Move away from hardcoding commands (would require some NLP or AI model)
