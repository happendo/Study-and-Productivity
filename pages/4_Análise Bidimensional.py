import sys, os
sys.path.append(str(os.path.dirname(os.path.abspath(__file__)))[:-5])
sys.path.append("functions")
sys.path.append("data")

import graphs as gp
import dataFunctions as df
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import theconstrutor as ctt

data = df.setData()

st.write("### Selecione duas variáveis:")
col1, col2 = st.columns(2)
with col1:
    firstVariable = st.selectbox("1º variável:", [item for item in data if item != "Insira seu código aqui:"], key=0)
    firstVariableType = st.selectbox("Tipo da 1º variável", ["Quantitativo", "Qualitativo"])
with col2:
    secondVariable = st.selectbox("2º variável:", [item for item in data if item != "Insira seu código aqui:"], key=1)
    secondVariableType = st.selectbox("Tipo da 2º variável", ["Quantitativo", "Qualitativo"])

if st.button('Aplicar'):
    st.write("### Gráfico:")
    gp.dispersionGraph(data, row=firstVariable, column=secondVariable, hideTitles=True)
    st.write("### Estatísticas:")
    if firstVariableType == "Quantitativo" and secondVariableType == "Quantitativo":
        st.dataframe(df.quantiQuantiAnalysis(data, firstVariable, secondVariable), use_container_width=True, hide_index=True)
    elif firstVariableType == "Qualitativo" and secondVariableType == "Qualitativo":
        st.dataframe(df.qualiQualiAnalysis(data, firstVariable, secondVariable), use_container_width=True, hide_index=True)
    elif (firstVariableType == "Qualitativo" and secondVariableType == "Quantitativo") or (firstVariableType == "Quantitativo" and secondVariableType == "Qualitativo"):
        st.dataframe(df.quantiQualiAnalysis(data, firstVariable, secondVariable, firstVariableType), use_container_width=True, hide_index=True)
        st.write("## Ainda não há tabelas para esse tipo de associação.")