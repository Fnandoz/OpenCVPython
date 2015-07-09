__author__ = 'Ueliton'

#Diferenca entre a imagem original e a opening.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)
kernel = np.ones((9, 9), np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN , kernel)
topHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(topHat), plt.title('Top Hat')
plt.xticks([]), plt.yticks([])

plt.show();