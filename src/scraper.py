import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://imprensaoficialmunicipal.com.br/avare"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Acessando site...")

response = requests.get(URL, headers=headers)

print(f"Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

print("Título da página:")
print(soup.title.string)

# Lista para salvar os dados
publicacoes = []

# Busca todos os links
links = soup.find_all("a", href=True)

print(f"Total de links encontrados: {len(links)}")

for link in links:

    texto = link.get_text(strip=True)
    href = link["href"]

    # Ignora links pequenos
    if len(texto) < 5:
        continue

    # Completa links relativos
    if href.startswith("/"):
        href = "https://imprensaoficialmunicipal.com.br" + href

    publicacoes.append({
        "data_publicacao": "Não identificado",
        "numero_edicao": "Não identificado",
        "titulo_ato": texto,
        "tipo_ato": "Publicação Oficial",
        "url_documento": href
    })

# Cria DataFrame
df = pd.DataFrame(publicacoes)

# Remove duplicados
df = df.drop_duplicates()

# Mantém apenas 20 linhas
df = df.head(20)

# Salva CSV
df.to_csv(
    "data/diario_avare.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nCSV salvo com sucesso!")

print(df.head())