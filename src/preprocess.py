#preprocess.py
import pandas as pd
import json
import os
import re
from collections import Counter

CSV = "data/processed/diarios.csv"
OUT_VOCAB = "data/processed/vocab.json"
OUT_DATASET = "data/processed/dataset_final.csv"

def limpar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"[^a-zà-ú0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

def tokenizar(texto: str):
    return texto.split()

def gerar_label(texto):
    t = texto.lower()
    if "decreto" in t:
        return 0
    if "lei" in t:
        return 1
    if "edital" in t:
        return 2
    return 0

def processar():
    if not os.path.exists(CSV):
        raise FileNotFoundError("diarios.csv não existe. Rode extract_text.py primeiro.")

    df = pd.read_csv(CSV)

    counter = Counter()
    textos_limpos = []
    labels = []

    print("Processando textos...")

    for texto in df["texto"].fillna("").astype(str):
        limpo = limpar_texto(texto)
        tokens = tokenizar(limpo)

        counter.update(tokens)

        textos_limpos.append(limpo)
        labels.append(gerar_label(limpo))

    # vocab
    vocab = {"<PAD>": 0, "<UNK>": 1}

    for i, (word, _) in enumerate(counter.most_common(20000)):
        vocab[word] = i + 2

    # salva vocab
    os.makedirs("data/processed", exist_ok=True)
    with open(OUT_VOCAB, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False)

    # salva dataset FINAL (isso faltava!)
    df_out = pd.DataFrame({
         "iddo": df["iddo"],
         "data": df["data"],
        "texto": textos_limpos,
        "label": labels
    })

    df_out.to_csv(OUT_DATASET, index=False, encoding="utf-8")

    print("OK dataset_final criado:", len(df_out))
    print("Vocab:", len(vocab))

if __name__ == "__main__":
    processar()