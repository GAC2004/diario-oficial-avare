#app.py
import streamlit as st
import torch
import json
import pandas as pd
import torch.nn.functional as F
import re
from model import ClassificadorDiario

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Diário Oficial IA",
    layout="wide",
    page_icon="📄"
)

# =========================
# CSS DARK FIX COMPLETO
# =========================
st.markdown("""
<style>
/* FUNDO GERAL */
[data-testid="stAppViewContainer"], .main {
    background-color: #0e0e0e !important;
}

/* SIDEBAR E CONTEÚDO */
[data-testid="stSidebar"] {
    background-color: #111111 !important;
}

/* INPUTS E SELECTBOX (CORREÇÃO FORÇADA) */
div[data-baseweb="select"] > div {
    background-color: #1e1e1e !important;
    border: 1px solid #333 !important;
    color: #ffffff !important;
}

div[data-baseweb="select"] div[role="option"] {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] input {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
    border: 1px solid #333 !important;
}

/* TEXTO BASE */
body, p, span, div, label, h1, h2, h3, h4 {
    color: #ffffff !important;
}

/* BOTÕES */
[data-testid="stButton"] > button {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
}

/* CARDS E MÉTRICAS */
.card, [data-testid="stMetric"], .ai-box {
    background-color: #1a1a1a !important;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA & MODEL
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/dataset_final.csv")

df = load_data()

with open("data/processed/vocab.json", encoding="utf-8") as f:
    vocab = json.load(f)

model = ClassificadorDiario(len(vocab), 100, 3)
model.load_state_dict(torch.load("models/model.pt", map_location="cpu"))
model.eval()

# =========================
# FUNÇÕES
# =========================
def limpar(texto):
    texto = str(texto).lower()
    texto = re.sub(r"[^a-zà-ú0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()

def encode(texto):
    tokens = limpar(texto).split()[:200]
    ids = [vocab.get(t, 1) for t in tokens]
    return torch.tensor(ids).unsqueeze(0)

# =========================
# INTERFACE
# =========================
st.title("📄 Diário Oficial IA")
st.divider()

with st.sidebar:
    st.header("🔎 Filtros")
    busca = st.sidebar.text_input("Palavra-chave")
    anos = sorted(df["data"].dropna().astype(str).str[:4].unique())
    ano_sel = st.sidebar.selectbox("Ano", ["Todos"] + list(anos))
    tipo_sel = st.sidebar.selectbox("Tipo", ["Todos", "Decreto", "Lei", "Edital"])

# LÓGICA DE FILTRO
filtrado = df.copy()
if busca:
    filtrado = filtrado[filtrado["texto"].fillna("").str.contains(busca, case=False, regex=False)]
if ano_sel != "Todos":
    filtrado = filtrado[filtrado["data"].astype(str).str[:4] == str(ano_sel)]
if tipo_sel != "Todos":
    filtrado = filtrado[filtrado["texto"].str.lower().str.contains(tipo_sel.lower(), na=False)]

# EXIBIÇÃO
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("📌 Resultados")
    st.info(f"{len(filtrado)} documentos encontrados")
    for _, row in filtrado.head(10).iterrows():
        st.markdown(f"""<div class="card"><b>ID:</b> {row.get('iddo','?')} <br>
                        <b>Data:</b> {row.get('data','?')} <br><br>
                        {str(row["texto"])[:600]}...</div>""", unsafe_allow_html=True)

with col2:
    st.subheader("📊 Estatísticas")
    st.metric("Filtrados", len(filtrado))
    st.metric("Total", len(df))

st.divider()
st.subheader("🧠 Classificação IA")
texto = st.text_area("Cole um texto para classificar")

if st.button("Classificar"):
    if texto.strip():
        x = encode(texto)
        with torch.no_grad():
            prob = F.softmax(model(x), dim=1)
        classe = torch.argmax(prob, dim=1).item()
        CLASSES = {0: "📜 Decreto", 1: "📖 Lei", 2: "📢 Edital"}
        st.success(f"Classe: {CLASSES[classe]}")
        st.markdown(f'<div class="ai-box">Decreto: {prob[0][0]:.2%}<br>Lei: {prob[0][1]:.2%}<br>Edital: {prob[0][2]:.2%}</div>', unsafe_allow_html=True)
    else:
        st.warning("Digite um texto")