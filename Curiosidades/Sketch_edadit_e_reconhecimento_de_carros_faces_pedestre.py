"""
Transformando imagens em sketchs (esboço)

import cv2

imagem = cv2.imread("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\logo .jpg")
# Converter para escala de cinza
imagem_sketch = cv2.cvtColor(imagem,  cv2.COLOR_BGR2GRAY)
print(type(imagem_sketch))
print(imagem_sketch)
# Aplicar um desfoque para suavizar
esboco = cv2.GaussianBlur(255-imagem_sketch,(31,31),0)
print(esboco)
print(type(esboco))
pincel = cv2.divide(imagem_sketch,255-esboco,scale=300.0)

cv2.imwrite('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\foto.png', pincel)


"""


