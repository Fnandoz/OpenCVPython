__author__ = 'Ueliton'
#Diferentes tipos de kernel
#Eliptcos, circulares..etc.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)

recKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print recKernel
recKernel = cv2.morphologyEx(img, cv2.MORPH_RECT, recKernel)

elipticalKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print elipticalKernel
elipticalKernel = cv2.morphologyEx(img, cv2.MORPH_ELLIPSE, elipticalKernel)

crossShapedKernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print crossShapedKernel
crossShapedKernel = cv2.morphologyEx(img, cv2.MORPH_CROSS, crossShapedKernel)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(recKernel), plt.title('Rectangle')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(elipticalKernel), plt.title('Eliptical')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(crossShapedKernel), plt.title('Cross')
plt.xticks([]), plt.yticks([])

plt.show();
