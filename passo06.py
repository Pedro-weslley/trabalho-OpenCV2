import cv2
import numpy as np

# Carregar a imagem para cinza
cinza = cv2.imread('imagens/leao.jpg', cv2.IMREAD_GRAYSCALE)

# binarizar a imagem
_, binarizando = cv2.threshold(cinza, 128, 255, cv2.THRESH_BINARY)

# Definir o elemento estruturante 
kernel = np.ones((5, 5), np.uint8)

# Aplicando a dilatação
dilatação = cv2.dilate(binarizando, kernel, iterations=1)
# Aplicando a erosão
erosao = cv2.erode(binarizando, kernel, iterations=1)

# Exibir as imagens
cv2.imshow('imagem Dilatacao', dilatação)
cv2.imshow('imagem Erosao', erosao)

# tecla q 
cv2.waitKey(0)
cv2.destroyAllWindows()
