__author__ = 'Ueliton'

#Diferenca entre a closing e imagem original.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)
kernel = np.ones((9, 9), np.uint8)
black = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(closing), plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(black), plt.title('BlackHat')
plt.xticks([]), plt.yticks([])

plt.show();