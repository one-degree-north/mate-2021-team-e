import pygame
import serial
pygame.init()
background_color = (0,0,0)
width = 300
height = 300
screen  = pygame.display.set_mode((width,height))
screen.fill(background_color)
running = True
ser = serial.begin("dev/cu.usbserial-1420", 9600)
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False
       if event.type == pygame.KEYUP:
          ser.write("1")
          ser.write("500")
       if event.type == pygame.KEYDOWN:
          ser.write("2")
          ser.write("500")
       if event.type == pygame.K_LEFT:
          ser.write("3")
          ser.write("500")
       if event.type == pygame.K_RIGHT:
          ser.write("4")
          ser.write("100")
       if event.type == pygame.K_w:
          ser.write("5")
          ser.write("100")
