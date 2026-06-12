# Software Setup
This setup guide should be completed first before the hardware setup guide.

## Raspberry Pi Imager
1. Follow this link to download the Raspberry Pi Imager that is needed to start your setup for the Raspberry Pi 5: https://www.raspberrypi.com/software/ 
2. After downloading the imager, select the device as Raspberry Pi 5, operating system as the 64-bit one, and then the storage device as your micro SD card you have plugged into your computer. 
3. After you reach the next popup, click on edit settings when it asks you to apply OS customization.
4. Afterwards, you can set a username and password if you like, and then also make sure to configure wireless LAN to connect you Pi to your house wifi.
5. Hit save and then write for it to write its OS onto your micro SD card.
6. After you are done, you can remove the card and plug it into your Raspberry Pi 5.

## Using the Raspberry Pi
1. After doing the OS setup, you can now use your Pi.
2. To do so, you can use an external monitor and use an HDMI cable to connect your Pi to your monitor and use it like an ordinary PC.
3. Or, you can control you Pi remotely using RPI Connect which you can find the tutorial here to use: https://www.youtube.com/watch?v=ZbadI2Vloh4, this is very well explained tutorial.

## Transferring Code and Firmware
1. After setting up the OS for the Raspberry Pi, you can download the code and firmware files from this github, which should all be under the firmware folder. 
2. Transfer the code files from your computer onto a USB drive and then plug that USB drive into one of the the Pi’s USB ports.
3. Open the Pi’s files manager and copy all of the needed code into the Pi’s “home” directory.

## Using Adafruit PCA9685 Servo Driver
1. This project requires an Adafruit PCA9685 Servo Driver which helps powers servos without having to put load onto the Raspberry Pi
2. Go to your terminal in the Raspberry Pi and type in this command: `sudo pip3 install adafruit-circuitpython-servokit`
3. If an "externally managed" error comes up, type in this command: `sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED`
4. This should download the library necessary for the code to run properly.
5. Refer to this documentation is anything is unclear: https://docs.circuitpython.org/projects/servokit/en/latest/

## Installing Libraries
1. Go to you Raspberry Pi terminal (which you should have open already from the preivous steps)
2. Install easyocr: `sudo pip3 install easyocr`
3. Install deep_translator: `sudo pip3 install deep-translator`

## Code Running Upon Power On
1. This is optional but you can run the code as soon as the Raspberry Pi is powered on, to give a more authentic feel to the project, making it seem like its a real product.
2. Open the terminal in the Raspberry Pi and then type in: `sudo crontab -e`
3. Then, type 1 if it’s asking to select an editor.
4. Type in the command: `@reboot python3 /home/pi/Desktop/main.py &`
5. The above really depends on where you put your code files so you can change it accordingly. This assumes you have it all on your Desktop but you would likely have them in the firmware folder still.

## Huge Thanks
I want to thank these YouTube videos which were an insane help to me when creating this project, they explained things so well and allowed to be get a good grasp despite being a complete beginner. 
Please refer to these videos if my explanations were unclear in any way, they are amazing.
https://www.youtube.com/watch?v=-x2EEIUMm6A 
https://www.youtube.com/watch?v=w-4V_q8XWtk 
https://www.youtube.com/watch?v=Gl9HS7-H0mI
https://www.youtube.com/watch?v=-x2EEIUMm6A
