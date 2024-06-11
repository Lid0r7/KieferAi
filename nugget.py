#import playsound
import random
import pvporcupine
from pvrecorder import PvRecorder
import time
import pvrhino
import openai
import keyboard
import pyttsx3
import numpy as np
import cv2
import pyautogui
import pyaudio
#API_KEY = open("API_KEY", "r").read()
#openai.api_key = API_KEY
#response = openai.ChatCompletion(
#    model="gpt-3.5-turbo",
#    message=[
#      {"role": "user", "content": "What is the difference between Celsius and Fahrenheit?"},
#        {}
#    ]
#)
#print(response)
#engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#print (rate)
#engine.setProperty('rate', 150)
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
#pyttsx3.speak("I will speak this text")
#engine.say("Hello World!")
#engine.say('My current speaking rate is ' + str(rate))
#engine.runAndWait()
#engine.stop()
cam = cv2.VideoCapture(0)
access_key = "9/NHUwfjvLqQ2cG6m8dJ6MK7E6IsPmIR51B9uhk4WDlCKAvOAx8kGA=="
porcupine = pvporcupine.create(
    access_key=access_key,
    keywords=['picovoice', 'nugget', "Скриншот"],
    keyword_paths=['Nuggeter\\nugget_en_windows_v3_0_0.ppn'])
#rhino = pvrhino.create(
#    access_key='9/NHUwfjvLqQ2cG6m8dJ6MK7E6IsPmIR51B9uhk4WDlCKAvOAx8kGA==',
#    context_path='Nuggeter\\Nugget.yml')
recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
recorder.start()
print('Using device: %s' % recorder.selected_device)
while True:
    ret, frame = cam.read()
    if cv2.waitKey(1) == ord('q'):
        break
    pcm = recorder.read()
    is_finalized = porcupine.process(pcm)
    if is_finalized == 0:
        try:
            image = pyautogui.screenshot()
            image1 = pyautogui.screenshot("Image.png")
            s = "s.png"
            cv2.imwrite(s, frame)
        finally:
            print("Screenshot was taken")
#\keyword_index = porcupine.process(pcm)w
#if keyword_index == 0:
#while t != 15:
#t = time.time()
# #if keyword_index == 1:
#print("L")



# take screenshot using pyautogui

# this will return the image as PIL and
# store in `image`

# if you need to save the image as a
# file, pass the path of the file as
# an argument like this
