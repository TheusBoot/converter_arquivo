from PIL import Image
import os

def converter_para_png(caminho_pasta):
    # Lista todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    # Filtra apenas os arquivos de imagem (por extensão)
    arquivos_imagem = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.ppm', '.pgm'))]

    # Cria um diretório para armazenar as imagens convertidas, se não existir
    pasta_saida = os.path.join(caminho_pasta, "imagens_convertidas")
    os.makedirs(pasta_saida, exist_ok=True)

    # Converte as imagens para PNG e salva na nova pasta
    for arquivo in arquivos_imagem:
        caminho_entrada = os.path.join(caminho_pasta, arquivo)
        nome_saida = os.path.splitext(arquivo)[0] + ".png"
        caminho_saida = os.path.join(pasta_saida, nome_saida)

        imagem = Image.open(caminho_entrada)
        imagem.save(caminho_saida, "PNG")

        print(f"Convertido: {caminho_entrada} -> {caminho_saida}")

# Substitua 'caminho_da_sua_pasta' pelo caminho da pasta que contém as imagens
caminho_da_sua_pasta = os.path.dirname(os.path.abspath(__file__))

converter_para_png(caminho_da_sua_pasta)
