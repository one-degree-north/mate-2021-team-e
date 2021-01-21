import pygame
from pyfirmata import Arduino
board = pyfirmata.Arduino()

it = pyfirmata.util.Iterator(board)
it.start()

#Still have to complete: Attach the arduino pins to the right joystick inputs and buttons setup, camera up and down movement


board.analog[2].mode = pyfirmata.INPUT
board.analog[3].mode = pyfirmata.INPUT
board.digital[2].mode = pyfirmata.INPUT
board.analog[8].mode = pyfirmata.OUTPUT
board.analog[9].mode = pyfirmata.OUTPUT

board.analog[13].mode = pyfirmata.OUTPUT
board.analog[12].mode = pyfirmata.OUTPUT
board.analog[7].mode = pyfirmata.OUTPUT
board.analog[14].mode = pyfirmata.OUTPUT
board.analog[0].mode = pyfirmata.INPUT
board.analog[1].mode = pyfirmata.INPUT
clock = pygame.time.Clock() 
keepPlaying = True
pygame.init()
joysticks = []
buttons = []
pygame.joystick.init()
for i in range(0, pygame.joysticks.get_count()):
  joysticks.append(pygame.joystick.Joystick(i))
  joysticks[-1].init()
for i in range(0, pygame.buttons.get_count()):
  buttons.append(pygame.button.Button(i))
  buttons[-1].init()
def readpins(pin0, pin1):
  positioninitial = pin0.read()
  positionlast = pin1.read()
  return positioninitial, positionlast
    
while keepPlaying:
  scale_value = 0
  j = pygame.joystick.Joystick(0)
  for event in pygame.event.get():
    if(event == pygame.JOYAXISMOTION):
      if(j.get_joy()==0):
        axisinitial, axislast = readpins(board.analog[2], board.analog[3])#Moves the robot backward or forward
        board.analog[8].write(axisinitial/2)
        board.analog[9].write(axislast/2)
      elif(j.get_joy()==1): # Moves the robot left or write
        board.analog[14].write(board.analog[0].read()*scale_value)
        board.analog[14].write(board.analog[1].read()*scale_value)
    if(event == pygame.JOYBUTTONDOWN):
      if(j.get_button() == 0): #Move the claw up
        board.analog[13].write(board.digital[2].read()*scale_value)
      elif(j.get_button()==1): #Move the claw right
        board.analog[12].write(board.digital[2].read()*scale_value)
      elif(j.get_button()==4):#Move the claw down
        board.analog[13].write(-1*board.digital[2].read()*scale_value)
      elif(j.get_button()==5):#Move the claw other 
        board.analog[12].write(-1*board.digital[2].read()*scale_value)
      elif(j.get_button()==2): #Open the claw
        board.analog[7].write(180)
      elif(j.get_button()==3): #Close the claw
        board.analog[7].write(0)
    if(event == pygame.JOYBUTTONUP):
      board.analog[13].write(0)
      if(j.get_button() == 0): 
        board.analog[13].write(0)
      elif(j.get_button()==1):
        board.analog[12].write(0)
    
    if(event == pygame.QUIT):
      keepPlaying = False
      pygame.quit()
'''
      


        



      
        
        































































