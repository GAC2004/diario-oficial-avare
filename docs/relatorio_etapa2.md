# Etapa 2 - Extração e Pré-processamento

Arquivos: extract_text.py, preprocess.py e train.py.

## extract_text.py
- Utiliza asyncio e aiohttp.
- Extrai os textos das publicações.
- Salva data/processed/diarios.csv.

## preprocess.py
- Limpa caracteres especiais.
- Tokeniza os textos.
- Cria labels automaticamente.
- Gera vocab.json.
- Gera dataset_final.csv.

## train.py
- Codifica os textos.
- Treina a rede neural.
- Salva models/model.pt.
