#LIST OF TASKS TO DO:
#1. Make the voice more "human ear friendly".
#2. Make  Artemis be able to respond to "what is" question sourcing to wikipedia.
#3. See the full potential of "pywhatkit".
#4. Add a value timer to how long Artmis needs to wait for speech until turning off (Current default value is too short).
#5. Find a way for Artemis to open applications on command.
#6. New libraries for more diverse functions.

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "artemis" in command:
                command = command.replace("artemis", "")
    except:
        pass
    return command

def run_artemis():
    command = take_command()
    #print(command)

    if "play" in command:
        song = command.replace("play", "")
        talk("playing:" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")

        #For AM / PM system:
        #time = datetime.datetime.now().strftime("%I:%M %p")

        print(time)
        talk("Current time is:" + time)

    elif "who is" or "what is" in command:
        something = command.replace("who is" or "what is", "")
        #nonliving = command.replace("what is", "")
        info = wikipedia.summary(something, 1)
        print(info)
        talk(info)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)

    else:
        print("Sorry, Artyom. I didn't hear what you said.")
          
while True:
    run_artemis()