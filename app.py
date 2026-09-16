import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

st.header("Análise de anúncios de veículos")

st.write(
    "Este aplicativo permite explorar visualmente os dados "
    "de anúncios de venda de veículos."
)

hist_button = st.button("Criar histograma")

if hist_button:
    st.write(
        "Criando um histograma para o conjunto de dados de anúncios de vendas de carros")

    fig = px.histogram(
        car_data,
        x="odometer"
    )

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Relação entre quilometragem e preço")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço dos veículos por quilometragem"
    )

    st.plotly_chart(fig, use_container_width=True)
