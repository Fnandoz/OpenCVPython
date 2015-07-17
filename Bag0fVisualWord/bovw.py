#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Ueliton'
import cv2
from enum import Enum, unique

@unique
class BOVW_EXTRATOR(Enum):
    """Extratores de utilizados no bovw """
    SURF = 0
    SIFT = 1
    ORB = 2

class BOVW:

    def __init__(self, extrator = BOVW_EXTRATOR.SIFT, tamanho_do_dicionario=128):

        self.tamanho_do_dicionario = tamanho_do_dicionario
        self.pontos_de_interesse_das_imagens = []
        self.descritores_das_imagens = []
        self.imagens_em_tons_de_cinza = []
        self.imagens_BGR = []
        self.numero_de_imagens = 0

        #Algoritmo de clusterização baseado no KMeans
        self.bovw = cv2.BOWKMeansTrainer(tamanho_do_dicionario)

        if extrator == BOVW_EXTRATOR.SIFT:
            self.extrator = cv2.xfeatures2d.SIFT_create()

        elif extrator == BOVW_EXTRATOR.SURF:
            self.extrator = cv2.xfeatures2d.SURF_create()

        elif extrator == BOVW_EXTRATOR.ORB:
            self.extrator = cv2.ORB_create(tamanho_do_dicionario)

    def cria_vetor_de_atributos_das_imagens(self):
        """Cria o vetor de atributos que descreve as imagens"""
        self.cria_vocabulario()

    def cria_vocabulario(self):
        """Cria vocabulario"""
        self.bovw.cluster()

    def adiciona_e_detecta_pontos_de_interesse_de_uma_imagem(self, imagem):
        """Detecta os pontos de interesse de uma imagem"""
        imagem_em_tons_de_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        self.imagens_BGR.append(imagem)
        self.imagens_em_tons_de_cinza.append(imagem_em_tons_de_cinza)

        pontos_de_interesse = self.extrator.detect(imagem_em_tons_de_cinza)
        self.pontos_de_interesse_das_imagens.append(pontos_de_interesse)

        self.numero_de_imagens += 1

    def adiciona_descritor(self, descritor):
        """Adiciona o descritor da imagem"""
        self.bovw.add(descritor)

    def adiciona_uma_imagem_e_detecta_descreve_pontos_de_interesses(self, imagem):
        """Detecta e descreve os pontos de interesse de uma imagem"""
        imagem_em_tons_de_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        self.imagens_BGR.append(imagem)
        self.imagens_em_tons_de_cinza.append(imagem_em_tons_de_cinza)

        pontos_de_interesse, descritor = self.extrator.detectAndCompute(imagem_em_tons_de_cinza, None)

        self.adiciona_descritor(descritor)

        self.pontos_de_interesse_das_imagens.append(pontos_de_interesse)
        self.descritores_das_imagens.append(descritor)

        self.numero_de_imagens += 1

    def adiciona_e_detecta_pontos_de_interesse_das_imagens(self, imagens):
        """Dada uma lista de imagens, esta funçao detecta os pontos de interesse de cada imagem"""
        for imagem in imagens:
            self.adiciona_e_detecta_pontos_de_interesse_de_uma_imagem(imagem)

    def desenha_pontos_de_interesse_nas_imagens_coloridas(self):
        """Desenha pontos de interesse em cada uma das imagens coloridas"""

        for index in range(self.numero_de_imagens):
             cv2.drawKeypoints(self.imagens_BGR[index],
                               self.pontos_de_interesse_das_imagens[index],
                               self.imagens_BGR[index],
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    def desenha_pontos_de_interesse_nas_imagens_em_tons_de_cinza(self):
        """Desenha pontos de interesse em cada uma das imagens coloridas"""

        for index in range(self.numero_de_imagens):
             cv2.drawKeypoints(self.imagens_em_tons_de_cinza[index],
                               self.pontos_de_interesse_das_imagens[index],
                               self.imagens_em_tons_de_cinza[index],
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    def mostra_imagens_em_tons_de_cinza(self):
        """Imprime cada imagem adicionada ao BOVW"""

        contador = 1
        for imagem in self.imagens_em_tons_de_cinza:
            cv2.imshow("Image"+str(contador), imagem)
            contador += 1
            cv2.waitKey()

    def mostra_imagens_em_BGR(self):
        """Imprime cada imagem adicionada ao BOVW"""

        contador = 1
        for imagem in self.imagens_BGR:
            cv2.imshow("Image"+str(contador), imagem)
            contador += 1
            cv2.waitKey()

    def ultima_imagem_BRG_adicionada(self):
        return self.imagens_BGR[-1]