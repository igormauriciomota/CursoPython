"""
Transformando imagens em sketchs (esboço)


import cv2

# Carregar a imagem
imagem = cv2.imread("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\logo.jpg")

if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    # Converter para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Inverter a imagem (efeito negativo)
    imagem_invertida = cv2.bitwise_not(imagem_cinza)

    # Aplicar um desfoque para suavizar
    imagem_suavizada = cv2.GaussianBlur(imagem_invertida, (21, 21), sigmaX=0, sigmaY=0)

    # Criar o efeito de sketch
    imagem_sketch = cv2.divide(imagem_cinza, 255 - imagem_suavizada, scale=256)

    # Mostrar a imagem resultante
    cv2.imshow("Sketch", imagem_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
