# Dicionário de Campos

Este documento apresenta a descrição dos campos utilizados na base textual estruturada do projeto Diário Oficial Inteligente de Avaré.

---

# Arquivo Relacionado

```text
data/processed/base_textual.csv
```

---

# Campos da Base

| Campo           | Tipo   | Descrição                               |
| --------------- | ------ | --------------------------------------- |
| id              | string | Identificador único da publicação       |
| data_publicacao | string | Data da publicação                      |
| numero_edicao   | string | Número da edição do Diário Oficial      |
| tipo_ato        | string | Tipo geral da publicação                |
| titulo          | string | Título da publicação encontrada         |
| secretaria      | string | Secretaria responsável pela publicação  |
| texto           | string | Texto processado da publicação          |
| url_original    | string | URL original da publicação              |
| rotulo          | string | Classe textual utilizada para rotulagem |

---

# Classes Utilizadas

As classes utilizadas na rotulagem inicial foram:

* decreto
* portaria
* licitacao_contrato
* edital_concurso
* ato_pessoal
* contas_publicas
* outros

---

# Objetivo da Base

A base textual estruturada foi criada para utilização futura em tarefas envolvendo:

* Processamento de Linguagem Natural (NLP);
* Machine Learning;
* Classificação supervisionada;
* Mineração de dados públicos.