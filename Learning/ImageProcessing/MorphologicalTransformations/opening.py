__author__ = 'Ueliton'

#Erosao seguida de dilatacao
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opening.png', 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
erosion = cv2.erode(img,kernel,iterations=-1)
dilatation = cv2.dilate(erosion, kernel,iterations=-1)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(dilatation), plt.title('Dilatation')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])

plt.show();