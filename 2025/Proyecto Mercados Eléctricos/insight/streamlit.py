
# Código para ir construyendo el streamlit


"""
# Probando streamlit


"""

import streamlit as st
import pandas as pd

st.title("Probando streamlit")
st.write("Hola, este es un ejemplo de Streamlit")
st.write("Podemos mostrar dataframes:")
df = pd.DataFrame({
    'Columna 1': [1, 2, 3, 4],
    'Columna 2': ['A', 'B', 'C', 'D']
})
st.dataframe(df)