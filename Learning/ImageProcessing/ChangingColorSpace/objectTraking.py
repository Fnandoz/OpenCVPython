__author__ = 'Ueliton'

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
color = [[[201, 171, 161]]]
color = np.uint8(color);
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
print hsv_color

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([133, 28, 174])
    upper_blue = np.array([170, 102, 242])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()