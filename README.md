PASSO 01:
Forma de imagem em JPEG, PNG, BMP e JPG, ou seja, em diferentes arquivos que
podemos usar uma imagem:
Ex: “imagens/leao.jpg”, “imagens/leao copy.jpeg”, “imagens/leao copy.png”
PASSO 02:
Conversão de cores: onde podemos colori a imagem em várias cores.
Imagem redimensionada: tamanho da imagem.
Imagem equalizada: colori a imagem para uma cinza mais claro.
Ex:
Conversão de cores: converter para cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
Imagem redimensionada:
redimensionada = cv2.resize(imagem, (200, 200))
Imagem equalizada:
equalizada = cv2.equalizeHist(cinza)
PASSO 03:
Imagem GaussianBlur: suaviza a imagem, reduzindo o ruído e os detalhes.
Imagem Canny: Canny é um método popular para detectar bordas em imagens.
Imagem Sobel: Sobel é utilizado para detectar bordas em uma direção específica,
horizontal ou vertical.
Ex:
Imagem Canny:
bordas = cv2.Canny(cinza, 100, 200)
Imagem GaussianBlur:
blur = cv2.GaussianBlur(imagem, (5,5), 10)
Imagem Sobel:
sobel= cv2.Sobel(cinza, cv2.CV_64F, 0, 1, ksize=5)
PASSO 04:
Cantos destacados: Para detectar cantos em uma imagem, podemos usar o método
de Harris ou o algoritmo Shi-Tomasi.
Contornos destacados: Um processo que geralmente envolve a conversão da
imagem para escala de cinza, a aplicação de um filtro de borda (como Canny), e
finalmente a detecção dos contornos.
Ex:
Cantos destacados:
cantos = cv2.cornerHarris(cinza, 2, 3, 0.04)
Contornos destacados:
cantos = cv2.dilate(cantos, None)
PASSO 05:
Rotacionamento de Imagem: Para rotacionar uma imagem usando OpenCV em
Python, você pode usar a função cv2.getRotationMatrix2D() para criar uma
matriz de rotação e cv2.warpAffine() para aplicar essa matriz à imagem.
Ex:
# centro da imagem e o ângulo de rotação
center = (w // 2, h // 2)
# ângulo em graus, a imagem pode roda 360°graus
angle = 45
# escala, como uma especíe de zoom quanto mais aumenta o zoom fica maior...
scale = 1.0
Rotacionamento = cv2.warpAffine(imagem, M, (w, h))
PASSO 05.02:
Translação da Imagem: Para realizar a translação de uma imagem usando OpenCV
em Python, você pode criar uma matriz de translação e aplicar essa matriz à
imagem com cv2.warpAffine(). A translação desloca a imagem em direções
específicas (horizontal e vertical).
Ex:
# deslocamento na horizontal
dx = 50
# deslocamento na vertical
dy = 50
translação = cv2.warpAffine(imagem, M, (imagem.shape[1], imagem.shape[0]))
PASSO 06:
Imagem Dilatação: A dilatação é uma operação morfológica que aumenta as áreas
brancas (ou os pixels com valor alto) em uma imagem.
Imagem Erosão: A erosão é uma operação morfológica que reduz as áreas brancas
(ou pixels com valor alto) em uma imagem.
Ex:
Imagem Dilatação:
# Aplicando a dilatação
dilatação = cv2.dilate(binarizando, kernel, iterations=1)
Imagem Erosão:
# Aplicando a erosão
erosao = cv2.erode(binarizando, kernel, iterations=1)
PASSO 07:
Imagem segmentação: A segmentação de imagem é um processo que consiste em
dividir uma imagem em partes significativas ou em objetos.
Ex:
# Aplicar o algoritmo Watershed
Marcadores = cv2.watershed(imagem,Marcadores)
# Marcar os limites em vermelho na imagem
imagem[Marcadores == -1] = [0, 0, 255]
PASSO 08:
Salva um imagem em um arquivo: Para salvar uma imagem em um arquivo usando
OpenCV em Python, você pode usar a função cv2.imwrite().
Ex:
# Salvar a imagem que foi processada no arquivo
cv2.imwrite('SalvaImagem/leao.jpg', processamento)
PASSO 09:
Carregar várias imagens de um diretório, aplicar algum processamento nelas e
salvar os resultados em outro diretório.
Ex:
# Arquivo de imagens onde será feito os testes
ArquivoTeste = 'imagens'
# onde as imagens processadas serão salvas
ArquivoSalvo = 'teste Final'
Teste:
def teste_De_Imagens(test_directory, output_directory):
 # Testar cada imagem do Arquivo
 for nomeArquivo in os.listdir(test_directory):
 # Cria o caminho da imagem de entrada
 teste = os.path.join(test_directory, nomeArquivo)

 # Cria o caminho da imagem de saída
 saida = os.path.join(output_directory, f"processada_{nomeArquivo}")

 # Chama a função para processar e salvar a imagem do arquivo
 Processamento_e_salva(teste, saida)
