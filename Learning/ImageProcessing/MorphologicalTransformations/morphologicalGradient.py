__author__ = 'Ueliton'

#Diferenca entre dilatacao e erosao.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])

plt.show();