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

st.write("### Frequência de prática de atividade física")
ctt.doThatBaby(data, "Com que frequência você pratica atividade física?", labelX="Dias", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=0)

st.write("### Tipo de atividade física praticada")
ctt.doThatBaby(data, "Qual é o tipo de atividade física que você costuma praticar?", labelX="Tipos", labelY="data", labelZ="Tipos:", graphType="pieGraph", variableType="Qualitativo", key=1)

st.write("### Equilíbrio do tempo entre atividade física e os estudos")
ctt.doThatBaby(data, "Como você equilibra seu tempo entre atividade física e estudos?", labelX="Métodos", labelY="data", labelZ="Métodos:", graphType="pieGraph", variableType="Qualitativo", key=2)

st.write('### Escala de Impacto da prática regular de atividade física na saúde mental relativo aos estudos')
ctt.doThatBaby(data, 'Em uma escala de 1 a 5, onde 1 representa "Nenhum impacto" e 5 representa "Grande impacto", como você avaliaria o impacto da prática regular de atividade física na sua saúde mental em relação aos estudos?', labelX="Escala de Impacto",labelF="Escala de Impacto",labelZ="v", graphType="barGraph", variableType="Quantitativo", labelG=1, key=3)

st.write("### Frequência de procrastinação em relação às tarefas de estudo")
ctt.doThatBaby(data, "Com que frequência você procrastina quando se trata de realizar tarefas de estudo?", labelX="Frequência", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=4)

st.write("### Motivos que levam à procrastinação das tarefas de estudo")
ctt.doThatBaby(data, "Qual o principal motivo que leva você a procrastinar as tarefas de estudo?", labelX="Motivos", labelY="data", labelZ="Motivos:", graphType="pieGraph", variableType="Qualitativo", key=5)

st.write("### Impacto da procrastinação no desempenho acadêmico")
ctt.doThatBaby(data, 'Como a procrastinação afeta seu desempenho acadêmico?', labelX="Motivos", labelZ="h", graphType="barGraph", variableType="Qualitativo", key=6)

st.write('### Escala de Impacto da procrastinação na satisfação pessoal com seus hábitos de estudo')
ctt.doThatBaby(data, 'Em uma escala de 1 a 5, onde 1 representa "Nenhum impacto" e 5 representa "Grande impacto", como você avaliaria o impacto da procrastinação na sua satisfação pessoal com seus hábitos de estudo?', labelX="Escala de Impacto",labelF="Escala de Impacto",labelZ="v", graphType="barGraph", variableType="Quantitativo", labelG=1, key=7)

st.write("### Principal forma de entretenimento diário")
ctt.doThatBaby(data, 'Qual sua principal forma de entretenimento diário?', labelX="Métodos", labelZ="h", graphType="barGraph", variableType="Qualitativo", key=8)

st.write("### Tempo de dedicação a atividades de entretenimento")
ctt.doThatBaby(data, "Quanto tempo médio do seu dia você dedica a atividades de entretenimento, como assistir a filmes, séries, Jogos ou utilizar redes sociais?", labelX="Horas", graphType="histogramGraph", variableType="Qualitativo", labelG=1, key=9)

st.write('### Escala de Impacto do entretenimento diário nos estudos')
ctt.doThatBaby(data, 'Em uma escala de 1 a 5, onde 1 representa "Nenhum impacto" e 5 representa "Grande impacto", como você avaliaria o impacto da procrastinação na sua satisfação pessoal com seus hábitos de estudo?', labelX="Escala de Impacto",labelF="Escala de Impacto",labelZ="v", graphType="barGraph", variableType="Quantitativo", labelG=1, key=10)

st.write("### Frequência regular de estudos")
ctt.doThatBaby(data, "Com que frequência você estuda regularmente?", labelX="Frequência", graphType="histogramGraph", labelZ=25,variableType="Qualitativo", labelG=1, key=11)