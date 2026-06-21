# Relatório de Exploração e Processamento de Dados — Diário Oficial Inteligente de Avaré

**Disciplina:** Redes Neurais e IA Aplicada
**Instituição:** Faculdade de Engenharia e Administração Paulista de Avaré (FEAP)
**Curso:** Bacharelado em Engenharia da Computação

---

# 1. Introdução

Este documento descreve as etapas de exploração, coleta, processamento e preparação dos dados utilizados no desenvolvimento do projeto **Diário Oficial Inteligente de Avaré**.

O objetivo do projeto é automatizar o processo de obtenção das publicações do Diário Oficial do Município de Avaré, estruturar os dados textuais e aplicar técnicas de Inteligência Artificial e Processamento de Linguagem Natural (NLP) para classificar automaticamente os atos administrativos.

Todo o pipeline foi desenvolvido em Python, desde a coleta dos documentos até a disponibilização dos resultados em uma interface web.

---

# 2. Fonte dos Dados

As informações utilizadas no projeto foram obtidas a partir do Portal Oficial da Imprensa Oficial do Município de Avaré.

**Portal:**

```
https://imprensaoficialmunicipal.com.br/avare
```

O portal disponibiliza as edições do Diário Oficial contendo decretos, leis, editais, licitações, nomeações e demais atos administrativos publicados pelo município.

---

# 3. Estrutura do Portal

Durante a fase de exploração foi identificado que o portal organiza suas publicações de maneira cronológica.

Cada edição contém diversos atos administrativos, podendo estar disponíveis em dois formatos distintos:

* páginas HTML;
* documentos PDF.

As informações de cada edição incluem metadados como:

* data da publicação;
* número da edição;
* ano;
* link para o documento;
* texto completo do ato administrativo.

---

# 4. Processo de Coleta

A coleta foi implementada no script:

```
src/scraper.py
```

O processo realiza automaticamente:

* acesso ao portal;
* identificação das edições disponíveis;
* obtenção dos links dos documentos;
* download dos arquivos necessários;
* geração da base inicial de dados.

Ao final desta etapa é produzido o arquivo:

```
data/diario_avare.csv
```

que contém todos os metadados utilizados nas etapas seguintes.

---

# 5. Extração dos Textos

Após a coleta, os documentos são processados pelo script:

```
src/extract_text.py
```

Esta etapa realiza:

* abertura dos arquivos PDF;
* extração do conteúdo textual;
* leitura das páginas HTML quando disponível;
* processamento paralelo utilizando ThreadPoolExecutor;
* integração com o módulo de pré-processamento.

O processamento paralelo reduziu significativamente o tempo de execução durante a leitura dos documentos.

---

# 6. Pré-processamento dos Dados

O tratamento textual é realizado pelo módulo:

```
src/preprocess.py
```

As principais etapas são:

* remoção de caracteres inválidos;
* normalização Unicode;
* remoção de múltiplos espaços;
* remoção de quebras de linha desnecessárias;
* padronização da acentuação;
* limpeza de textos duplicados;
* remoção de ruídos provenientes da conversão dos PDFs.

Após essa etapa é gerada a base textual utilizada pelo modelo de Inteligência Artificial.

---

# 7. Construção da Base de Dados

Os textos extraídos são armazenados em arquivos CSV estruturados.

Arquivos produzidos:

```
data/diario_avare.csv
```

Base contendo os metadados coletados.

---

```
data/processed/base_textual.csv
```

Base contendo o texto completo de cada publicação.

---

```
data/processed/amostra_rotulada.csv
```

Conjunto de exemplos classificados manualmente para treinamento supervisionado.

---

# 8. Classificação dos Atos

Foi construída uma base rotulada contendo quatro categorias principais:

* atos_normativos
* pessoal
* licitacoes_contratos
* contas_publicas

Essas categorias serviram como conjunto inicial para o treinamento do modelo de classificação.

---

# 9. Modelo de Inteligência Artificial

Após a preparação dos dados foi desenvolvido um modelo de classificação utilizando a biblioteca PyTorch.

O pipeline consiste em:

```
Texto

↓

Pré-processamento

↓

Vetorização

↓

Rede Neural

↓

Categoria Prevista
```

Durante o treinamento são calculadas métricas como:

* Accuracy
* Precision
* Recall
* F1-Score

Essas métricas permitem avaliar o desempenho do modelo na classificação automática das publicações.

---

# 10. Interface Web

Foi desenvolvida uma aplicação utilizando Streamlit para facilitar a utilização do modelo treinado.

A interface permite:

* visualizar as publicações;
* pesquisar por palavras-chave;
* filtrar por ano;
* filtrar por categoria;
* visualizar a categoria prevista pelo modelo;
* consultar a probabilidade da classificação.

Dessa forma, o usuário consegue explorar rapidamente grandes volumes de publicações oficiais.

---

# 11. Tecnologias Utilizadas

| Tecnologia         | Finalidade                 |
| ------------------ | -------------------------- |
| Python             | Linguagem principal        |
| Requests           | Requisições HTTP           |
| BeautifulSoup      | Extração de conteúdo HTML  |
| pdfplumber         | Extração de texto dos PDFs |
| Pandas             | Manipulação dos dados      |
| PyTorch            | Rede Neural                |
| Streamlit          | Interface Web              |
| fake-useragent     | Simulação de navegador     |
| ThreadPoolExecutor | Processamento paralelo     |
| Git                | Controle de versão         |
| GitHub             | Hospedagem do projeto      |

---

# 12. Principais Dificuldades

Durante o desenvolvimento foram encontrados alguns desafios.

## Bloqueio do pip

Em algumas máquinas o Windows Device Guard bloqueava a execução do executável `pip.exe`.

Como solução, todas as instalações foram realizadas utilizando:

```
python -m pip
```

---

## Extração dos PDFs

Alguns documentos possuíam formatação irregular, ocasionando quebras excessivas de linha e caracteres inválidos.

Foi desenvolvido um módulo específico de limpeza textual para padronizar todos os documentos antes do treinamento.

---

## Estrutura Heterogênea

Nem todas as publicações possuíam o mesmo padrão de estrutura.

Foi necessário criar regras específicas para tratar documentos HTML e PDF separadamente.

---

## Desempenho

O processamento sequencial tornava a extração muito lenta.

A utilização de processamento paralelo com ThreadPoolExecutor reduziu significativamente o tempo de execução.

---

# 13. Comparação com o Projeto de Referência

O projeto foi inspirado na organização utilizada pelo repositório de Acórdãos do Tribunal de Contas da União (TCU).

## Semelhanças

* utilização de Python;
* estruturação em CSV;
* preparação de bases para Machine Learning;
* processamento automático de documentos oficiais.

## Diferenças

Enquanto o projeto do TCU trabalha com documentos federais em larga escala, este projeto concentra-se exclusivamente nas publicações do Município de Avaré, permitindo um pipeline mais simples e especializado.

---

# 14. Resultados Obtidos

Ao término do desenvolvimento foi possível construir um pipeline completo composto pelas seguintes etapas:

* coleta automática dos documentos;
* extração textual;
* limpeza dos dados;
* criação da base estruturada;
* treinamento da Rede Neural;
* classificação automática;
* disponibilização dos resultados em interface web.

O sistema elimina grande parte do trabalho manual necessário para organizar as publicações do Diário Oficial, oferecendo uma solução automatizada baseada em Inteligência Artificial.

---

# 15. Conclusão

O projeto atingiu os objetivos propostos pela disciplina de Redes Neurais e IA Aplicada.

Foi desenvolvido um sistema capaz de coletar, organizar, processar e classificar automaticamente documentos do Diário Oficial de Avaré, integrando técnicas de Web Scraping, Processamento de Linguagem Natural, Aprendizado de Máquina e desenvolvimento de aplicações web.

Além de cumprir os requisitos acadêmicos da disciplina, o projeto demonstra o potencial da Inteligência Artificial na automatização da gestão e análise de documentos públicos.
