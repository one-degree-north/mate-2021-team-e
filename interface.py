import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
import time
from threading import Thread
import matplotlib.animation as animation

class Interface():
    
    def __init__(self, robot, object_seen, motor_controls):
        
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
    
    #make_interface makes the user interface that will use information parsed through from the camera 
    #and the controls in order to make information about the robot's speed, acceleration, and other measurements available
    def make_interface(self):
        self.camera_layout = [[sg.Text(title="Camera", size=(60,60), justification="center")], [sg.Image(filename="", key="camera")]]
        self.camera_column = sg.Column(camera_layout, element_justification="center")
        self.speed_graph_layout = [[sg.Text("Speeds Graphs", size=(60,60), justification="center")], [sg.Image(filename="graph.png", key="graphs")]]
        self.layout = [camera_layout, speed_graph_layout]
        self.window = sg.Window(title="Interface", layout=layout, return_keyboard_events=True,location=(600,600))
    def graph_update(self, time, data, subplot):
        subplot.clear()
        subplot.plot(time,data)
    
        
    #update_interface puts the incoming pictures on the interface to show video output    
    def update_interface(self, cameraFrameSize, graphFrameSize, videoFrames):
        self.running = True
        self.cameraFrameSize = cameraFrameSize
        self.graphFrameSize = graphFrameSize
        self.angular_position = angular_position
        self.velocity = velocity
        self.acceleration = acceleration
        self.angular_velocity = angular_velocity
        self.power = power
        self.information = interfaceInformation()
        
        while self.running:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "EXIT":
                self.running = False
           
            frame = cv2.resize(videoFrames, self.graphFrameSize)
            frame_grayversion = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            images_bytess = cv2.imencode(".png", frame_grayversion)[1].tobytes()
            window["camera"].update(data=images_bytess)
            for i in range(0, len(graphs)):
                ani = animation.FuncAnimation(self.graphs[i], graph_update, interval=10000)
            plt.show()    
                #How to continuously show the graphs
            
            
