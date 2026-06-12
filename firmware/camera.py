from picamera2 import Picamera2 #exclusive to raspberry pi OS so I can't import properly in vscode
from libcamera import controls #exclusive to rpi 5 as well
from deep_translator import GoogleTranslator
import easyocr
import time
import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

camera = Picamera2()
reader = easyocr.Reader(["ch_sim", "en"], gpu=False, quantize=True) # may not be good for RAM to make 2 readers so we combine to one model

camera_config = camera.create_still_configuration()
camera.configure(camera_config)
camera.options["quality"] = 95

camera.start()
time.sleep(2)
camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

#takes photo based on button press
def take_photo():
    img_path = "/home/pi/photo.jpg"
    camera.capture_file(img_path)

#returns array of letters
def analyze_photo():
    try:
        letters = [] #no spaces
        results = reader.readtext("/home/pi/photo.jpg", detail = 0, paragraph = True)
        for letter in results[0]:
            char = letter.lower()
            if char != " " and ((char in alphabet) or (char in numbers)): # okay maybe I don't need char != " " but just keep it there for sanity
                letters.append(char)
        os.remove("/home/pi/photo.jpg")
        return letters
    except:
        print("You probably have not taken a photo yet")
        return []

def analyze_chinese_photo():
    try:
        letters = [] #no spaces
        results = reader.readtext("/home/pi/photo.jpg", detail = 0, paragraph = True)
        translated = GoogleTranslator(source='chinese (simplified)', target='english').translate(results[0])
        for letter in translated:
            char = letter.lower()
            if char != " " and ((char in alphabet) or (char in numbers)): # okay maybe I don't need char != " " but just keep it there for sanity
                letters.append(char)
        os.remove("/home/pi/photo.jpg")
        return letters
    except:
        print("You probably have not taken a photo yet")
        return []

def stop_camera():
    camera.stop()

def start_camera(): #camera usually already started but just in case yk
    camera.start()
    time.sleep(2)