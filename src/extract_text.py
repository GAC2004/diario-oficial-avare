#extract_text.py
import os
import json
import base64
import asyncio
import aiohttp
import pandas as pd
import re

# ============================================================
# CONFIG
# ============================================================

API_URL = "https://dosp.com.br/api/index.php/dioe.js/4700?callback=dioe"
MUNICIPIO_URL = "Avar%C3%A9"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

cache = {}

# ============================================================
# JSONP
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
# URL
# ============================================================

def url_jornal(iddo):
    return f"https://imprensaoficialmunicipal.com.br/leiturajornal.php?c={MUNICIPIO_URL}&i={b64(iddo)}"

# ============================================================
# LIMPEZA HTML (rápida)
# ============================================================

def limpar(html):
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    html = re.sub(r"<style.*?</style>", "", html, flags=re.S)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()

# ============================================================
# LINK TEXTO
# ============================================================

def pegar_link(html):
    m = re.search(r'href="(https://dosp\.com\.br/leituratexto\?p=[^"]+)"', html)
    return m.group(1) if m else None

# ============================================================
# API ASYNC
# ============================================================

async def baixar_api(session):
    async with session.get(API_URL) as resp:
        text = await resp.text()
        return extrair_json(text)

# ============================================================
# FETCH URL
# ============================================================

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as resp:
            return await resp.text()
    except:
        return ""

# ============================================================
# PROCESSO ITEM
# ============================================================

async def processar_item(session, url):
    if url in cache:
        return cache[url]

    html = await fetch(session, url)

    link = pegar_link(html)

    if link:
        html2 = await fetch(session, link)
        texto = limpar(html2)
    else:
        texto = limpar(html)

    if len(texto) < 80:
        texto = "SEM_TEXTO"

    cache[url] = texto
    return texto

# ============================================================
# PIPELINE ASYNC
# ============================================================

async def processar(df, session):
    urls = df["url_jornal"].tolist()

    print(f"Processando {len(urls)} URLs (async)...")

    tasks = [processar_item(session, url) for url in urls]

    resultados = await asyncio.gather(*tasks)

    df["texto"] = resultados
    return df

# ============================================================
# MAIN
# ============================================================

async def main():
    print("Baixando API...")

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        dados = await baixar_api(session)

        df = pd.DataFrame([
            {
                "iddo": i["iddo"],
                "data": i["data"],
                "edicao": i["edicao_do"],
                "url_jornal": url_jornal(i["iddo"])
            }
            for i in dados["data"]
            if i.get("iddo")
        ])

        df = await processar(df, session)

        os.makedirs("data/processed", exist_ok=True)
        df.to_csv("data/processed/diarios.csv", index=False, encoding="utf-8")

        print("FINALIZADO:", len(df))

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())