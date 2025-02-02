"""
(I) Transformando imagens em sketchs (esboço)

import cv2

imagem = cv2.imread("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\logo .jpg")
# Converter para escala de cinza
imagem_sketch = cv2.cvtColor(imagem,  cv2.COLOR_BGR2GRAY)
print(type(imagem_sketch))
print(imagem_sketch)
# Aplicar um desfoque para suavizar
esboco = cv2.GaussianBlur(255-imagem_sketch,(31,31),0)# 
print(esboco)
print(type(esboco))
pincel = cv2.divide(imagem_sketch,255-esboco,scale=300.0) # Scale altera a tonalidade de preto e branco

cv2.imwrite('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\foto.png', pincel)

(II) Reconhecimento facial de carro e pedestre/ pip3 install opencv-python

1-Carros:
- import cv2
- import imutils

import cv2
import imutils

arquivo_reconhecimento = cv2.CascadeClassifier('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\cars.xml')

figura = cv2.imread('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\Carros.jpg')
figura = imutils.resize(figura,width=min(400,figura.shape[1]))

dimensoes = arquivo_reconhecimento.detectMultiScale(figura)

for (x,y,w,h) in dimensoes:
    cv2.rectangle(figura,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2_imshow('Deteccao',figura)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""



