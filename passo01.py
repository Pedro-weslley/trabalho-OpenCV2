import cv2

# exibir as imagens em nas formas JPEG, PNG, BMP
jpg = cv2.imread("imagens/leao.jpg")
jpeg = cv2.imread("imagens/leao copy.jpeg")
png = cv2.imread("imagens/leao copy.png")
 
# correção de imagem
if jpg is None:
    print("Erro a imagem.")
else:
    cv2.imshow('jpg',jpg)
    cv2.imshow('jpeg',jpeg)
    cv2.imshow('png',png)

# tecla q
    cv2.waitKey(0)
    cv2.destroyAllWindows()
