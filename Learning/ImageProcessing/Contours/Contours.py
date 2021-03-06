__author__ = 'Ueliton'
import numpy as np
import cv2

im = cv2.imread('c.png')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
imagesd = cv2.drawContours(image, contours, -1, (255,255,255), 3)

cv2.imshow("Contornos", image)
cv2.waitKey()