# 📘 Diário Oficial Inteligente de Avaré

Projeto Final da disciplina **Redes Neurais e IA Aplicada** da **Faculdade FEAP Avaré**
(Faculdade de Engenharia e Administração Paulista de Avaré)

🎓 **Curso:** Bacharelado em Engenharia da Computação

---

# 👨‍🏫 Professor Responsável da Matéria

**Prof. Fernando Oliveira**

---

# 👥 Alunos Participantes do Projeto

* Gabriela Arruda Carriel
* Stela Veiga Monteiro
* José Leonardo Pereira dos Santos
* Maria Júlia da Costa Teixeira
* Enzo Fortes
* Yehudi Witzel de Oliveira

---

# 🎯 Objetivo

Coletar automaticamente publicações do Diário Oficial de Avaré e estruturar os textos utilizando técnicas de Processamento de Linguagem Natural (NLP) para o futuro treinamento de Redes Neurais.

---

# 🛠️ Tecnologias

* Python
* Requests *(Coleta de páginas)*
* BeautifulSoup *(Raspagem de HTML)*
* pdfplumber *(Extração de texto de arquivos PDF)*
* fake-useragent *(Evitar bloqueios de requisições)*
* Pandas *(Estruturação de bases de dados)*
* Git e GitHub

---

# 🚀 Como Executar o Projeto

Siga os passos abaixo para executar corretamente o projeto.

---

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/GAC2004/diario-oficial-avare.git
```

---

## 2️⃣ Acessar a Pasta do Projeto

```bash
cd diario-oficial-avare
```

---

## 3️⃣ Criar Ambiente Virtual

```bash
python -m venv venv
```

---

## 4️⃣ Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

Após ativar, o terminal deverá mostrar:

```text
(venv)
```

---

## 5️⃣ Instalar as Dependências

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Ordem de Execução dos Scripts

## 🔹 scraper.py

Executa a coleta inicial do portal e gera a listagem bruta de links.

```bash
python src/scraper.py
```

---

## 🔹 extract_text.py

Realiza a extração textual em paralelo *(multithreading)* das páginas HTML/PDF utilizando o pipeline de limpeza do arquivo `preprocess.py`.

O script gera automaticamente os dois arquivos de saída.

```bash
python src/extract_text.py
```

---

# 📂 Arquivos Gerados

Após a execução dos scripts, a estrutura de pastas do projeto conterá:

---

## 📄 Base de Dados Bruta *(Links Coletados)*

```text
data/diario_avare.csv
```

---

## 📄 Base Textual Limpa *(Texto Integral Tratado)*

```text
data/processed/base_textual.csv
```

---

## 📄 Amostra Rotulada *(Mapeada nas Classes Oficiais de NLP)*

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

Durante o desenvolvimento foi identificado bloqueio do `pip.exe` pelo **Device Guard** do Windows.

Por esse motivo, os comandos foram executados utilizando:

```bash
python -m pip
```

em vez de:

```bash
pip
```