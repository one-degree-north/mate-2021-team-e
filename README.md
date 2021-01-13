Robot Control - C++
Microcontroller - Arduino Nano
Communciation Systems -  
Interface - Python Library


UML

Class: Robot Control
Methods:
- Move forward and backward

Description: Moves the robot forward and backward while taking in the joystick for forward and backward movement. When the joystick is moved up, the robot moves forward, and when the joystick is moved backward, the robot moves backward depending on the amount of time the key is pressed for.
- Move up and down
Description: Moves the robot up and down through the use of the k and l keys. When the k key is pressed, the robot moves up, and when the l key is pressed, the robot moves down depending on the amount of time the key is pressed for.
- Move left and right
Description: Moves the robot left and right through the use of the 
- Rotate or turn left or right
- ClawMovement
Description: Moves the claw up and down or left and right based on which of the four buttons (Y for down, X for left, A for up, B for down). The left and right arrow buttons move the robot claw to close and open together.
- CameraMovement
Description: 

Class: DataReceiver
Description: This class takes the input data from the robots movements from the camera and position of the robot in order to store it in a temporary database for later usage.
Methods:


