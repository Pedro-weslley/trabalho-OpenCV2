import cv2

# Carregar a imagem
imagem = cv2.imread('imagens/leao.jpg')

# Obter as dimensões da imagem
(h, w) = imagem.shape[:2]

# centro da imagem e o ângulo de rotação
center = (w // 2, h // 2)
 # ângulo em graus, a imagem pode roda 360°graus
angle = 45 
# escala, como uma especíe de zoom quanto mais aumenta o zoom fica maior...
scale = 1.0  

# Criar a matriz de rotação da imagem
M = cv2.getRotationMatrix2D(center, angle, scale)

# Aplicando a rotação
Rotacionamento = cv2.warpAffine(imagem, M, (w, h))

# Exibir o resultado da imagem
cv2.imshow('Rotacionamento da imagem', Rotacionamento)

#tecla q
cv2.waitKey(0)
cv2.destroyAllWindows()
