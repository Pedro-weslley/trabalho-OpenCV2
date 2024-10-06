import cv2
import numpy as np

imagem = cv2.imread('imagens/leao.jpg')

# O dx e dy Definir os deslocamentos
# deslocamento na horizontal
dx = 50
 # deslocamento na vertical
dy = 50  

# Criar a matriz de translação da imagem
M = np.float32([[1, 0, dx], [0, 1, dy]])

# Aplicando a translação na imagem
translação = cv2.warpAffine(imagem, M, (imagem.shape[1], imagem.shape[0]))

# exibir o resultado da imagem
cv2.imshow('Translação da imagem', translação)

#tecla q
cv2.waitKey(0)
cv2.destroyAllWindows()

