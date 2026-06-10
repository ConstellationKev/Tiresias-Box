from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# setting servos to 0 position to attach the gears; tune these values later depending on the gears
kit.servo[0].angle = 0 #inner
kit.servo[3].angle = 0 #outer