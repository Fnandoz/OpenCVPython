__author__ = 'Ueliton'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise.jpg')

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(331), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(332), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(333), plt.imshow(blur), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(334), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(335), plt.imshow(bilateral), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()