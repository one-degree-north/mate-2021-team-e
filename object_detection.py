#import opencv-python as computer
import cv2
import numpy as np
import imutils
from imutils import contours
#part, place = videoing.read()
#black = computer.cvtColor(place, computer.COLOR_BGR2GRAY)
#computer.imshow('place', black)
img = cv2.imread("/Users/nityaarora/Downloads/picture.png")
picture = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# hsv_white = np.uint8([[[210, 13, 88]]])
# hsv_white = cv2.cvtColor(white, cv2.COLOR_BGR2HSV)

# hsv_white_white = np.uint([[[203, 15, 96]]])

hsv_dark_red = np.uint8([[[321, 45, 33]]])

hsv_light_red = np.uint8([[[330, 36, 76]]])
kernel = np.ones((5,5), np.float32)/25

picture_picture = cv2.filter2D(picture, -1, kernel)
mask_picture = cv2.inRange(picture_picture, hsv_light_red, hsv_dark_red)

picture_show = cv2.bitwise_and(picture_picture, picture_picture, mask_picture)
picture_picture_show = cv2.cvtColor(picture_show, cv2.COLOR_BGR2GRAY)

ret, red_part = cv2.threshold(picture_picture_show, 127,255,0)
ret_white, white_part = cv2.threshold(picture_picture_show, 255-160, 255, 0)
white_white_white = cv2.subtract(white_part, red_part)
full_part, hierarchy_full_part = cv2.findContours(white_white_white, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
reds_part, hierarchy_red_part = cv2.findContours(red_part, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

picture_lines_white_red = cv2.drawContours(picture, full_part, -1, (255,0,0), 3)
picture_lines_red = cv2.drawContours(picture, reds_part, -1, (0,255,0), 3)
cv2.imshow('picture_show', picture)
cv2.waitKey(100000000)
cv2.destroyAllWindows()






































































