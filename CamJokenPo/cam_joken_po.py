__author__ = 'Ueliton'
import numpy as np
import cv2

"""
Joken po com a camera

"""
#Camera
cap = cv2.VideoCapture(0)

# cv2.namedWindow('frame1')
# cv2.namedWindow('frame2')
min = 0
max = 400

MIN_H = 28
MAX_H = 154

MIN_S = 59
MAX_S = 149

MIN_V = 139
MAX_V = 89

#63, 47, 91

#91, 41, 89

min_amarelo = np.array([MIN_H,MIN_S,MIN_V])
max_amarelo = np.array([MAX_H,MAX_S,MAX_V])

cannyMin = min
cannyMax = min

#Eventos das barras.
#Estas funcoes sao chamadas todas as vezes que um valor muda na barra.
def cannyTreshouldMin(value):
    global cannyMin
    cannyMin = value

def cannyTreshouldMax(value):
    global cannyMax
    cannyMax = value


while(True):
    # frame-By-Frame
    ret, frame = cap.read()

    # Operacores com os frames
    #Imagem em preto e branco
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #remove ruidos com a gaussiana
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    #aplica um trasehold...esta invertido para ser utilizado no escuro para remover o fundo com facilidade
    ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    segmentada = cv2.inRange(hsv, min_amarelo, max_amarelo)

    #encontra os contornos da mao.
    ret, contours, hierarchy = cv2.findContours(segmentada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #encontra o contorno de maior area
    max_area = 0.0
    for i in range(len(contours)):

            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area > max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    #desenha os contornos
    hull = cv2.convexHull(cnt)
    epsilon = 0.01*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    drawing = np.zeros(frame.shape, np.uint8)

    cv2.drawContours(drawing,[cnt], 0, (0, 255, 0), 2)
    cv2.drawContours(drawing,[hull], 0, (0, 0, 255), 2)

    print hull.shape

    cv2.imshow("HSV", hsv)
    cv2.imshow("Original", frame)
    cv2.imshow('Result', drawing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
