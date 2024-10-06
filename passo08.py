import cv2

# Carregar a imagem 
imagem = cv2.imread('imagens/leao.jpg')

# Usa uma função simples para processar a imagem( deixa a imagem cinza)
processamento = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Salvar a imagem que foi processada no arquivo SalvaImagem!
cv2.imwrite('SalvaImagem/leao.jpg', processamento)

# exibir mensagem de sucesso
print("Imagem salva com sucesso!")
