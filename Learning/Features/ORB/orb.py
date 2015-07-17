__author__ = 'Ueliton'
import numpy as np
import cv2
import copy
from matplotlib import pyplot as plt

MIN_H = 39
MAX_H = 116

MIN_S = 0
MAX_S = 240

MIN_V = 255
MAX_V = 255

#63, 47, 91

#91, 41, 89

min_amarelo = np.array([MIN_H,MIN_S,MIN_V])
max_amarelo = np.array([MAX_H,MAX_S,MAX_V])

cam = cv2.VideoCapture(0)
orb = cv2.ORB_create()

# bag of words
bovw = cv2.BOWKMeansTrainer(32)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)

bovwIDE = cv2.BOWImgDescriptorExtractor(orb, flann)

print "Treinamento"

frame = cv2.imread("messi.jpg")

while(True):
    #frame
    _, frame = cam.read(cv2.CV_32F)
    image = copy.deepcopy(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = np.float32(gray)
    print frame.dtype, frame.ndim, gray.dtype, gray.ndim

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    #aplica um trasehold...esta invertido para ser utilizado no escuro para remover o fundo com facilidade
    # _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # segmentada = cv2.inRange(hsv, min_amarelo, max_amarelo)
    # cv2.imshow('Tresh', segmentada)

    kp = orb.detect(gray, None)

    kp, des = orb.compute(gray, kp)
    #A covnersao e necessaria para a clusterizacao
    des = np.float32(des)
    bovw.add(des)

    cv2.drawKeypoints(image, kp, image, color=(0, 255, 0), flags= 0)

    cv2.imshow("frame", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print "Clusterizando"
vocabulary = bovw.cluster()
print "Vocabulario criado"

bovwIDE.setVocabulary(vocabulary)

while(True):
    #frame
    _, frame = cam.read()
    image = copy.deepcopy(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = np.float32(gray)

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    #aplica um trasehold...esta invertido para ser utilizado no escuro para remover o fundo com facilidade
    # _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # segmentada = cv2.inRange(hsv, min_amarelo, max_amarelo)
    # cv2.imshow('Tresh', segmentada)

    kp = orb.detect(gray, None)
    #A covnersao e necessaria para a clusterizacao
    kp, des = orb.compute(gray, kp)
    #A covnersao e necessaria para a clusterizacao
    des = np.float32(des)

    a = bovwIDE.compute(frame, kp)

    cv2.drawKeypoints(image, kp, image, color=(0, 255, 0), flags= 0)

    cv2.imshow("frame", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# img = cv2.imread('pedra.jpg',0)
# img2 = cv2.imread('pedra.jpg')
# # Initiate STAR detector
# orb = cv2.ORB_create()
#
# # find the keypoints with ORB
# kp = orb.detect(img, None)
# print kp
# # compute the descriptors with ORB
# kp, des = orb.compute(img, kp)
#
# # draw only keypoints location,not size and orientation
#
# cv2.drawKeypoints(img, kp, img2, color=(0, 255, 0), flags=0)
# plt.imshow(img2), plt.show()