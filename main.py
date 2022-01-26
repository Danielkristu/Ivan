from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import datetime
import sys
from datetime import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pywikihow import search_wikihow
import keyboard
import time
import requests
from bs4 import BeautifulSoup

recognizer = sr.Recognizer()
speaker = tts.init()
current_time = datetime.now()
speaker.setProperty("rate", 170)
voices = speaker.getProperty("voices")  # gets you the details of the current voices
speaker.setProperty("voice", voices[1].id)

todo_list = ["Work", "Learn", "Sleep"]
schedule_list = [
    "Dinner appointment at 6 am saturday",
    "work meeting at 11 AM sunday twenty third",
]


def speak(audio):  # function for assistant to speak
    speaker.say(audio)
    speaker.runAndWait()  # without this command, the assistant won't be audible to us


def wishme():  # function to wish the user according to the daytime
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak(
        "I am Natalia, your Artificial intelligence assistant. Please tell me how may I help you"
    )


def listens():
    global recognizer
    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                listen = recognizer.recognize_google(audio)
                listen = listen.lower()

                done = True

                speak("wait a second sir!")

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand, please try again!")


def create_note():
    global recognizer

    speak("What do you want to write sir?")

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speak("Choose filename")

                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, "w") as f:
                f.write(note)
                done = True
                speak(f"I Successfully created the note {filename}")

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand you! Please try again!")


def add_todo():

    global recognizer

    speak(" What todo do you want to add?")

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speak(f"I added {item} to the to do list!")

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand, please try again!")


def show_todos():

    speak("The items on your to do list are the following")
    for item in todo_list:
        speak(item)


def hello():

    speak("hello Sir!, Welcome aboard, and what can I do for you sir?")


def master():

    speak("youre Daniel! and you are my master!")


def quit():
    speak("are you sure sir?, all program will be lost!")
    if "yes" in takecommand():
        speak("Goodbye Sir!")
        sys.exit()
    elif "no" in takecommand():
        speak("affimartive, cancelling shut down")


def schedule():

    global recognizer

    speak("Yes sir!, What appointment do you wanna add?")

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                schedule = recognizer.recognize_google(audio)
                schedule = schedule.lower()

                schedule_list.append(schedule)
                done = True

                speak(f"I added {schedule} to your schedule sir!")

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speak("I did not understand, please try again!")


def show_schedule():

    speak("This is your schedule sir")
    for schedule in schedule_list:
        speak(schedule)


def rio():

    speak("i know him, he is RIO, fel tanu boyfriend")


def arlene():

    speak("ofcourse i know him sir, he is atnanta, zefanya boyfriend")


def gordon():

    speak("oh, i know he is gordon, rios best friend!")


def dates():

    speak(datetime.date(datetime.now()))


def clocks():
    speak(f"its, {current_time.hour} and {current_time.minute} minutes")


def misuh():
    speak("sorry motherfucker that i have to disturb you!")


def chrome():
    speak("openning google chrome")
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")


def youtube():
    speak("openning youtube")
    webbrowser.open("https://www.youtube.com/")


def spotify():
    query = takecommand()
    if "open spotify" in query or "i want to hear some music" in query:
        speak("openning your spotify")
        os.system("spotify")
        time.sleep(4)
        keyboard.press("space bar")

    elif "start spotify" in query or "stop spotify" in query:
        keyboard.press("space bar")

    elif "close spotify" in query:
        os.system("TASKKILL /F /IM spotify.exe")


def github():
    speak("openning your github repository sir!")
    webbrowser.open("https://github.com/Danielies367")


def takecommand():

    global recognizer
    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                print("listening.....")
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                listen = recognizer.recognize_google(audio)
                listen = listen.lower()
                print(f"{listen}")
                print("recognizing.....")
                done = True

        except sr.UnknownValueError:

            recognizer = sr.Recognizer()
            return "none"
        return listen


def func():

    while True:
        query = takecommand()

        if "wake up natalia" in query or "wake up" in query:
            speak("i am already online sir!")

        elif (
            "please create a new note" in query
            or "new note" in query
            or "create a new note" in query
            or "i want to create a note" in query
        ):
            create_note()

        elif (
            "shut up" in query
            or "thankyou" in query
            or "goodbye" in query
            or "i have to go" in query
        ):
            quit()

        elif (
            "i want to at to do" in query
            or "at a new to do" in query
            or "at this to my to do list" in query
            or "make a new item for my to do list" in query
        ):
            add_todo()

        elif (
            "show my to do" in query
            or "what are my to do natalya?" in query
            or "check my to do" in query
            or "read my to do list" in query
        ):
            speak("The items on your to do list are the following")
            for item in todo_list:
                speak(item)

        elif (
            "can you make me schedule" in query
            or "can you make me appointment" in query
            or "can you add new schedule" in query
            or "new schedule" in query
        ):
            schedule()

        elif (
            "can you show my schedule" in query
            or "can you show my appointment" in query
            or "show my schedule" in query
            or "what is my schedule" in query
        ):
            show_schedule()

        elif (
            "what is my name Natalya" in query
            or "say my name" in query
            or "do you remember me" in query
            or "who is your master" in query
        ):
            master()

        elif (
            "who is rio" in query
            or "do you now rio" in query
            or "do you remember rio" in query
        ):
            rio()

        elif (
            "do you know atnanta girlfriend" in query
            or "do you now atnanta" in query
            or "girlfriend" in query
        ):
            arlene()

        elif (
            "do you know gordon best friend" in query
            or "do you know gordon" in query
            or "best friend" in query
        ):
            gordon()

        elif (
            "what day is it" in query
            or "do you know what date is today" in query
            or "day" in query
        ):
            dates()

        elif (
            "what time is it" in query
            or "do you know what time is it" in query
            or "time" in query
        ):
            clocks()

        elif "close google" in query:
            speak("closing")
            os.system("TASKKILL /F /IM chrome.exe")

        elif (
            "open new tab" in query
            or "open google" in query
            or "open google natalya" in query
        ):
            chrome()

        elif (
            "open youtube" in query
            or "can you open youtube for me" in query
            or "youtube" in query
            or "open youtube natalya" in query
        ):
            youtube()

        elif (
            "open spotify" in query
            or "can you open spotify for me" in query
            or "open spotify natalya" in query
            or "i want to hear some music" in query
        ):
            speak("openning your spotify")
            os.system("spotify")
            time.sleep(4)
            keyboard.press("space bar")

        elif "start spotify" in query or "stop spotify" in query:
            keyboard.press("space bar")

        elif "volume up" in query:
            os.system("spotify")
            keyboard.press("ctrl + up arrow")

        elif "volume down" in query:
            os.system("spotify")
            keyboard.press("ctrl + down arrow")

        elif "close spotify" in query:
            speak("closing")
            os.system("TASKKILL /F /IM spotify.exe")

        elif (
            "open my github" in query
            or "github" in query
            or "open my github natalya" in query
            or "i want to see my repositories" in query
        ):
            github()

        elif "temperature" in query:
            speak("which city do you want to know sir")
            city = takecommand().lower()
            search = f"weather in {city}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif (
            "open tik-tok" in query
            or "tik-tok" in query
            or "open tik-tok natalya" in query
        ):
            speak("openning your tik tok")
            os.system("TikTok")

        elif "close tik tok" in query:
            speak("closing")
            os.system("TASKKILL /F /IM tiktok.exe")

        elif "close zoom" in query:
            speak("closing")
            os.system("TASKKILL /F /IM Zoom.exe")

        elif (
            "open zoom" in query
            or "i want to start meeting" in query
            or "start meeting" in query
        ):
            os.system("Zoom_launcher")

        elif "search" in query:
            speak("what do you want to search sir")
            searchs = takecommand().lower()
            search = f"{searchs}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.content, "html5lib")
            answer = data.find("div")
            speak(f"{answer}")

        elif "sleep now" in query or "sleep" in query:
            speak("okay sir, you can call me anytime!")
            break


wishme()
func()


if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission or "natalia" in permission:
            speak("I am back online sir")
            func()
        elif "goodbye" in permission:
            quit()
