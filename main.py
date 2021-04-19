import pygame
import serial
import threading
import time

DIMENSIONS: (int, int) = (800, 600)
BACKGROUND: (int, int, int) = (0, 0, 0)

pygame.init()
pygame.joystick.init()

screen = pygame.display.set_mode(DIMENSIONS)
screen.fill(BACKGROUND)

active = True

PORT_NAME = "/dev/ttyUSB0"
BAUD_RATE = 115200

controller = pygame.joystick.Joystick(0)

ser = serial.Serial(port=PORT_NAME, baudrate=BAUD_RATE)
ser.close()
ser.open()

def read_serial(ser):
    while True: 
        print(ser.read_line())
        time.sleep(0.01)

t = threading.Thread(target=read_serial, args=(ser))
t.start()

def write_msg(msg):
    ser.write(msg.encode("latin"))

def move_forward(val):
    msg1 = "1\n" + str(val) + "\n"
    msg2 = "3\n" + str(val) + "\n"
    print(msg1, end="")
    print(msg2, end="")
    write_msg(msg1)
    write_msg(msg2)

def turn_left(val):
    msg = "3\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def turn_right(val):
    msg = "1\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def move_up(val):
    msg = "2\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def right_push(val):
    msg = "3\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def left_push(val):
    msg = "1\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def claw_use(val):
    msg = "4\n" + str(val) + "\n"
    print(msg, end="")
    write_msg(msg)

def transform_val(val):
    return int(300*val)

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_forward(250)
            if event.key == pygame.K_s:
                move_forward(-250)
            if event.key == pygame.K_SPACE:
                move_up(300)
            if event.key == pygame.K_LSHIFT:
                move_up(-300)
            if event.key == pygame.K_a:
                turn_right(300)
            if event.key == pygame.K_d:
                turn_left(300)
            if event.key == pygame.K_UP:
                claw_use(180)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_forward(0)
            if event.key == pygame.K_s:
                move_forward(0)
            if event.key == pygame.K_SPACE:
                move_up(0)
            if event.key == pygame.K_LSHIFT:
                move_up(0)
            if event.key == pygame.K_a:
                turn_right(0)
            if event.key == pygame.K_d:
                turn_left(0)
            if event.key == pygame.K_UP:
                claw_use(0)
        if event.type == pygame.JOYAXISMOTION:
            # print(event)
            if event.axis == 1:
                move_up(transform_val(event.value))
            if event.axis == 2:
                if event.value > 0:
                    turn_left(transform_val(event.value))
                if event.value < 0:
                    turn_right(transform_val(event.value))
            if event.axis == 3:
                move_forward(-1 * transform_val(event.value))
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 7:
                claw_use(0)
            if event.button == 6:
                claw_use(180)
#         if event.type == pygame.JOYBUTTONUP:
#             if event.button == 7:
#                 claw_use(180)

t.join()
ser.close()
