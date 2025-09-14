import streamlit as st
from dados import dados_filmes
from main import recomendar_filmes_por_emoji, emojis_para_genero

# Usa o cache para carregar os dados uma única vez
@st.cache_data
def get_data():
    return dados_filmes()

st.title("Recomendador de Filmes por Emojis")

# Carrega o DataFrame no início da aplicação
# Corrigido: a chamada à função tem os parênteses `()`
dados_filmes = get_data()

# Verificação de depuração para garantir que a variável é um DataFrame
st.write("---")
st.write(f"**Tipo da variável `dados_filmes`**: {type(dados_filmes)}")
st.write("---")

if dados_filmes is None or dados_filmes.empty:
    st.error("Erro ao carregar ou processar os dados de filmes. Verifique o caminho do arquivo no `data_loader.py`.")
    st.stop()

st.markdown("""
<div style="font-size: 1.2em; font-weight: bold;">
    Olá! Escolha um ou mais emojis para receber uma recomendação de filme.
</div>
""", unsafe_allow_html=True)

opcoes_emojis = list(emojis_para_genero.keys())

st.write(f"**As opções de emoji são:** {opcoes_emojis}")

emojis_selecionados = st.multiselect(
    label="Selecione um ou mais emojis:",
    options=opcoes_emojis,
    default=[]
)

if emojis_selecionados:
    st.subheader("Filmes Recomendados:")
    
    emojis_string = "".join(emojis_selecionados)

    # Corrigido: a chamada usa o nome da função e as variáveis corretas
    recomendacoes = recomendar_filmes_por_emoji(emojis_string, dados_filmes, emojis_para_genero)

    for filme in recomendacoes:
        st.write(f"- {filme}")
else:
    st.info("Selecione pelo menos um emoji para ver as recomendações.")