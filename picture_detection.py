import cv2
import numpy as np
import imutils
from imutils import contours
def picture_lines(pictures):
    img = cv2.imread(pictures)
    picture = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

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
    return ([full_part, reds_part])
def draw_picture(picture, lines):
    picture_lines_white_red = cv2.drawContours(picture, lines[0], -1, (255,0,0), 3)
    picture_lines_red = cv2.drawContours(picture, lines[1], -1, (0,255,0), 3)
    cv2.imshow('picture_show', picture)
