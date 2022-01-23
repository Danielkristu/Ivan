from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import datetime
import sys
from datetime import datetime
import wikipedia
import webbrowser
import os.path
import smtplib

recognizer = sr.Recognizer()
speaker = tts.init("sapi5")
current_time = datetime.now()
speaker.setProperty("rate", 155)
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
        speak("Good Morning")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(
        "Hello Sir, I am Natalya, your Artificial intelligence assistant. Please tell me how may I help you"
    )


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
    speak("Goodbye Sir!")
    sys.exit()


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


def dates():

    speak(datetime.date(datetime.now()))


def clocks():
    speak(f"its, {current_time.hour} and {current_time.minute} minutes")


def misuh():
    speak("sorry motherfucker that i have to disturb you!")


def chrome():
    speak("openning google chrome")
    webbrowser.open("https://www.google.com")


def youtube():
    speak("openning youtube dot com")
    webbrowser.open("https://www.youtube.com/")


def spotify():
    speak("openning your spotify")
    webbrowser.open("https://open.spotify.com/")


def github():
    speak("openning your github repository sir!")
    webbrowser.open("https://github.com/Danielies367")


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "schedule": schedule,
    "show_schedule": show_schedule,
    "master": master,
    "rios": rio,
    "arlenes": arlene,
    "dates": dates,
    "clocks": clocks,
    "misuh": misuh,
    "chrome": chrome,
    "youtube": youtube,
    "spotify": spotify,
    "github": github,
    "exit": quit,
}


assistant = GenericAssistant("intents.json", intent_methods=mappings)
assistant.train_model()
wishme()

while True:

    try:
        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=1)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()

