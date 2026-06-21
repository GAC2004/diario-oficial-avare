#model.py
import torch.nn as nn

class ClassificadorDiario(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)

        self.fc1 = nn.Linear(embed_dim, 128)
        self.fc2 = nn.Linear(128, num_classes)

        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        x = self.relu(self.fc1(x))
        return self.fc2(x)