# scraper.py
import os
import json
import base64
import requests
import pandas as pd

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm

# ============================================================
# CONFIG
# ============================================================

API_URL = "https://dosp.com.br/api/index.php/dioe.js/4700?callback=dioe"
MUNICIPIO_URL = "Avar%C3%A9"

PASTA_RAW = "data/raw"
ARQUIVO_SAIDA = os.path.join(PASTA_RAW, "diarios.csv")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ============================================================
# SESSION
# ============================================================

def criar_sessao():
    retry = Retry(
        total=2,
        backoff_factor=0.3,
        status_forcelist=[429, 500, 502, 503, 504]
    )

    session = requests.Session()
    session.headers.update(HEADERS)
    session.mount("https://", HTTPAdapter(max_retries=retry))

    return session

session = criar_sessao()

# ============================================================
# JSONP seguro
# ============================================================

def extrair_json(texto):
    start = texto.find("{")
    end = texto.rfind("}") + 1
    return json.loads(texto[start:end])

# ============================================================
# BASE64
# ============================================================

def b64(v):
    return base64.b64encode(str(v).encode()).decode()

# ============================================================
# URL jornal
# ============================================================

def url_jornal(iddo):
    return (
        "https://imprensaoficialmunicipal.com.br/"
        f"leiturajornal.php?c={MUNICIPIO_URL}&i={b64(iddo)}"
    )

# ============================================================
# API
# ============================================================

def baixar_api():
    r = session.get(API_URL, timeout=20)

    if r.status_code != 200:
        raise Exception(f"Erro API: {r.status_code}")

    return extrair_json(r.text)

# ============================================================
# LINK TEXTO
# ============================================================

def pegar_link(html):
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "leituratexto" in href:
            if href.startswith("http"):
                return href
            return requests.compat.urljoin("https://dosp.com.br", href)

    return None

# ============================================================
# LIMPEZA HTML
# ============================================================

def limpar(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    return soup.get_text(" ", strip=True)

# ============================================================
# PROCESSO ITEM
# ============================================================

def processar_item(url):
    try:
        html = session.get(url, timeout=10).text

        link = pegar_link(html)

        if link:
            html2 = session.get(link, timeout=10).text
            texto = limpar(html2)
        else:
            texto = limpar(html)

        return texto if len(texto) > 80 else "SEM_TEXTO"

    except Exception as e:
        print("Erro:", e)
        return "SEM_TEXTO"

# ============================================================
# PIPELINE PARALELO (CORRIGIDO)
# ============================================================

def processar(df):
    urls = df["url_jornal"].tolist()
    textos = [None] * len(urls)

    print("Extraindo textos...")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(processar_item, url): i
            for i, url in enumerate(urls)
        }

        for f in tqdm(as_completed(futures), total=len(futures)):
            i = futures[f]
            textos[i] = f.result()

    df["texto"] = textos
    return df

# ============================================================
# MAIN
# ============================================================

def main():
    print("Baixando API...")

    dados = baixar_api()

    registros = []

    for item in dados["data"]:
        iddo = item.get("iddo")
        if not iddo:
            continue

        registros.append({
            "iddo": iddo,
            "edicao": item.get("edicao_do"),
            "data": item.get("data"),
            "url_jornal": url_jornal(iddo)
        })

    df = pd.DataFrame(registros)

    df = processar(df)

    os.makedirs(PASTA_RAW, exist_ok=True)

    df.to_csv(ARQUIVO_SAIDA, index=False, encoding="utf-8")

    print("FINALIZADO:", len(df))


if __name__ == "__main__":
    main()