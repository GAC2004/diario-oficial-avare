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

- requests
- BeautifulSoup
- pandas

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