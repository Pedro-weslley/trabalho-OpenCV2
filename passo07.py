import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('imagens/leao.jpg')

# carregando a imagem para cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# deixa desfocado
desfoque = cv2.GaussianBlur(cinza, (5, 5), 0)

# Binarizar a imagem
_, Binarizar = cv2.threshold(desfoque, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Encontrar contornos para pode criar marcadores
contornos, _ = cv2.findContours(Binarizar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
Marcadores = np.zeros_like(cinza, dtype=np.int32)

# Preencher marcadores
for i, contour in enumerate(contornos):
    cv2.drawContours(Marcadores, [contour], -1, (i + 1), -1)

# Aplicar o algoritmo Watershed
Marcadores = cv2.watershed(imagem,Marcadores)

# Marcar os limites em vermelho na imagem
imagem[Marcadores == -1] = [0, 0, 255]  

# Exibir resultados das imagens
cv2.imshow('imagem Segmentacao', imagem)

# tecla q 
cv2.waitKey(0)
cv2.destroyAllWindows()
