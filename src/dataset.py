import json
import pandas as pd
import torch
from torch.utils.data import Dataset

class DatasetDiario(Dataset):
    def __init__(self,csv,vocab_json):
        self.df=pd.read_csv(csv)
        with open(vocab_json,encoding='utf8') as f:
            self.vocab=json.load(f)

    def encode(self,texto):
        return torch.tensor([self.vocab.get(w,1) for w in str(texto).split()[:200]])

    def __len__(self):
        return len(self.df)

    def __getitem__(self,idx):
        row=self.df.iloc[idx]
        return self.encode(row['texto']), int(row['label'])
