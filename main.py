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
import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import cv2
import numpy as np
import pyautogui
import pyjokes
import random
import hashlib
import mediapipe as mp
from Detectmod import detect
from Trainmodel import TrainMod
from Learnmodel import LearnMod, csv_coords_new_file
import cv2  # Import opencv
import csv
import os
import numpy as np
import pandas as pd
import speech_recognition as sr
import pickle
import pandas as pd

mp_drawing = mp.solutions.drawing_utils  # Drawing helpers
mp_holistic = mp.solutions.holistic  # Mediapipe Solutions
cap = cv2.VideoCapture(0)

with open(
    "D:\Eagleies\SLAVIK AI Project\slavik\BodyLanguageDecoder/body_language.pkl", "rb"
) as f:
    model = pickle.load(f)


recognizer = sr.Recognizer()
speaker = tts.init()
current_time = datetime.now()
speaker.setProperty("rate", 170)
voices = speaker.getProperty("voices")  # gets you the details of the current voices
speaker.setProperty("voice", voices[1].id)
gsearch = search

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


def source():

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
        speak("okay sir, i will close the program")
        sys.exit()
    else:
        speak("okay sir, i will continue the program")


def schedule():

    global recognizer

    speak("What do you want to do sir?")

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

    speak("The items on your schedule are the following")
    for schedule in schedule_list:
        speak(schedule)


def rio():

    speak("i know him, he is RIO, fel tanu boyfriend")


def arlene():

    speak("ofcourse i know him sir, he is atnanta, zefanya boyfriend")


def gordon():

    speak("oh, i know he is gordon, rios best friend!")


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
        speak("opening spotify")
        os.system("spotify")
        time.sleep(4)
        pyautogui.press("space bar")

    elif "start spotify" in query or "stop spotify" in query:
        pyautogui.press("space bar")

    elif "close spotify" in query:
        os.system("TASKKILL /F /IM spotify.exe")


def github():
    speak("openning your github repository sir!")
    webbrowser.open("https://github.com/Danielies367")


"""show real time clock"""


def clock():
    while True:
        current_time = datetime.now()
        print(current_time.hour, ":", current_time.minute, ":", current_time.second)
        speak(f"its, {current_time.hour} and {current_time.minute} minutes")
        time.sleep(1)
        break


"""show date"""


def date():
    while True:
        print(datetime.date(datetime.now()))
        speak(datetime.date(datetime.now()))
        time.sleep(1)
        break


"""show my files"""


def my_files():
    os.startfile("D:\Eagleies\SLAVIK AI Project")


"""open camera"""


def camera():
    speak("opening camera")
    os.system("start microsoft.windows.camera:")


"""close camera"""


def close_camera():
    os.system("TASKKILL /F /IM microsoft.windows.camera:")


"""open google classroom"""


def classroom():
    speak("opening google classroom")
    os.system("start chrome https://classroom.google.com/")


"""open notepad"""


def notepad():
    speak("opening notepad")
    os.system("start notepad")


"""close notepad"""


def close_notepad():
    speak("closing notepad")
    os.system("TASKKILL /F /IM notepad.exe")


"""search in google"""


def searchss():
    query = takecommand()
    if "search" in query:
        speak("what do you want to search sir?")
        query = takecommand()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Here is what i found for {query}")


"""open discord"""


def discord():
    speak("opening discord")
    os.system("start chrome https://discord.com/")


"""close discord"""


def close_discord():
    speak("closing discord")
    os.system("TASKKILL /F /IM discord.exe")


"""take a photo"""


def photo():
    speak("opening camera")
    os.system("start microsoft.windows.camera:")
    speak("taking photo")
    time.sleep(3)
    pyautogui.press("space bar")
    time.sleep(3)
    pyautogui.press("enter")


"""make a note"""


def note():
    speak("what do you want to note sir?")
    note = takecommand()
    file = open("note.txt", "w")
    file.write(note)
    file.close()
    speak("note created")


"""show note"""


def show_note():
    file = open("note.txt", "r")
    print(file.read())
    speak(file.read())
    file.close()


"""delete note"""


def delete_note():
    file = open("note.txt", "w")
    file.close()
    speak("note deleted")


"""build an alarm clock"""


def alarm():
    speak("what time do you want to set the alarm?")
    time = takecommand()
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[2])
    speak("do you want to set the alarm once or repeat?")
    repeat = takecommand()
    if "once" in repeat:
        while True:
            if current_time.hour == hour and current_time.minute == minute:
                speak("the alarm is ringing")
                break
            else:
                continue
    elif "repeat" in repeat:
        while True:
            if current_time.hour == hour and current_time.minute == minute:
                speak("the alarm is ringing")
                break
            else:
                continue


"""call a friend"""


def message(number):
    speak("what is the number or who is the person you want to message?")
    number = takecommand()
    number = number.replace("/", "")
    number = number.replace(" ", "")
    number = number.replace("-", "")
    print(number)
    speak("what do you want to message?")
    os.system(f"start chrome https://wa.me/{number}")
    time.sleep(4)
    message = takecommand()
    pyautogui.write(f"{message}")
    time.sleep(1)
    pyautogui.press("enter")  # press enter to call


"""message specific person"""


def messages(number):
    number = number.replace("/", "")
    number = number.replace(" ", "")
    number = number.replace("-", "")
    print(number)
    speak("what do you want to message?")
    os.system(f"start chrome https://wa.me/{number}")
    time.sleep(4)
    message = takecommand()
    pyautogui.write(f"{message}")
    time.sleep(1)
    pyautogui.press("enter")  # press enter to call


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


"""enviroment setup"""


def enviroment():
    speak("setting up your enviroment sir!")
    speak("installing dependencies")
    os.system("pip install -r requirements.txt")
    speak("dependencies installed")
    speak("installing python-telegram-bot")
    os.system("pip install python-telegram-bot")
    speak("python-telegram-bot installed")
    speak("installing pyttsx3")
    os.system("pip install pyttsx3")
    speak("pyttsx3 installed")
    speak("installing speech recognition")
    os.system("pip install speechrecognition")
    speak("speech recognition installed")
    speak("installing pyaudio")
    os.system("pip install pyaudio")
    speak("pyaudio installed")
    speak("installing pywin32")
    os.system("pip install pywin32")
    speak("pywin32 installed")
    speak("installing pyautogui")
    os.system("pip install pyautogui")
    speak("pyautogui installed")
    speak("installing wikipedia")
    os.system("pip install wikipedia")
    speak("wikipedia installed")
    speak("installing bs4")
    os.system("pip install bs4")
    speak("bs4 installed")
    speak("installing cv2")
    os.system("pip install cv2")
    speak("cv2 installed")
    speak("installing os")
    os.system("pip install os")
    speak("os installed")
    speak("installing webbrowser")
    os.system("pip install webbrowser")
    speak("webbrowser installed")
    speak("installing smtplib")
    os.system("pip install smtplib")
    speak("smtplib installed")
    speak("installing googlesearch")
    os.system("pip install googlesearch")
    speak("googlesearch installed")
    speak("installing time")
    os.system("pip install time")
    speak("time installed")
    speak("installing pywikihow")
    os.system("pip install pywikihow")
    speak("pywikihow installed")
    speak("installing pyjokes")
    os.system("pip install pyjokes")
    speak("pyjokes installed")


"""play a jokes"""


def jokes():
    speak("haha here is a joke")
    joke = pyjokes.get_joke()
    speak(joke)


"""open adobe premiere pro"""


def premiere():
    speak("opening adobe premiere pro")
    os.startfile(
        "C:\Program Files\Adobe\Adobe Premiere Pro 2021\Adobe Premiere Pro.exe"
    )  # open adobe premiere pro""


"""generate a random number"""


def random_number():
    speak("generating a random number")
    number = random.randint(1, 100)
    print(number)
    speak(f"your random number is {number}")


"""generate password"""


def password():
    speak("how long do you want your password to be")
    length = takecommand()
    length = int(length)
    speak("what do you want to use for your password")
    password = takecommand()
    password = password.split()
    password = "".join(password)
    password = password * length
    print(password)
    speak(f"your password is {password}")


"""generate an encrypted password"""


def encrypt():
    speak("what is the password you want to encrypt")
    password = takecommand()
    password = password.split()
    password = "".join(password)
    password = password.encode()
    password = hashlib.sha256(password).hexdigest()
    print(password)
    speak(f"your encrypted password is {password}")


"""decrypt an encrypted password"""


def decrypt(encrypted_password):
    encrypted_password = encrypted_password.split()
    encrypted_password = "".join(encrypted_password)
    encrypted_password = encrypted_password.encode()
    encrypted_password = hashlib.sha256(encrypted_password).hexdigest()
    print(encrypted_password)
    speak(f"your decrypted password is {encrypted_password}")


"""listen to the user"""


def listenss():
    speak("listening")
    os.system("start chrome https://www.google.com/")
    time.sleep(4)
    speak("what do you want to search for?")
    search = takecommand()
    search = search.split()
    search = " ".join(search)
    print(search)
    speak(f"searching for {search}")
    os.system(f"start chrome https://www.google.com/search?q={search}")


"""open camera"""


def camera():

    ################################
    wCam, hCam = 1280, 720
    ################################

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    while True:

        # Capture the video frame
        # by frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow("Your Pretty Face", frame)
        func()
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


"""code for sending mail"""


def send_mail():
    riomail = "rionardosupardy123@gmail.com"
    arlenmail = "hadrianreith12@gmail.com"
    email = "danielkris.photography@gmail.com"
    password = "gendatzbesar"
    speak("what is the email address you want to send the message to")
    query = takecommand()
    if "rio" in query:
        to = riomail
    else:
        to = arlenmail

    speak("what is the subject of the message")
    subject = "test"
    speak("what is the message you want to send")
    message = takecommand()
    speak("sending mail")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to, message)
        server.quit()
        speak("mail sent successfully")
    except:
        speak("mail not sent")


def DetectModel():
    wCam, hCam = 1280, 720
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    # Initiate holistic model
    with mp_holistic.Holistic(
        min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as holistic:

        while cap.isOpened():
            ret, frame = cap.read()

            # Recolor Feed
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make Detections
            results = holistic.process(image)
            # print(results.face_landmarks)

            # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks

            # Recolor image back to BGR for rendering
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # 1. Draw face landmarks
            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_TESSELATION,
                mp_drawing.DrawingSpec(
                    color=(80, 110, 10), thickness=1, circle_radius=1
                ),
                mp_drawing.DrawingSpec(
                    color=(80, 256, 121), thickness=1, circle_radius=1
                ),
            )

            # 2. Right hand
            mp_drawing.draw_landmarks(
                image,
                results.right_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(
                    color=(80, 22, 10), thickness=2, circle_radius=4
                ),
                mp_drawing.DrawingSpec(
                    color=(80, 44, 121), thickness=2, circle_radius=2
                ),
            )

            # 3. Left Hand
            mp_drawing.draw_landmarks(
                image,
                results.left_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(
                    color=(121, 22, 76), thickness=2, circle_radius=4
                ),
                mp_drawing.DrawingSpec(
                    color=(121, 44, 250), thickness=2, circle_radius=2
                ),
            )

            # 4. Pose Detections
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(
                    color=(245, 117, 66), thickness=2, circle_radius=4
                ),
                mp_drawing.DrawingSpec(
                    color=(245, 66, 230), thickness=2, circle_radius=2
                ),
            )
            # Export coordinates
            try:
                # Extract Pose landmarks
                pose = results.pose_landmarks.landmark
                pose_row = list(
                    np.array(
                        [
                            [landmark.x, landmark.y, landmark.z, landmark.visibility]
                            for landmark in pose
                        ]
                    ).flatten()
                )

                # Extract Face landmarks
                face = results.face_landmarks.landmark
                face_row = list(
                    np.array(
                        [
                            [landmark.x, landmark.y, landmark.z, landmark.visibility]
                            for landmark in face
                        ]
                    ).flatten()
                )

                # Concate rows
                row = pose_row + face_row

                #             # Append class name
                #             row.insert(0, class_name)

                #             # Export to CSV
                #             with open('coords.csv', mode='a', newline='') as f:
                #                 csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #                 csv_writer.writerow(row)

                # Make Detections
                X = pd.DataFrame([row])
                body_language_class = model.predict(X)[0]
                body_language_prob = model.predict_proba(X)[0]
                print(f"{body_language_class}")

                # Grab ear coords
                coords = tuple(
                    np.multiply(
                        np.array(
                            (
                                results.pose_landmarks.landmark[
                                    mp_holistic.PoseLandmark.LEFT_EAR
                                ].x,
                                results.pose_landmarks.landmark[
                                    mp_holistic.PoseLandmark.LEFT_EAR
                                ].y,
                            )
                        ),
                        [640, 480],
                    ).astype(int)
                )

                cv2.rectangle(
                    image,
                    (coords[0], coords[1] + 5),
                    (coords[0] + len(body_language_class) * 20, coords[1] - 30),
                    (245, 117, 16),
                    -1,
                )
                cv2.putText(
                    image,
                    body_language_class,
                    coords,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )

                # Get status box
                cv2.rectangle(image, (0, 0), (250, 60), (245, 117, 16), -1)

                # Display Class
                cv2.putText(
                    image,
                    "CLASS",
                    (95, 12),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                    1,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    image,
                    body_language_class.split(" ")[0],
                    (90, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )

                # Display Probability
                cv2.putText(
                    image,
                    "PROB",
                    (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 0),
                    1,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    image,
                    str(round(body_language_prob[np.argmax(body_language_prob)], 2)),
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )

            except:
                pass

            cv2.imshow("Raw Webcam Feed", image)

            if cv2.waitKey(10) or 0xFF == ord("q"):
                break


cap.release()
cv2.destroyAllWindows()
time.sleep(1)


def func():

    while True:
        query = takecommand()

        if "wake up natalia" in query or "wake up" in query:
            speak("hello sir!")

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
            speak("here is your to do list")
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
            date()

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
            "open spotify" in query
            or "can you open spotify for me" in query
            or "open spotify natalya" in query
            or "i want to hear some music" in query
        ):
            speak("opening spotify")
            os.system("spotify")
            time.sleep(4)
            pyautogui.press("space bar")

        elif "start spotify" in query or "stop spotify" in query:
            pyautogui.press("space bar")

        elif "volume up" in query:
            os.system("spotify")
            pyautogui.press("ctrl + up arrow")

        elif "volume down" in query:
            os.system("spotify")
            pyautogui.press("ctrl + down arrow")

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
            os.system("start Zoom meeting")

        elif "who is" in query:
            searchs = takecommand().lower()
            query = query.replace("search", "")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            search = f"{searchs}"
            url = f"https://www.google.com/search?q={search}"
            answer = wikipedia.summary(search, 2)
            print(answer)
            speak(answer)

        elif "tutorial" in query or "i want to search tutorial" in query:
            speak("what tutorial do you want to search sir")
            how = takecommand().lower()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif "open whatsapp" in query:
            speak("openning whatsapp")
            os.system("WhatsApp.exe")

        elif "close whatsapp" in query:
            speak("closing")
            os.system("TASKKILL /F /IM Whatsapp.exe")

        elif "open facebook" in query:
            speak("openning facebook")
            webbrowser.open("https://www.facebook.com/")

        elif "open instagram" in query:
            speak("openning instagram")
            webbrowser.open("https://www.instagram.com/")

        elif "open twitter" in query:
            speak("openning twitter")
            webbrowser.open("https://www.twitter.com/")

        elif "open youtube" in query:
            speak("openning youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            speak("openning google")
            webbrowser.open("https://www.google.com/")

        elif "open new tab" in query:
            speak("openning new tab")
            webbrowser.open_new_tab("https://www.google.com/")

        elif "time" in query:
            clock()

        elif "open gmail" in query:
            speak("openning gmail")
            webbrowser.open("https://www.gmail.com/")

        elif "current project folder" in query or "current project file" in query:
            speak("opening current project folder")
            my_files()

        elif "open my camera" in query or "camera" in query:
            camera()

        elif "classroom" in query or "class" in query:
            classroom()

        elif "close camera" in query:
            close_camera()

        elif "notepad" in query or "open notepad" in query:
            notepad()

        elif "close notepad" in query:
            close_notepad()

        elif "search" in query:
            searchss()

        elif "open discord" in query:
            discord()

        elif "close discord" in query:
            close_discord()

        elif "message rio" in query:
            messages("+6282124650547")

        elif "message hadrian" in query:
            messages("+6281319965080")

        elif "open canva" in query:
            speak("openning canva")
            webbrowser.open("https://www.canva.com/")

        elif "tell me a jokes" in query or "jokes" in query:
            jokes()

        elif "generate random number" in query or "random number" in query:
            random_number()

        elif "train my model" in query:
            speak("wait a second")
            TrainMod()
            speak("your model have been trained")

        elif "learn my model" in query:
            speak("what class name for your model sir")
            class_name = takecommand().lower()
            speak("okay sir, please wait a moment")
            LearnMod(f"{class_name}")

        elif "open detection" in query:
            speak("wait a second")
            detect()

        elif "clear model file" in query:
            speak("wait a second")
            csv_coords_new_file()
            speak("your model file have been cleared")

        elif (
            "close detection" in query
            or "stop training" in query
            or "stop learning" in query
        ):
            pyautogui.press("q")

        elif "sleep now" in query or "sleep" in query:
            speak("okay sir, you can call me anytime!")
            break


# enviroment()
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

