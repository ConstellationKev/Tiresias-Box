from gpiozero import Button
import time
import camera
import servos

button = Button(5) #pin 5 but could change
servos.initial_pos()

english = True
status = True #true for on
pressed = False
photo_taken = False
start_time = time.time()
duration = 0
wait = 3
letters = []

while status:
    if button.is_pressed and not pressed and not photo_taken:
        pressed = True
        start_time = time.time()
    elif not button.is_pressed and pressed and not photo_taken:
        pressed = False
        duration = time.time() - start_time
        if duration >= 6:
            status = False
        elif duration >= 3:
            english = not english
            time.sleep(1)
        else:
            camera.take_photo()
            photo_taken = True

    if photo_taken:
        if english:
            letters = camera.analyze_photo()
        else:
            letters = camera.analyze_chinese_photo()
        if letters != []:
            for i in range(len(letters)):
                servos.move_to_letter(letters[i].lower())
                time.sleep(wait)
            letters = []
        photo_taken = False

camera.stop_camera()
servos.off()
