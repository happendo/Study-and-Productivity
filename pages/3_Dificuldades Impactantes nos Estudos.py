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

st.write("### Cidade de Residência")
ctt.doThatBaby(data, "Em que cidade você mora?", labelX="Cidades", graphType="mapGraph", variableType="Qualitativo", labelG=1, key=0)

st.write("### Tempo de locomoção para ida até a universidade")
ctt.doThatBaby(data, "Quanto tempo, em média, você leva para se locomover de onde você mora até a universidade", labelX="Horas", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=1)

st.write("### Tempo de locomoção de volta pra casa da universidade")
ctt.doThatBaby(data, "Quanto tempo em média, você leva para se locomover da universidade até onde você mora?", labelX="Horas", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=2)

st.write("### Horas de sono")
ctt.doThatBaby(data, "Quantas horas de sono você costuma ter em uma noite típica?", labelX="Horas", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=3)

st.write('### Desafios encontrados para manter a consistência nos estudos')
ctt.doThatBaby(data, 'Quais são os principais desafios que você enfrenta para manter a consistência nos estudos?', labelX="Escala de Impacto", labelZ="h", graphType="barGraph", variableType="Qualitativo", key=4)

st.write('### Frequência de percepção da interferência da ansiedade na motivação para estudar')
ctt.doThatBaby(data, 'Com que frequência você percebe que a ansiedade interfere na sua motivação para estudar', labelX="Escala de Impacto",labelZ="v", graphType="barGraph", variableType="Qualitativo", key=5)

st.write("### Como a ansiedade afeta o planejamento de estudos")
ctt.doThatBaby(data, "Como a ansiedade afeta o seu planejamento de estudos?", labelX="Tipos", labelY="data", labelZ="", graphType="pieGraph", variableType="Qualitativo", key=6)

st.write("### Frequência de percepção da interferência da ansiedade na motivação para estudar")
ctt.doThatBaby(data, "Você teria interesse em participar de uma palestra sobre administração do tempo e metodologias de estudos, visando melhorar sua eficiência e produtividade acadêmica?", labelX="Tipos", labelY="data", labelZ="", graphType="pieGraph", variableType="Qualitativo", key=7)