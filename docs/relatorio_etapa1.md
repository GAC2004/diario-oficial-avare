# Etapa 1 - Coleta (scraper.py)

## Objetivo
Coletar automaticamente os metadados do Diário Oficial utilizando a API.

## Principais funções
- criar_sessao(): cria sessão HTTP com retry.
- baixar_api(): consulta a API.
- extrair_json(): converte JSONP para JSON.
- url_jornal(): monta a URL da publicação.
- processar_item(): extrai o texto HTML.
- processar(): executa em paralelo com ThreadPoolExecutor.
- main(): gera data/raw/diarios.csv.

## Resultado
Arquivo inicial contendo iddo, data, edição, URL e texto.
