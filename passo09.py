import cv2
import os

def Processamento_e_salva(teste, saida):
    # Carregar a imagem do arquivo
    imagem = cv2.imread(teste)
    
    # Mensagem se dê erro
    if imagem is None:
        print("Erro de carregar imagem")
        return
    
    # Processar a imagem para RGB, ou seja, deixa as imagens azuís
    processamento = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    # Salvar as imagens azuís processadas 
    cv2.imwrite(saida, processamento)
    # Exibir mensagem das imagens salvas
    print("Imagem salva")

def teste_De_Imagens(test_directory, output_directory):
    # Testar cada imagem do Arquivo
    for nomeArquivo in os.listdir(test_directory):
        # Cria o caminho da imagem de entrada
        teste = os.path.join(test_directory, nomeArquivo)
        
        # Cria o caminho da imagem de saída
        saida = os.path.join(output_directory, f"processada_{nomeArquivo}")
        
        # Chama a função para processar e salvar a imagem do arquivo
        Processamento_e_salva(teste, saida)

# Arquivo de imagens onde será feito os testes
ArquivoTeste = 'imagens'  
# Diretório onde as imagens processadas serão salvas
ArquivoSalvo = 'teste Final'

# Executar o teste das imagens
teste_De_Imagens(ArquivoTeste, ArquivoSalvo)
