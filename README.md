# 📘 Diário Oficial Inteligente de Avaré

Projeto Final da disciplina **Redes Neurais e IA Aplicada**, desenvolvido na **Faculdade de Engenharia e Administração Paulista de Avaré (FEAP)**.

🎓 **Curso:** Bacharelado em Engenharia da Computação

---

# 👨‍🏫 Professor Responsável

**Prof. Fernando Oliveira**

---

# 👥 Equipe

- Gabriela Arruda Carriel
- Stela Veiga Monteiro
- José Leonardo Pereira dos Santos
- Maria Júlia da Costa Teixeira
- Enzo Fortes
- Yehudi Witzel de Oliveira

---

# 📖 Sobre o Projeto

O projeto tem como objetivo automatizar a coleta, processamento e classificação das publicações do Diário Oficial do Município de Avaré utilizando técnicas de Inteligência Artificial e Processamento de Linguagem Natural (NLP).

O sistema realiza todo o pipeline de processamento, desde a obtenção das publicações até sua classificação automática em categorias administrativas.

---

# 🎯 Objetivos

- Automatizar a coleta das publicações do Diário Oficial.
- Extrair texto dos documentos em PDF.
- Realizar limpeza e normalização dos textos.
- Construir uma base de dados estruturada.
- Treinar uma Rede Neural para classificação automática.
- Disponibilizar uma interface web para consulta e classificação.

---

# ⚙️ Funcionalidades

✔ Coleta automática do Diário Oficial

✔ Download dos arquivos PDF

✔ Extração textual dos documentos

✔ Pré-processamento utilizando NLP

✔ Criação automática da base de dados

✔ Treinamento da Rede Neural

✔ Classificação automática dos atos públicos

✔ Interface Web desenvolvida em Streamlit

---

# 🛠 Tecnologias Utilizadas

## Linguagem

- Python 3.14

## Bibliotecas

- PyTorch
- Pandas
- Requests
- BeautifulSoup4
- pdfplumber
- fake-useragent
- Streamlit
- Scikit-learn
- tqdm

## Ferramentas

- Git
- GitHub
- Visual Studio Code

---

# 📂 Estrutura do Projeto

```
diario-oficial-avare/

│
├── data/
│   ├── pdfs/
│   ├── processed/
│   └── diario_avare.csv
│
├── models/
│
├── src/
│   ├── scraper.py
│   ├── extract_text.py
│   ├── preprocess.py
│   ├── train.py
│   ├── model.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Instalação

## 1. Clonar o repositório

```bash
git clone https://github.com/GAC2004/diario-oficial-avare.git
```

---

## 2. Entrar na pasta

```bash
cd diario-oficial-avare
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 5. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

---

# ▶ Pipeline de Execução

## 1. Coleta dos Diários Oficiais

```bash
python src/scraper.py
```

Gera:

```
data/diario_avare.csv
```

---

## 2. Extração dos textos

```bash
python src/extract_text.py
```

Gera:

```
data/processed/base_textual.csv
```

---

## 3. Treinamento da Rede Neural

```bash
python src/train.py
```

Gera:

- modelo treinado
- encoder de classes
- métricas

---

## 4. Executar a Interface Web

```bash
streamlit run src/app.py
```

---

# 📄 Arquivos Gerados

## Base de links

```
data/diario_avare.csv
```

---

## Base textual

```
data/processed/base_textual.csv
```

---

## Amostra rotulada

```
data/processed/amostra_rotulada.csv
```

---

## Modelo treinado

```
models/modelo.pth
```

---

## Encoder

```
models/label_encoder.pkl
```

---

# 🧠 Modelo de Inteligência Artificial

O projeto utiliza uma Rede Neural desenvolvida em **PyTorch** para classificar automaticamente os textos do Diário Oficial.

Fluxo:

```
Texto

↓

Pré-processamento

↓

Tokenização

↓

Vetorização

↓

Rede Neural

↓

Categoria prevista
```

---

# 🌐 Interface Web

A aplicação foi desenvolvida utilizando **Streamlit**, permitindo:

- pesquisa por palavras-chave;
- filtro por ano;
- filtro por tipo de ato;
- visualização das classificações;
- exibição da probabilidade prevista pelo modelo.

---

# 📈 Resultados

O modelo foi treinado utilizando textos previamente rotulados da base de dados.

Após o treinamento são exibidas métricas como:

- Accuracy
- Precision
- Recall
- F1-Score

---

# 🔄 Atualizar Dependências

Caso novas bibliotecas sejam instaladas:

```bash
python -m pip freeze > requirements.txt
```

---

# ⚠️ Observações

Durante o desenvolvimento foi identificado bloqueio do **pip.exe** pelo Windows Device Guard.

Por esse motivo, recomenda-se utilizar:

```bash
python -m pip
```

em vez de:

```bash
pip
```

---

# 📚 Disciplina

Projeto desenvolvido para a disciplina de **Redes Neurais e IA Aplicada**.

Faculdade de Engenharia e Administração Paulista de Avaré (FEAP).

---

# 📄 Licença

Este projeto possui finalidade exclusivamente acadêmica.