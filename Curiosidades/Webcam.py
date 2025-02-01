"""
WebCam com Python

pode ser 0,1,2,3

import cv2

video = cv2.VideoCapture(1, cv2.CAP_DSHOW)#

while True:
    conexao,frame = video.read() # Leitura de conexao e fremes
    cv2.imshow('Imagem',frame) # Apresenta a imagem
    if cv2.waitKey(2) == ord('f'): # Clicar na letra f pra a execução da webcam
        break
    
video.release() # liberar a camera
cv2.destroyAllWindows() # limpa a memoria

"""


