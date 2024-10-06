import cv2
import numpy as  np

# carregar a imagem
imagem = cv2.imread("imagens/leao.jpg")

#correção de imagem 
if imagem is None:
    print("Erro a imagem.")
else:
    #convertendo em cinza para se usada nas funções  
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # filtro com a função Canny
    bordas = cv2.Canny(cinza, 100, 200)
    #filtrar a imagem para blur
    blur = cv2.GaussianBlur(imagem, (5,5), 10)
    #filtrar para Sobel
    sobel= cv2.Sobel(cinza, cv2.CV_64F, 0, 1, ksize=5) 
    
    
    cv2.imshow('imagem filtrada GaussianBlur', blur)
    cv2.imshow('imagem filtrada Canny', bordas)
    cv2.imshow('Imagem filtrada Sobel', sobel)

    #tecla q 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
