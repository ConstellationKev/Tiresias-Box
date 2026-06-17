from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# setting servos to 0 position to attach the gears; tune these values later depending on the gears
kit.servo[0].angle = 180 #inner
kit.servo[3].angle = 180 #outer

kit.servo[0].angle = None #inner
kit.servo[3].angle = None #outer