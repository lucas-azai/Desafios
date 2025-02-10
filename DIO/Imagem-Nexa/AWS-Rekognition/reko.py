import boto3
import os

def detect_celebrities(image_path):
    """Detecta celebridades em uma imagem usando AWS Rekognition."""
    rekognition = boto3.client('rekognition', region_name='us-east-1')
    
    with open(image_path, "rb") as image:
        response = rekognition.recognize_celebrities(Image={'Bytes': image.read()})
    
    if not response['CelebrityFaces']:
        print("Nenhuma celebridade detectada.")
        return []
    
    celebrities = []
    for celebrity in response['CelebrityFaces']:
        name = celebrity['Name']
        confidence = celebrity['MatchConfidence']
        print(f"Detectado: {name} com {confidence:.2f}% de confiança.")
        celebrities.append((name, confidence))
    
    return celebrities


def save_results(celebrities, output_path):
    """Salva os resultados em um arquivo."""
    with open(output_path, "w", encoding="utf-8") as file:
        for name, confidence in celebrities:
            file.write(f"{name}: {confidence:.2f}%\n")
    print(f"Resultados salvos em: {output_path}")


if __name__ == "__main__":
    image_path = "celebridade.jpg"  # Substitua pelo caminho da sua imagem
    output_path = "celebridades_detectadas.txt"
    
    if not os.path.exists(image_path):
        print(f"Erro: O arquivo {image_path} não foi encontrado!")
    else:
        celebrities = detect_celebrities(image_path)
        save_results(celebrities, output_path)
