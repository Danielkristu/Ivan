from multiprocessing import Process
import sys
import cv2
from Detectmod import DetectModel  # Import opencv
from main import func
import speech_recognition as sr
import threading


def a():

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
                done = True

        except sr.UnknownValueError:

            recognizer = sr.Recognizer()
            return "none"
        return listen


def b():

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
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


threading.Thread(target=a).start()
threading.Thread(target=b).start()
