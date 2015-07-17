#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ueliton'
import cv2

import bovw

if __name__ == '__main__':
    """Executa o BOVW em uma camera"""

    #Camera
    camera = cv2.VideoCapture(0)
    bovw = bovw.BOVW(extrator=bovw.BOVW_EXTRATOR.SIFT)

    while True:
        #Lê uma imagem
        _, imagem = camera.read()

        bovw.adiciona_uma_imagem_e_detecta_descreve_pontos_de_interesses(imagem)
        bovw.desenha_pontos_de_interesse_nas_imagens_coloridas()

        imagem = bovw.ultima_imagem_BRG_adicionada()

        cv2.imshow("Imagem", imagem)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print "Clusterizand..."
bovw.cria_vetor_de_atributos_das_imagens()
bovw.cria_vocabulario()
print "Vocabulario Criado"

