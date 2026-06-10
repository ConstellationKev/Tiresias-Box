import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#start positions, tune later
cur_pos_inner = 0 #servo port 0, inner
cur_pos_outer = 0 #servo port 3, outer

inner_servo_positions = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
}

outer_servo_positions = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
}

def move_to_letter(letter):
    position(0, inner_servo_positions[letter], 0.02)
    position(3, outer_servo_positions[letter], 0.02)

#gradually moves servo
def position(servo_num, end_pos, delay):
    start_pos = 0
    if servo_num == 0: 
        start_pos = cur_pos_inner
    elif servo_num == 3: 
        start_pos = cur_pos_outer

    step = -1
    if start_pos < end_pos:
        step = 1

    #may need to change delay later on
    for pos in range(start_pos, end_pos+step, step):
        kit.servo[servo_num].angle = pos
        time.sleep(delay)

    if servo_num == 0: 
        cur_pos_inner = end_pos
    elif servo_num == 3: 
        cur_pos_outer = end_pos

#should run this first
def initial_pos():
    kit.servo[0].angle = cur_pos_inner
    kit.servo[3].angle = cur_pos_outer