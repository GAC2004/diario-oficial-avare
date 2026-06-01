import requests
import pdfplumber
from bs4 import BeautifulSoup
from pathlib import Path

# Extrai texto de PDF
def extrair_de_pdf(caminho):
    
    textos = []

    with pdfplumber.open(caminho) as pdf:

        for pagina in pdf.pages:

            texto = pagina.extract_text()

            if texto:
                textos.append(texto)

    return '\n'.join(textos)

# Extrai texto de HTML
def extrair_de_html(url):

    headers = {
        'User-Agent': 'ProjetoFEAP/1.0'
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    soup = BeautifulSoup(
        response.text,
        'html.parser'
    )

    # Remove elementos desnecessários
    for tag in soup([
        'script',
        'style',
        'nav',
        'header',
        'footer'
    ]):
        tag.decompose()

    texto = soup.get_text(
        separator='\n',
        strip=True
    )

    return texto

# Teste rápido
if __name__ == '__main__':

    url = 'https://imprensaoficialmunicipal.com.br/avare'

    texto = extrair_de_html(url)

    print(texto[:1000])