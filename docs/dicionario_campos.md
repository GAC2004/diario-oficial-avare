# Dicionário de Campos - Diário Oficial Inteligente de Avaré

**Unidade Curricular:** Redes Neurais e IA Aplicada | FEAP  
**Etapa 2:** Extração, Limpeza e Estruturação de Dados  
**Grupo:** [Insere o Número do Grupo]  

Este documento descreve a estrutura de dados da tabela final processada contida no arquivo `data/processed/base_textual.csv`, mapeando os tipos de dados e propósitos de cada campo no pipeline de NLP.

| Nome do Campo | Tipo de Dado | Descrição / Propósito no Modelo | Exemplo de Conteúdo |
| :--- | :--- | :--- | :--- |
| `data_publicacao` | Texto (AAAA-MM-DD) | Data em que o ato foi veiculado. Crucial para habilitar a busca e filtragem por períodos temporais específicos. | `2026-03-15` |
| `numero_edicao` | Texto / Inteiro | Identificador sequencial da edição do Diário Oficial do município. | `1204` |
| `titulo_ato` | Texto | Ementa resumida ou cabeçalho do ato administrativo extraído. | `DECRETO EXECUTIVO N° 3437/2026` |
| `tipo_ato` | Texto | Categoria original da publicação coletada no portal oficial. | `Publicação Oficial` |
| `url_documento` | Texto (URL) | Link absoluto de acesso à origem do documento (PDF ou HTML). | `https://imprensaoficialmunicipal.com.br/avare/...` |
| `texto_completo` | Texto Longo | Conteúdo integral limpo, normalizado em Unicode NFC, livre de ruídos e pronto para o treinamento de Embeddings de IA. | `DECRETO EXECUTIVO N°... Texto Integral:...` |
| `classe_rotulo` | Texto | (*Exclusivo do arquivo amostra_rotulada.csv*) Classe categórica alvo mapeada rigorosamente conforme a tabela oficial de NLP da faculdade. | `atos_normativos`, `pessoal`, `licitacoes_contratos`, `contas_publicas` |

## Mapeamento de Classes Utilizado na Amostra
* **`atos_normativos`**: Leis ordinárias, leis complementares e decretos executivos.
* **`pessoal`**: Portarias de nomeação, exoneração, portarias de férias e gratificações funcionais.
* **`licitacoes_contratos`**: Editais de licitação, avisos de pregão eletrônico, contratos e aditivos.
* **`contas_publicas`**: Balancetes financeiros, relatórios fiscais, orçamentos e prestações de contas municipais.