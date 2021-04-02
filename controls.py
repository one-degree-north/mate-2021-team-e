import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
import time

class Control():
    #Creates variables that store the motor labels for the different motors used. Some motor values have also been put in for adjustments that may be made to add the claw          
    _CENTRAL_MOTOR = 1
    _RIGHT_MOTOR = 2
    _LEFT_MOTOR = 3

    def __init__(self, scale, adjustment, clock):
        self.scale = scale 
        self.adjustment = adjustment
        self.running = False
        self.list_movements = {
            'abutton': 0,
            'bbutton': 0,
            'xbutton': 0,
            'ybutton': 0,
            'left_motor_right': 0,
            'up_motor' : 0,
            'right_motor_right': 0,
            'turning_amount': 0
        }
        
        #Initializes the joystick being used, which is the XBox Controller
        pygame.init()
        (width, height) = (500,500)
        scree = pygame.display.set_mode((width, height))
        joysticks = []
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("Connect Joystick")
        else:
            for i in range(joystick_count):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[i].init()
                try:
                    jid = joystick.get_instance_id()
                except AttributeError:
                    # get_instance_id() is an SDL2 method
                    jid = joystick.get_id()
                    return AttributeError
            self.controller = joysticks[0]                              

            #Sets up the timing for the interface
            self.A = self.controller.get_button(0)
            self.B = self.controller.get_button(1)
            self.X = self.controller.get_button(2)
            self.Y = self.controller.get_button(3)

            self.left_joystick = (self.movement_scaler(controller.get_axis(0)), self.movement_scaler(controller.get_axis(2)))
            self.right_joystick = (self.movement_scaler(controller.get_axis(1)), self.movement_scaler(controller.get_axis(3)))

            self.serial_port = serial_port

            self.serial_baudrate = serial_baudrate

            self.ser = serial.Serial(port=serial_port, baudrate=serial_baudrate)    
    #Function that scales the movement on the joystick of the XBox Controller to the amount that needs to be moved by the robot
    
    def movement_scaler(self, raw, adjustment):
        if abs(raw) <= self.adjustment:
            return 0
        else:
            if raw > 0:
                return (raw-self.adjustment)/1.0
            elif raw < 0:
                return  (raw+self.adjustment)/1.0       
               
    #Correctly encodes the strings that are used to send quantities in order to send them to serial
    def printer(information):
        ser.write(information.encode('latin'))
        
    #Moves the robot upward by putting the central motor on higher output
    def move_up(quantity):
        printer("" + central_motor + "\n" + quantity + "\n")
        
    #Moves the robot leftward by putting the left motor on higher output
    def move_left(quantity):
        printer("" + left_motor + "\n" + quantity + "\n")
        
    #Moves the robot rightward by putting the right motor on higher output
    def move_right(quantity):
        printer("" + right_motor +  "\n" + quantity + "\n")
        
    #Moves the robot to the front by putting the right motor and the left motor on higher output
    def move_front(quantity):
        printer("" + right_motor + "\n" + quantity + "\n")
        printer("" + left_motor + "\n" + quantity + "\n")
    #Turns the robot in some direction with the power output provided    
    def move_turn(quantity):
        printer("" + right_motor + "\n" + quantity + "\n")
        printer("" + left_motor + "\n" + -1*quantity + "\n")
       

    #Starts controls and sets up event responses to control movements on the controller
    def controls_move(self):
        self.running = True
        pygame.init()
        (width, height) = (500,500)
        scree = pygame.display.set_mode((width, height))
        while self.running:
            claw_movement = 99
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                input_move = event.value
                amount = movement_scaler(input_move, 0.2)
                elif event.type == pygame.JOYAXISMOTION:
                    input_move = event.value
                    amount = movement_scaler(input_move, 0.2)
                    if event.axis == 0:
                        if amount<0:
                            move_left(amount)
                            self.list_movement['left_motor_left'] += abs(amount)
                        else:
                            move_right(amount)
                            self.list_movement['left_motor_right'] += amount
                    elif event.axis == 3:
                        move_turn(amount)
                        self.list_movements['turning_amount'] += amount      
                    elif event.axis == 4:
                        move_up(amount)
                        self.list_movements['up_motor'] += amount
                    
            scree.fill((0,0,0))
            pygame.display.update()
    #Stops the controller by setting self.running to false                   
    def stop():
        self.running = False
        print(self.list_movements)
