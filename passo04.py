import cv2
import numpy as np

# Carregar a imagem do Leão
imagem = cv2.imread('imagens/leao.jpg')
# converter a imaagem pra cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar cantos da imagem do Leão
cantos = cv2.cornerHarris(cinza, 2, 3, 0.04)
# Aplicar os contornos da imagem 
contornos = cv2.Canny(cinza, 100, 200)

# Dilatar a imagem para destacar os cantos
cantos = cv2.dilate(cantos, None)

# Marcar os cantos na imagem
imagem[cantos > 0.01 * cantos.max()] = [0, 0, 200]

# exibir os resultados da imagem! 
cv2.imshow('Cantos detectados', imagem)
cv2.imshow('contornos detectados', contornos)

# tecla q
cv2.waitKey(0)
cv2.destroyAllWindows()
