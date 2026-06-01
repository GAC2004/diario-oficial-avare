import requests
import pandas as pd

from bs4 import BeautifulSoup

from preprocess import processar

URL = 'https://imprensaoficialmunicipal.com.br/avare'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

print('Acessando portal...')

response = requests.get(
    URL,
    headers=headers,
    timeout=10
)

print(f'Status Code: {response.status_code}')

# Verifica conexão
if response.status_code != 200:

    print('Erro ao acessar o site.')
    exit()

# Cria BeautifulSoup
soup = BeautifulSoup(
    response.text,
    'html.parser'
)

# Busca todos os links
links = soup.find_all('a', href=True)

print(f'Total de links encontrados: {len(links)}')

registros = []

contador = 1

for link in links:

    try:

        texto = link.get_text(strip=True)

        href = link['href']

        # Ignora links vazios
        if len(texto.strip()) == 0:
            continue

        # Completa links relativos
        if href.startswith('/'):
            href = 'https://imprensaoficialmunicipal.com.br' + href

        # Limpa texto
        texto_limpo = processar(texto)

        # Ignora duplicados muito pequenos
        if len(texto_limpo) < 3:
            continue

        # Detecta rótulos automaticamente
        texto_lower = texto_limpo.lower()

        rotulo = 'outros'

        if 'decreto' in texto_lower:
            rotulo = 'decreto'

        elif 'portaria' in texto_lower:
            rotulo = 'portaria'

        elif 'licitação' in texto_lower:
            rotulo = 'licitacao_contrato'

        elif 'licitacao' in texto_lower:
            rotulo = 'licitacao_contrato'

        elif 'contrato' in texto_lower:
            rotulo = 'licitacao_contrato'

        elif 'concurso' in texto_lower:
            rotulo = 'edital_concurso'

        elif 'edital' in texto_lower:
            rotulo = 'edital_concurso'

        elif 'servidor' in texto_lower:
            rotulo = 'ato_pessoal'

        elif 'nomeação' in texto_lower:
            rotulo = 'ato_pessoal'

        elif 'contas' in texto_lower:
            rotulo = 'contas_publicas'

        registro = {

            'id': f'DOA-2026-{contador:03}',

            'data_publicacao': '2026-06-01',

            'numero_edicao': '0001',

            'tipo_ato': 'Publicação Oficial',

            'titulo': texto_limpo,

            'secretaria': 'Não identificada',

            'texto': texto_limpo,

            'url_original': href,

            'rotulo': rotulo
        }

        registros.append(registro)

        contador += 1

    except Exception as erro:

        print(f'Erro ao processar link: {erro}')

# Verifica se encontrou registros
if len(registros) == 0:

    print('\nNenhum registro encontrado.')
    exit()

# Cria DataFrame
df = pd.DataFrame(registros)

# Remove duplicados
df = df.drop_duplicates()

# Limita registros
df = df.head(50)

# Salva base textual
df.to_csv(
    'data/processed/base_textual.csv',
    index=False,
    encoding='utf-8-sig'
)

# Salva amostra rotulada
df.to_csv(
    'data/processed/amostra_rotulada.csv',
    index=False,
    encoding='utf-8-sig'
)

print('\nArquivos gerados com sucesso!')

print('\nPrévia da base:\n')

print(df.head())