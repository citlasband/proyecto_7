import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Histograma y Diagrama de dispersión")

car_data= pd.read_csv("vehicles_us.csv")  # leer los datos

hist_button = st.button('Histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches') 
    # crear un histograma
    fig = px.histogram(car_data, x="type")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Diagrama de dispersión')  # crear un botón

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    disp = px.scatter(car_data, x="type", y="model")
    # mostrar el gráfico de dispersión
    st.plotly_chart(disp, use_container_width=True) 
    