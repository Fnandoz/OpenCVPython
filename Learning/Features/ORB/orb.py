__author__ = 'Ueliton'
import numpy as np
import cv2
import copy
from matplotlib import pyplot as plt

img = cv2.imread('pedra.jpg',0)
img2 = cv2.imread('pedra.jpg')
# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)
print kp
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation

cv2.drawKeypoints(img, kp, img2, color=(0, 255, 0), flags=0)
plt.imshow(img2), plt.show()