# main.py
import modulo_reconhecimento

def main():
    # Definir a pasta com imagens conhecidas
    pasta_conhecidos = 'D:\PROJETOS\GIT\4-Cursos\DIO\Python\Processamento_imagem\reconhecimento_facial\imagens_conhecidas'
    
    # Carregar rostos conhecidos e seus nomes
    rostos_conhecidos, nomes_conhecidos = modulo_reconhecimento.carregar_rostos_conhecidos(pasta_conhecidos)
    
    # Definir o caminho da imagem onde faremos o reconhecimento
    caminho_imagem = 'D:\PROJETOS\GIT\4-Cursos\DIO\Python\Processamento_imagem\reconhecimento_facial\imagens_nomeadas.jpg'
    
    # Reconhecer rostos e nomear
    modulo_reconhecimento.reconhecer_rostos_e_nomear(caminho_imagem, rostos_conhecidos, nomes_conhecidos)

if __name__ == "__main__":
    main()
