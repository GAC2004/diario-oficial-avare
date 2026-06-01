import re
import unicodedata

# Limpeza básica
def limpar_texto(texto):

    # Remove espaços excessivos
    texto = re.sub(r'[ \t]+', ' ', texto)

    # Remove muitas quebras de linha
    texto = re.sub(r'\n{3,}', '\n\n', texto)

    # Remove linhas apenas com números
    texto = re.sub(
        r'^\s*\d+\s*$',
        '',
        texto,
        flags=re.MULTILINE
    )

    # Remove caracteres estranhos
    texto = re.sub(
        r'[\x00-\x08\x0b\x0c\x0e-\x1f]',
        '',
        texto
    )

    return texto.strip()

# Normalização
def normalizar_texto(texto):

    texto = unicodedata.normalize(
        'NFC',
        texto
    )

    texto = texto.replace('--', '-')

    return texto

# Pipeline completo
def processar(texto):

    texto = limpar_texto(texto)

    texto = normalizar_texto(texto)

    return texto

# Teste
if __name__ == '__main__':

    texto_sujo = '''
    Decreto 123


    Prefeitura de Avaré


    1
    '''

    texto_limpo = processar(texto_sujo)

    print(texto_limpo)