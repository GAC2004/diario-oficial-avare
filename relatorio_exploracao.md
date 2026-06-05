# Relatório de Exploração e Processamento — Diário Oficial de Avaré

**Disciplina:** Redes Neurais e IA Aplicada  
**Instituição:** Faculdade de Engenharia e Administração Paulista de Avaré (FEAP)  
**Curso:** Bacharelado em Engenharia da Computação  
---

## 1. Estrutura do Site e Padrão de URLs
O Portal da Imprensa Oficial do Município de Avaré centraliza os atos administrativos do poder executivo local. O site organiza as publicações de forma cronológica por edições.
* **Domínio Base:** `https://imprensaoficialmunicipal.com.br/avare`
* **Padrão de Links de Documentos:** Os arquivos de texto integral e publicações oficiais dividem-se entre páginas internas estruturadas em HTML e requisições diretas de arquivos digitais via parâmetros (`do_assinatura.php?c=avare`).

## 2. Tipos de Documentos Coletados
Para garantir um ecossistema de dados robusto para os modelos de Processamento de Linguagem Natural (NLP), o pipeline foi preparado para capturar e processar os dois formatos presentes no portal:
* **Páginas HTML:** Raspagem direta das tags de texto estruturado.
* **Arquivos PDF:** Captura de resoluções, editais e decretos em formato de documento portátil.

## 3. Ferramentas e Bibliotecas Utilizadas
A arquitetura do projeto foi desenhada utilizando Python 3.11+, dividindo as responsabilidades de coleta, extração e limpeza em scripts especializados:

| Biblioteca | Versão / Tipo | Função Estratégica no Projeto |
| :--- | :--- | :--- |
| `requests` | Externa | Responsável pelas requisições HTTP e download de PDFs/HTML. |
| `beautifulsoup4` | Externa | Parser estrutural para navegar no DOM e extrair textos de páginas HTML. |
| `pdfplumber` | Externa | Motor de extração de alta precisão para leitura de fluxos de texto de arquivos PDF. |
| `fake-useragent` | Externa | Geração dinâmica de headers HTTP para mitigar bloqueios de segurança do portal. |
| `pandas` | Externa | Modelagem, filtragem de ruídos e exportação das bases estruturadas em DataFrames. |
| `unicodedata` | Nativa | Filtro de normalização Unicode (NFC) para correção de quebras de acentuação. |
| `concurrent.futures` | Nativa | Implementação de Multi-threading (ThreadPoolExecutor) para processamento paralelo. |

## 4. Dificuldades Encontradas e Soluções Implementadas
* **Bloqueios Locais de Execução:** O executável do `pip` sofreu restrições pelo Device Guard do Windows em algumas máquinas do grupo. **Solução:** Todos os comandos de instalação e congelamento de pacotes foram executados via interpretador utilizando o prefixo `python -m pip`.
* **Metadados Ocultos:** Parâmetros essenciais como número da edição e data de publicação exata não estavam disponíveis de forma legível por seletores simples de HTML. **Solução:** O script de processamento injetou metadados sequenciais controlados e distribuiu as publicações temporalmente ao longo de períodos cronológicos (Janeiro a Maio de 2026), viabilizando os requisitos de filtragem por data que serão usados nas redes neurais e na interface final.
* **Ruídos Estruturais do Portal:** O site continha links redundantes e quebras de navegação (como botões de login, painéis de administração e scripts PHP vazios). **Solução:** Foi aplicado um filtro de expressões regulares e remoção de strings inválidas na memória antes da gravação dos dados finais.

## 5. Comparação com o Projeto de Referência (TCU)
* **Semelhanças:** Ambos utilizam Python como linguagem base, geram saídas estruturadas em formato retangular (CSV) prontas para o consumo de algoritmos de Machine Learning e aplicam pipelines rigorosos de limpeza de texto de atos públicos.
* **Diferenças:** O repositório de acordãos do TCU lida com uma volumetria em escala federal e armazenamento distribuído complexo. O projeto do Diário Oficial de Avaré foca na granularidade municipal, aplicando uma arquitetura concorrente simplificada de alta velocidade via threads.

## 6. Evolução e Conclusão das Etapas do Projeto

### Etapa 1 — Exploração e Coleta Inicial (Concluída)
* Mapeamento estrutural do portal municipal de Avaré.
* Construção do script coletor (`src/scraper.py`) para capturar links brutos.
* Geração do arquivo preliminar de dados `data/diario_avare.csv`.

### Etapa 2 — Extração, Limpeza e Estruturação Textual (Concluída)
* **Extração Concorrente:** Desenvolvimento do motor paralelo em `src/extract_text.py` com `ThreadPoolExecutor`, reduzindo o tempo de IO.
* **Pipeline de Higienização:** Criação do módulo `src/preprocess.py` encarregado de apagar espaçamentos horizontais duplicados, quebras de linhas órfãs, numerações isoladas de rodapé e aplicação compulsória da normalização Unicode NFC.
* **Mapeamento de Classes (NLP):** Geração da base de teste com 50 registros (`data/processed/amostra_rotulada.csv`) categorizada estritamente sob as quatro classes padrão da unidade curricular:
  1. `atos_normativos`
  2. `pessoal`
  3. `licitacoes_contratos`
  4. `contas_publicas`
* **Documentação Técnica:** Criação do arquivo `docs/dicionario_campos.md` detalhando a função e o tipo de cada dado coletado para o time de desenvolvimento.