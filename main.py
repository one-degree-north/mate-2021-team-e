import pygame
import serial
import sympy
import numpy
import matplotlib
import PySimpleGUI as sg
from threading import Thread
import time
from camera import Camera
from interface import Interface
from controls import Control

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
    interface = Interface(robot=camera.list_movements, object_seen=True, motor_controls=True)
    controller = Control(100,0.1)
    interface.make_interface() 
    try:
        controller.controls_move()
        print("Controller is working")
    except KeyboardInterrupt:
        print("Stop")
    except:
        print("Unexpected error: ", sys.exc_infor()[0])
        raise
    if not camera.video_capture.isOpened():
        print("Start Cameras")
        SystemExit(0)
    while self.running:
        _, camera_picture = camera.read()
        camera_pictures = np.hstack((camera_picture))
        thread = Thread(target=update_interface, args=(cameraFrameSize=(600,600), videoFrames=camera_pictures,))
        thread.start()
        camera.stop()
        camera.release()
    
    
    
    
