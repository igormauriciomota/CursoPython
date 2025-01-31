"""
WebCam com Python

pode ser 0,1,2,3

import cv2

video = cv2.VideoCapture(1, cv2.CAP_DSHOW)#

while True:
    conexao,frame = video.read()
    cv2.imshow('Imagem',frame)
    if cv2.waitKey(2) == ord('f'):
        break
    
video.release()
cv2.destroyAllWindows()

"""


