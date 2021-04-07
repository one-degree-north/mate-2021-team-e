import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
import time

class Control():
    #Creates variables that store the motor labels for the different motors used. Some motor values have also been put in for adjustments that may be made to add the claw          

    def __init__(self, scale, adjustment, clock, serial_port, serial_baudrate):
        self._CENTRAL_MOTOR = 1
        self._RIGHT_MOTOR = 2
        self._LEFT_MOTOR = 3
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
                    jid = joysticks[i].get_instance_id()
                except AttributeError:
                    # get_instance_id() is an SDL2 method
                    jid = joysticks[i].get_id()
                    return AttributeError
            self.controller = joysticks[0]                              

            #Sets up the timing for the interface
            self.clock = clock

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
            if raw < 0:
                return  (raw+self.adjustment)/1.0       
               
    #Correctly encodes the strings that are used to send quantities in order to send them to serial
    def printer(information):
        quantity = int(quantity*300)
        ser.write(information.encode('latin'))
        
    #Moves the robot upward by putting the central motor on higher output
    def move_up(self, quantity):
        quantity = int(quantity*300)
        msg = "" + str(self._CENTRAL_MOTOR) + "\n" + str(quantity) + "\n")
        self.printer(msg)
        
    #Moves the robot leftward by putting the left motor on higher output
    def move_left(self, quantity):
        quantity = int(quantity*300)
        msg = "" + str(self._LEFT_MOTOR) + "\n" + str(quantity) + "\n")
        self.printer(msg)
        
    #Moves the robot rightward by putting the right motor on higher output
    def move_right(self, quantity):
        quantity = int(quantity*300)
        msg = "" + str(self._RIGHT_MOTOR) +  "\n" + str(quantity) + "\n")
        self.printer(msg)
        
    #Moves the robot to the front by putting the right motor and the left motor on higher output
    def move_front(self, quantity):
        quantity = int(quantity*300)
        msg1 = "" + str(self._RIGHT_MOTOR) + "\n" + str(quantity) + "\n")
        msg2 = "" + str(self._LEFT_MOTOR) + "\n" + str(quantity) + "\n")
        self.printer(msg1)
        self.printer(msg2)
    #Turns the robot in some direction with the power output provided    
    def move_turn(self, quantity):
        quantity = int(quantity*300)
    def move_turn(self, quantity):
        quantity = int(quantity*300)
        msg1 = "" + str(self._RIGHT_MOTOR) + "\n" + str(quantity) + "\n")
        msg2 = "" + str(self._LEFT_MOTOR) + "\n" + str(-1*quantity) + "\n")
        self.printer(msg1)
        self.printer(msg2)
       

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
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        input_move = self.controller.get_axis(0)
                        amount = self.movement_scaler(input_move, 0.2)
                        if amount<0:
                            self.move_left(amount)
                            self.list_movements['left_motor_left'] += abs(amount)
                        else:
                            self.move_right(amount)
                            self.list_movements['left_motor_right'] += amount
                    if event.axis == 3:
                        input_move = self.controller.get_axis(3)
                        amount = self.movement_scaler(input_move, 0.2)
                        self.move_turn(amount)
                        self.list_movements['turning_amount'] += amount      
                    if event.axis == 4:
                        input_move = self.controller.get_axis(4)
                        amount = self.movement_scaler(input_move, 0.2)
                        self.move_up(amount)
                        self.list_movements['up_motor'] += amount
                    
            scree.fill((0,0,0))
            pygame.display.update()
    #Stops the controller by setting self.running to false                   
    def stop():
        self.running = False
        print(self.list_movements)
