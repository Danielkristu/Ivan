from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys


recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty("rate", 180)

todo_list = ["Work", "Learn", "Sleep"]


def create_note():
    global recognizer

    speaker.say("What do you want to write sir?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose filename")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, "w") as f:
                f.write(note)
                done = True
                speaker.say(f"I Successfully created the note {filename}")
                speaker.runAndWait()

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()


def add_todo():

    global recognizer

    speaker.say(" What todo do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"I added {item} to the to do list!")
                speaker.runAndWait()

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand, please try again!")
            speaker.runAndWait()


def show_todos():

    speaker.say("The items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():

    speaker.say("Hello, What can I do for you?")
    speaker.runAndWait()


def quit():
    speaker.say("Thankyou, Goodbye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit,
}


assistant = GenericAssistant("intents.json", intent_methods=mappings)
assistant.train_model()


while True:

    try:
        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()

