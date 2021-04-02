import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
from threading import Thread
import time
import sys
from camera import Camera
from controls import Control
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def gstreamer_pipeline(sensor_id = 0,sensor_mode = 3,capture_width = 1280,capture_height = 1280,display_width = 1280,display_height = 1280,framerate = 60,flip_method = 0):
    return("nvarguscamerasrc sensor-id=%d sensor-mode=%d ! "
    "video/x-raw(memory:NVMM), "
    "width=(int)%d, height=(int)%d, "
    "format=(string)NV12, framerate=(fraction)%d/1 ! "
    "nvvidconv flip-method=%d ! "
    "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
    "videoconvert ! "
    "video/x-raw, format=(string)BGR ! appsink"
    % (
        sensor_id,
        sensor_mode,
        capture_width,
        capture_height,
        framerate,
        flip_method,
        display_width,
        display_height,
    ))

if __name__ == '__main__':
    
    camera = Camera()
    camera.open(gstreamer_pipeline(sensor_id=0, sensor_mode=3, flip_method=0, display_height=600, display_width=600))
    camera.start()
    clocks = pygame.time.Clock()
    controller = Control(100,0.1,clocks)
    #interface = Interface(robot=controller.list_movements, object_seen=True, motor_controls=True, clock=clocks)
    #interface.make_interface() 
    try:
        controller.controls_move()
        print("Controller is working")
    except KeyboardInterrupt:
        print("Stop")
    except:
        print("Unexpected error")
        raise
    if not camera.video_capture.isOpened():
        print("Start Cameras")
        SystemExit(0)
    thread = Thread(target=interface.update_interface, args=((600,600),camera_pictures))
    thread.start()
    while controller.running:
        #Put interface update here
        _, camera_picture = camera.read()
        camera_pictures = np.hstack((camera_picture))
        camera.stop()
        camera.release()
        print("Hello")
    thread.join()
