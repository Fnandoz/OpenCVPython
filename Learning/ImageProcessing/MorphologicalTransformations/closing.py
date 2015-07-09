__author__ = 'Ueliton'

#Dilatacao seguida de erosao

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('closing.png', 0)
kernel = np.ones((5, 5), np.uint8)
dilatation = cv2.dilate(img, kernel, iterations=-1)
erosion = cv2.erode(dilatation, kernel, iterations=-1)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dilatation), plt.title('Dilatation')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])

plt.show();