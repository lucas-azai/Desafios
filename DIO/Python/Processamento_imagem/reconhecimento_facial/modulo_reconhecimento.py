# modulo_reconhecimento.py
import face_recognition
import cv2
import os

def carregar_rostos_conhecidos(pasta_conhecidos):
    rostos_conhecidos = []
    nomes_conhecidos = []
    
    # Percorrer a pasta de rostos conhecidos
    for arquivo in os.listdir(pasta_conhecidos):
        caminho_imagem = os.path.join(pasta_conhecidos, arquivo)
        
        # Carregar a imagem e extrair as características do rosto
        imagem = face_recognition.load_image_file(caminho_imagem)
        encoding = face_recognition.face_encodings(imagem)
        
        if encoding:
            rostos_conhecidos.append(encoding[0])
            nome = os.path.splitext(arquivo)[0]  # O nome do arquivo (sem extensão) é usado como nome da pessoa
            nomes_conhecidos.append(nome)
    
    return rostos_conhecidos, nomes_conhecidos


def reconhecer_rostos_e_nomear(caminho_imagem, rostos_conhecidos, nomes_conhecidos):
    # Carregar a imagem desconhecida
    imagem_desconhecida = face_recognition.load_image_file(caminho_imagem)
    
    # Localizar rostos e codificar suas características
    localizacoes_rostos = face_recognition.face_locations(imagem_desconhecida)
    codificacoes_rostos = face_recognition.face_encodings(imagem_desconhecida, localizacoes_rostos)

    # Converter a imagem para OpenCV para exibição
    imagem_cv2 = cv2.cvtColor(imagem_desconhecida, cv2.COLOR_RGB2BGR)

    # Percorrer os rostos encontrados
    for (top, right, bottom, left), codificacao in zip(localizacoes_rostos, codificacoes_rostos):
        # Comparar o rosto detectado com os rostos conhecidos
        resultados = face_recognition.compare_faces(rostos_conhecidos, codificacao)
        distancias = face_recognition.face_distance(rostos_conhecidos, codificacao)
        
        # Usar o rosto mais próximo (menor distância)
        melhor_indice = distancias.argmin()
        if resultados[melhor_indice]:
            nome = nomes_conhecidos[melhor_indice]
        else:
            nome = "Desconhecido"
        
        # Desenhar um retângulo ao redor do rosto
        cv2.rectangle(imagem_cv2, (left, top), (right, bottom), (0, 255, 0), 2)
        # Colocar o nome abaixo do rosto
        cv2.putText(imagem_cv2, nome, (left, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Exibir a imagem com os rostos e os nomes
    cv2.imshow('Rostos Identificados', imagem_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
