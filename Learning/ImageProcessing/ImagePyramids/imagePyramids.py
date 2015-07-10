__author__ = 'Ueliton'

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg', 0)

l4 = cv2.pyrDown(img)
l8 = cv2.pyrDown(l4)
l16 = cv2.pyrDown(l8)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(l4), plt.title('l4')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(l8), plt.title('l8')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(l16), plt.title('l16')
plt.xticks([]), plt.yticks([])

plt.show()
