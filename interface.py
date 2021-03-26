import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
import time
from threading import Thread
import matplotlib.animation as animation
from functions import interfaceInformation
matplotlib.use("TkAgg")
class Interface():
    
    def __init__(self, robot, object_seen, motor_controls, clock):
        self.clock = clock
        self.graphs_figure = figure(num = 0, figsize = (12, 8))
        self.graphs_figure.suptitle("Graphs", fontsize=12)
        self.robot = robot
        self.object_seen = object_seen
        self.motor_controls = motor_controls
        self.graph_angular_position = plt.figure()
        self.graph_speed = plt.figure()
        self.graph_position = plt.figure()
        self.graph_angular_velocity = plt.figure()
        self.graph_acceleration = plt.figure() 
        self.graph_power = plt.figure()
        self.graphs = [self.angular_position, self.graph_speed, self.graph_position, self.graph_angular_velocity, self.graph_acceleration, self.graph_power]
        self.information = interfaceInformation(self.clock)
        
        # Setup figure and subplots
    def graphs_setup(self):
        graph_angular_position_ax = subplot2grid((2, 2), (0, 0))
        graph_speed_ax = subplot2grid((2, 2), (0, 1))
        graph_power_ax = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
        

        # Set titles of subplots
        graph_angular_position_ax.set_title('Angular Position vs Time')
        graph_speed_ax.set_title('Velocity vs Time')
        graph_power_ax.set_title('Power vs Time')

        # set y-limits
        graph_angular_position_ax.set_ylim(0,2)
        graph_speed_ax.set_ylim(-6,6)
        graph_power_ax.set_ylim(-0,5)

        graph_angular_position_ax.set_xlim(0,5.0)
        graph_speed_ax.set_xlim(0,5.0)
        graph_power_ax.set_xlim(0,5.0)

        # Turn on grids
        graph_angular_position_ax.grid(True)
        graph_speed_ax.grid(True)
        graph_power_ax.grid(True)

        # set label names
        graph_angular_position_ax.set_xlabel("Time")
        graph_angular_position_ax.set_ylabel("Angular Position")
        graph_speed_ax.set_xlabel("Time")
        graph_speed_ax.set_ylabel("Velocity")
        graph_power_ax.set_xlabel("Time")
        graph_power_ax.set_ylabel("Power")

        # Data Placeholders
        angular_position=zeros(0)
        velocity=zeros(0)
        power=zeros(0)
        t=zeros(0)
        
        p011, = graph_angular_position_ax.plot(t,angular_position,'b-', label="Angular Position")
        

        p021, = graph_speed_ax.plot(t,velocity,'b-', label="Velocity")
        

        p031, = graph_power_ax.plot(t,power,'b-', label="Power")
        


    
    #make_interface makes the user interface that will use information parsed through from the camera 
    #and the controls in order to make information about the robot's speed, acceleration, and other measurements available
    def make_interface(self):
        self.camera_layout = [[sg.Text(title="Camera", size=(60,60), justification="center")], [sg.Image(filename="", key="camera")]]
        self.camera_column = sg.Column(camera_layout, element_justification="center")
        self.speed_graph_layout = [[sg.Text("Graphs", size=(60,60), justification="center")], [sg.Canvas(key="Canvas")]]
        self.layout = [camera_layout, speed_graph_layout]
        self.window = sg.Window(title="Interface", layout=layout, return_keyboard_events=True,location=(600,600))
    i = 0
    minimum_i = 0
    maximum_i = 10
    def graph_update(self):
        
        global angular_position
        global velocity
        global power
        global t
        
        angular_position = angular_positon.append(self.information.angular_position_changer(angular_position_arrays[1]))
        velocity = velocity.append(self.information.speeds_estimates())
        left_power = self.robot["left_motor"]
        right_power = self.robot["right_motor"]
        up_power = self.robot["up_motor"]
        magnitude = math.sqrt((left_power**2)+(right_motor)**2 + (up_motor**2))
        power = power.append(magnitude)
        
        p011.set_data(t, angular_position)
        p021.set_data(t, velocity)
        p031.set_data(t, power)
        
        return p011,p021,p031
        
        
        
    #update_interface puts the incoming pictures on the interface to show video output    
    def update_interface(self, cameraFrameSize, graphFrameSize, videoFrames):
        self.running = True
        self.cameraFrameSize = cameraFrameSize
        self.graphFrameSize = graphFrameSize  
        graphs_setup()
        while self.running:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "EXIT":
                self.running = False

                
            frame = cv2.resize(videoFrames, self.graphFrameSize)
            frame_grayversion = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            images_bytess = cv2.imencode(".png", frame_grayversion)[1].tobytes()
            window["camera"].update(data=images_bytess)
            window["Canvas"] = animation.FuncAnimation(self.graphs_figure, graph_update, blit=False, frames=200, interval=60, repeat=False)
            plt.show()
            #The two lines above this don't work but I'll try to figure out how to update the canvas continuously
            
            

            
