import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#start positions, tune later
cur_pos_inner = 180 #servo port 0, inner
cur_pos_outer = 180 #servo port 3, outer

inner_servo_positions = {
    "a" : 50,
    "b" : 170,
    "c" : 50,
    "d" : 110,
    "e" : 110,
    "f" : 170,
    "g" : 150,
    "h" : 150,
    "i" : 170,
    "j" : 150,
    "k" : 50,
    "l" : 170,
    "m" : 50,
    "n" : 110,
    "o" : 110,
    "p" : 170,
    "q" : 150,
    "r" : 150,
    "s" : 170,
    "t" : 150,
    "u" : 50,
    "v" : 170,
    "w" : 150,
    "x" : 50,
    "y" : 110,
    "z" : 110,
    "0" : 150, 
    "1" : 50, 
    "2" : 170, 
    "3" : 50, 
    "4" : 110, 
    "5" : 110, 
    "6" : 170, 
    "7" : 150, 
    "8" : 150, 
    "9" : 170
}

outer_servo_positions = {
    "a" : 170,
    "b" : 170,
    "c" : 75,
    "d" : 75,
    "e" : 170,
    "f" : 75,
    "g" : 75,
    "h" : 170,
    "i" : 120,
    "j" : 120,
    "k" : 162,
    "l" : 162,
    "m" : 158,
    "n" : 158,
    "o" : 162,
    "p" : 158,
    "q" : 158,
    "r" : 162,
    "s" : 90,
    "t" : 90,
    "u" : 40,
    "v" : 40,
    "w" : 110,
    "x" : 83,
    "y" : 83,
    "z" : 40,
    "0" : 120, 
    "1" : 170, 
    "2" : 170, 
    "3" : 75, 
    "4" : 75, 
    "5" : 170, 
    "6" : 75, 
    "7" : 75, 
    "8" : 170, 
    "9" : 120
}

# move to english letter and numbers only, no need to worry about translations here

def move_to_letter(letter):
    position(0, inner_servo_positions[letter], 0.005)
    position(3, outer_servo_positions[letter], 0.005)

#gradually moves servo
def position(servo_num, end_pos, delay):
    global cur_pos_inner, cur_pos_outer
    start_pos = 0
    if servo_num == 0: 
        start_pos = cur_pos_inner
    elif servo_num == 3: 
        start_pos = cur_pos_outer

    step = -1
    if start_pos < end_pos:
        step = 1

    for pos in range(start_pos, end_pos+step, step):
        kit.servo[servo_num].angle = pos
        time.sleep(delay)

    if servo_num == 0: 
        cur_pos_inner = end_pos
    elif servo_num == 3: 
        cur_pos_outer = end_pos

#should run this first
def initial_pos():
    global cur_pos_inner, cur_pos_outer
    kit.servo[0].angle = cur_pos_inner
    kit.servo[3].angle = cur_pos_outer

def off():
    kit.servo[0].angle = None
    kit.servo[3].angle = None