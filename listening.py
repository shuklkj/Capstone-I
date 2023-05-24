import cv2
from djitellopy import Tello
import cv2
import numpy as np
import concurrent.futures
import speech_recognition as sr


# Connect to drone - online (Use this code if your drone is on network )
ip1 = '192.168.86.37'
drone = Tello(ip1)

# Connect to drone - offline (Use this code if your drone is offline)

drone.connect()
print("Connected")
# Check the battery level
print(f"Current battery level: {drone.get_battery()}%")

# Start streaming 
drone.streamon()
print("Start streaming")

# Create recognizer 
r = sr.Recognizer()
mic = sr.Microphone()
print("Mic recognized")

drone_in_flight = False
# drone.takeoff()

while True:
    with mic as source:
        audio = r.listen(source)
        print("We got the audio") 
    try:
        command = r.recognize_google(audio).lower()
        print(command)
        if "flip" in command:
            print("Flipping")
            drone.takeoff()
            drone.flip_forward()
            drone.land()
        if "apple" in command:
            print("Dancing...")
            drone.takeoff()
            drone.move_up(50)
            drone.move_down(50)
            drone.move_up(50)
            drone.move_down(50)
            drone.land()
        if "circle" in command:
            print("Circling")
            drone.takeoff()
            drone.rotate_counter_clockwise(90)
            drone.rotate_clockwise(90)
            drone.land()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        continue
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        continue
print("We are out")