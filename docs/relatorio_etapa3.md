# Etapa 3 - Modelo (model.py e dataset.py)

## model.py
Rede neural composta por:
- Embedding
- Média dos embeddings
- Linear 128 neurônios
- ReLU
- Camada de saída com 3 classes

## dataset.py
Responsável por:
- Ler dataset_final.csv.
- Converter texto em índices.
- Retornar tensores para treinamento.
