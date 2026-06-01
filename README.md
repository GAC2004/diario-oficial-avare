# Diário Oficial Inteligente de Avaré

Projeto Final da disciplina Redes Neurais e IA Aplicada da Faculdade FEAP Avaré (Faculdade de Engenharia e Administração Paulista de Avaré)  
Bacharelado em Engenharia da Computação

## Professor Responsável da Matéria

Prof° Fernando Oliveira

## Alunos Participantes do Projeto

* Gabriela Arruda Carriel 
* Stela Veiga Monteiro
* José Leonardo Pereira dos Santos
* Maria Júlia da Costa Teixeira
* Enzo Fortes
* Yehudi Witzel de Oliveira

## Objetivo

Coletar automaticamente publicações do Diário Oficial de Avaré usando Python.

## Tecnologias

- Python
- Requests
- BeautifulSoup
- Pandas
- Git e GitHub

---

# 🚀 Como Executar o Projeto

Siga os passos abaixo para executar corretamente o projeto.

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/GAC2004/diario-oficial-avare.git
```

---

## 2️⃣ Acessar a pasta do projeto

```bash
cd diario-oficial-avare
```

---

## 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

## 4️⃣ Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

Após ativar, o terminal deverá mostrar:

```text
(venv)
```

---

## 5️⃣ Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Ordem de Execução dos Scripts

## scraper.py

Executa a coleta inicial do portal.

```bash
python src/scraper.py
```

---

## extract_text.py

Realiza a extração textual das páginas HTML/PDF.

```bash
python src/extract_text.py
```

---

## generate_base.py

Gera automaticamente:

* base textual estruturada;
* amostra rotulada;
* organização dos dados para NLP.

```bash
python src/generate_base.py
```

---

# 📂 Arquivos Gerados

Após a execução dos scripts, serão gerados:

## Base textual

```text
data/processed/base_textual.csv
```

## Amostra rotulada

```text
data/processed/amostra_rotulada.csv
```

---

# 🛠️ Atualizar Dependências

Caso novas bibliotecas sejam instaladas:

```bash
python -m pip freeze > requirements.txt
```

---

# ⚠️ Observações

Durante o desenvolvimento foi identificado bloqueio do `pip.exe` pelo Device Guard do Windows.

Por esse motivo, os comandos foram executados utilizando:

```bash
python -m pip
```

em vez de:

```bash
pip
```