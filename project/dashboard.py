import streamlit as st
from tinydb import TinyDB
import pandas as pd
import plotly.express as px
from datetime import datetime
from analise_ia import gerar_analise_cripto  # Função com Agente IA

# Função para carregar dados do TinyDB


def carregar_dados():
    db = TinyDB("db.json")  # Altere para "../db.json" se necessário
    dados = db.all()
    return dados

# Função para preparar os dados para o dashboard


def preparar_dados(dados):
    df = pd.DataFrame(dados)
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    return df


# Configuração da página
st.set_page_config(page_title="Dashboard Cripto", layout="wide")
st.title("📊 Dashboard de Cotação de Criptomoeda (Coinbase API)")

# Carregamento dos dados
dados = carregar_dados()

if not dados:
    st.warning("Ainda não há dados disponíveis.")
else:
    df = preparar_dados(dados)

    # Extrair os últimos 10 dados para análise da IA
    df_ultimos = df.tail(10)[["timestamp", "valor"]].copy()
    df_ultimos["timestamp"] = df_ultimos["timestamp"].dt.strftime(
        "%Y-%m-%d %H:%M:%S")
    tabela_para_ia = df_ultimos.to_string(index=False)

    # Mostrar métricas principais
    ultima_linha = df.iloc[-1]
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Valor Atual",
                f"{ultima_linha['valor']} {ultima_linha['moeda']}")
    col2.metric("🪙 Criptomoeda", ultima_linha["criptomoeda"])
    col3.metric("⏱️ Última Atualização",
                ultima_linha["timestamp"].strftime("%H:%M:%S"))

    # Gráfico de linha
    fig = px.line(df, x="timestamp", y="valor",
                  title="Histórico da Cotação", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # Dados brutos expandidos
    with st.expander("📄 Ver dados brutos"):
        st.dataframe(df)

    # Análise de IA com base nos dados
    # Análise de IA com botão para gerar
st.markdown("---")
st.subheader("🧠 Análise de IA com base nos dados reais")

if st.button("🔄 Gerar nova análise com IA"):
    with st.spinner("IA está analisando os dados..."):
        try:
            analise = gerar_analise_cripto(tabela_para_ia)
            st.markdown(analise)
        except Exception as e:
            st.error(f"Erro ao gerar análise com IA: {e}")
else:
    st.info("Clique no botão acima para gerar uma análise com IA com base nos dados mais recentes.")
