# Relatório de Exploração — Diário Oficial de Avaré

## Estrutura do Site

O site apresenta publicações organizadas por edições do Diário Oficial.

## Tipos de Documentos

Foram encontrados documentos em HTML e PDFs.

## Padrão de URL

As URLs seguem o domínio:

https://imprensaoficialmunicipal.com.br/avare

## Ferramenta Escolhida

Foi utilizado requests + BeautifulSoup.

A escolha foi feita porque o HTML do site pode ser acessado diretamente sem necessidade inicial de JavaScript dinâmico.

## Bibliotecas Utilizadas
Biblioteca  =	Função
requests	=   Requisições HTTP
beautifulsoup4	= Extração de HTML
pandas = 	Manipulação de dados
pdfplumber	= Extração de PDFs
lxml = 	Parser HTML/XML

## Dificuldades Encontradas

Algumas informações como data da edição e número da edição não aparecem facilmente estruturadas no HTML.

## Comparação com Projeto TCU

Projeto TCU:
- https://github.com/netoferraz/acordaos-tcu

Semelhanças:
- Coleta automatizada de documentos públicos
- Organização em CSV
- Uso de Python

Diferenças:
- Projeto TCU possui escala maior
- Diário Oficial de Avaré possui menos complexidade
- O projeto atual é municipal

## ETAPAS PROJETO

## Etapa 1 — Coleta Inicial

- Acesso para o portal do Diário Oficial;
- Realizar requisições HTTP;
- Identificar publicações;
- Gerar arquivos CSV iniciais;

## Etapa 2 — Extração e Processamento Textual

- Implementação para extração textual de páginas HTML;
- A implementação da limpeza e normalização dos textos;
- A implementação da criação de base textual estruturada;
- A implementação da rotulagem automática inicial;
- A implementação da organização dos dados para NLP e Machine Learning.