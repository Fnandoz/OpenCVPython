__author__ = 'Ueliton'
import cv2
import numpy as np

img = cv2.imread("raio.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

#retangulo sem rotacao
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#retangulo de area minima
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

#circulo de area minima
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (255, 0, 0), 2)

#elipse com rotacao
#ele tambem da a orientacao do objeto. Eixo maior e menor.
ellipse = cv2.fitEllipse(cnt)
print "(x,y),(MA,ma),angle: "+str(ellipse)
img = cv2.ellipse(img, ellipse, (255, 255, 0), 2)

#linha
rows,cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 255), 2)

mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
print "Pontos do objeto: "+str(pixelpoints)

#pontos extremos do objeto
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

cv2.imshow("Contornos", img)
cv2.waitKey()