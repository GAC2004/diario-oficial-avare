# train.py
import torch
import pandas as pd
import json
import os
from model import ClassificadorDiario
from torch.nn.utils.rnn import pad_sequence

df = pd.read_csv("data/processed/dataset_final.csv")

with open("data/processed/vocab.json", encoding="utf-8") as f:
    vocab = json.load(f)

def encode(text):
    return [vocab.get(w, 1) for w in str(text).lower().split()[:200]]

def gerar_label(texto):
    t = texto.lower()
    if "decreto" in t:
        return 0
    if "lei" in t:
        return 1
    if "edital" in t:
        return 2
    return 0

X = []
y = []

for t in df["texto"].fillna(""):
    X.append(torch.tensor(encode(t)))
    y.append(gerar_label(t))

X = pad_sequence(X, batch_first=True, padding_value=0)
y = torch.tensor(y)

model = ClassificadorDiario(len(vocab), 100, 3)

loss_fn = torch.nn.CrossEntropyLoss()
opt = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    out = model(X)
    loss = loss_fn(out, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

    print(f"epoch {epoch} loss {loss.item():.4f}")

os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), "models/model.pt")

print("Modelo salvo")