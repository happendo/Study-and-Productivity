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

st.write("### Idade dos Integrantes da População")

ctt.doThatBaby(data, "Qual sua idade?", labelX="Anos", labelF="Anos", graphType="boxPlotGraph", variableType="Quantitativo",labelG=1,key=0)

st.write("### Horas de dedicação diária aos estudos individuais")
ctt.doThatBaby(data, "Em média, quantas horas por dia você dedica aos estudos individuais?", labelX="Horas", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key =1)

st.write("### Em que são baseadas as escolhas dos métodos de estudo adotados")
ctt.doThatBaby(data, "Quando você vai definir seus métodos de estudo, como você faz essa escolha?", labelX="Métodos", labelY="data", labelZ="Métodos:", graphType="pieGraph", variableType="Qualitativo", key=2)

st.write("### Métodos de estudo considerados eficazes para o aprendizado")
ctt.doThatBaby(data, "Quais métodos de estudo você considera mais eficaz para o seu aprendizado?", labelX="Métodos",labelZ="h", graphType="barGraph", variableType="Qualitativo", key=3)

st.write("### Como são testados os métodos de estudos descobertos")
ctt.doThatBaby(data, "Quando você encontra um novo método de estudo, como decide testá-lo?", labelX="Testes",labelZ="h", graphType="barGraph", variableType="Qualitativo", key=4)

st.write("### Como é identificada a eficácia de um método de estudo utilizado")
ctt.doThatBaby(data, "Como você identifica se um método de estudo está funcionando para você?", labelX="Métodos", labelY="data", labelZ="Métodos:", graphType="pieGraph", variableType="Qualitativo", key=5)

st.write("### Frequência de revisões dos materiais estudados")
ctt.doThatBaby(data, "Com que frequência você revisa o material estudado?", labelX="Frequência", graphType="histogramGraph", labelZ=30,variableType="Qualitativo", labelG=1, key=6)

st.write("### Métodos favoritos de revisão e consolidação do conhecimento adquirido.")
ctt.doThatBaby(data, "Qual é o seu método preferido para revisar e consolidar o conhecimento adquirido durante os estudos?", labelX="Métodos", labelZ="v", graphType="barGraph", variableType="Qualitativo", key=7)

