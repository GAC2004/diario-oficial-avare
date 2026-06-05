import re
import unicodedata

def limpar_texto(texto):
    if not texto:
        return ""
    # Remove excesso de espaços horizontais e tabulações
    texto = re.sub(r'[ \t]+', ' ', texto)
    # Padroniza quebras de linha excessivas (máximo duas seguidas)
    texto = re.sub(r'\n{3,}', '\n\n', texto)
    # Remove linhas que contêm apenas números isolados (comum em rodapés)
    texto = re.sub(r'^\s*\d+\s*$', '', texto, flags=re.MULTILINE)
    # Remove caracteres invisíveis e de controle ASCII
    texto = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', texto)
    return texto.strip()

def normalizar_texto(texto):
    if not texto:
        return ""
    # Força a normalização Unicode NFC para evitar bugs de acentuação na IA
    texto = unicodedata.normalize('NFC', texto)
    # Corrige hifens duplos deixados por quebras de página de PDF
    texto = texto.replace('--', '-')
    return texto

def processar(texto):
    """Executa o pipeline completo de tratamento textual"""
    texto = limpar_texto(texto)
    texto = normalizar_texto(texto)
    return texto

if __name__ == '__main__':
    print("Pipeline de pré-processamento pronto para uso.")