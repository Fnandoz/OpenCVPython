import cv2

__author__ = 'Ueliton'

import bovw

if __name__ == '__main__':
    """Executa o BOVW em uma camera"""

    #Camera
    camera = cv2.VideoCapture(0)
    bovw = bovw.BOVW()

    while True:
        #Lê uma imagem
        _, imagem = camera.read()

        bovw.adiciona_e_detecta_pontos_de_interesse_de_uma_imagem(imagem)
        bovw.desenha_pontos_de_interesse_nas_imagens_coloridas()
        imagem = bovw.ultima_imagem_BRG_adicionada()

        cv2.imshow("Imagem", imagem)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



