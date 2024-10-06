import cv2

# carregar a imagem 
imagem = cv2.imread("imagens/leao.jpg")

# correção de imagem
if imagem is None:
    print("Erro a imagem.")
else:
    # converter a imagem em cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # converter a imagem em Azul
    azul = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # converter a imagem em hsv
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # converter em lad
    lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2Lab)

    # converter a imagem para redimensionada
    redimensionada = cv2.resize(imagem, (200, 200))

    # converter a imagem em equalizada
    equalizada = cv2.equalizeHist(cinza)

    # exibir resultados das imagens
    cv2.imshow('Imagem em Cinza', cinza)
    cv2.imshow('Imagem redimensionada', redimensionada)
    cv2.imshow('Imagem equalizada', equalizada)
    cv2.imshow('imagem em azul', azul)
    cv2.imshow('Imagem em hsv', hsv)
    cv2.imshow('Image, em lab', lab)

   #tecla q 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
