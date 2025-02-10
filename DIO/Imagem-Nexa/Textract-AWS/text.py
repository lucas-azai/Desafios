import boto3

def extract_text_from_image(image_path):
    textract = boto3.client('textract', region_name='us-east-1')

    with open(image_path, "rb") as image:
        response = textract.detect_document_text(Document={'Bytes': image.read()})

    extracted_text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + '\n'
    
    return extracted_text

# Teste o código com uma imagem
image_path = "caminho/para/sua/imagem.jpg"
text = extract_text_from_image(image_path)
print(text)
