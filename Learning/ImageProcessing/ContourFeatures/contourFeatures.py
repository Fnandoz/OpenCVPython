import cv2
import numpy as np

img = cv2.imread('raio.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 100, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
#o segundo parametro indica se os contornos sao fechados ou se e apenas uma curva.
perimeter = cv2.arcLength(cnt, True)

epsilon = 0.01*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

# convex hull
hull = cv2.convexHull(cnt)

image = cv2.drawContours(image, hull, -1, (255, 255, 255), 3)

print M
print "Area: "+str(area)
print "Perimetro: "+str(perimeter)
print approx

cv2.imshow("Imagem aproximada", image)
cv2.waitKey()
