import pandas as pd
import estatistica as stc
from geopy.geocoders import Nominatim
import time
import streamlit as st
import graphs as gp
import bidimensionalanalysis as bda
import os

def setData(diretorio=str(os.path.dirname(os.path.abspath(__file__)))[:-9] + "/data/Pesquisa.csv"):
    return pd.read_csv(diretorio)

def separeData(data): # Inserir dados da coluna
    treatedData = []
    for i in data:
        if isinstance(i, int):
            i = str(i)
            for i, parte in enumerate(i.split(';')):
                treatedData.append(int(parte.strip()))
        elif isinstance(i, str):
            for i, parte in enumerate(i.split(';')):
                treatedData.append(parte.strip())
    return pd.DataFrame(data=treatedData)

def countFrequency(data, labelX, labelY="Frequência Absoluta", labelZ="Frequência Relativa"):
    counter = data.value_counts() # value_counts() para contar as ocorrências de cada elemento na coluna do DataFrame
    typeFreq = [item[0] for item in counter.index.to_list()]
    countedFrequency = counter.values.tolist() # Criar a lista com a contagem de ocorrências de cada elemento
    data = pd.DataFrame({  str(labelX): typeFreq,
                                str(labelY): countedFrequency })
    if labelZ != None:
        totalData = data[labelY].sum()
        onePercentData = 100/totalData
        data[labelZ] = [round(i*onePercentData/100,2) for i in data[labelY]]

    return data

def sumData(data, drop=None, axis=0):
    dataTotal = pd.DataFrame(data.sum(numeric_only=True)).T
    if None not in drop:
        for i in drop:
            dataTotal.drop(i, axis=axis, inplace=True)
    finalData = pd.concat([data, dataTotal], ignore_index=True)
    finalData = finalData.rename(index={len(finalData) - 1: "Total"})
    return finalData

def getPositionS(data, variableType, labelA="Média", labelB="Mediana", labelC="Moda"):
    if variableType == "Quantitativo":
        finalData = pd.DataFrame(
        { labelA: stc.media(data), labelB: stc.mediana(data, variableType=variableType), labelC: stc.moda(data) })
    elif variableType == "Qualitativo":
        finalData = pd.DataFrame(
        { labelA: None, labelB: stc.mediana(data, variableType=variableType), labelC: stc.moda(data) })
    return finalData.round(2)

def getDispersionS(data, labelA="Desvio Médio", labelB="Desvio Padrão", labelC="Variância"):
    finalData = pd.DataFrame(
        { labelA: stc.desvMedio(data), labelB: stc.desvPadrao(data), labelC: stc.variancia(data)})
    return finalData.round(2)

def getLocator(data):
    coords = [[],[]]
    for i in data:
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(i, timeout=None)
        coords[0].append(location.latitude); coords[1].append(location.longitude)
        time.sleep(1.0)
    locData = pd.DataFrame({"Cidades": data, "latitude": coords[0], "longitude": coords[1], "size": data.count()})
    return locData

def quantiQuantiAnalysis(data, row, column):
    separeData(data[row]); separeData(data[column])
    analyzedData = pd.DataFrame({"Covariância": bda.covariancia(data[row], data[column]), "Coeficiente de Pearson": bda.Pearson_Coef(data[row], data[column])}, index=[0])
    return analyzedData

def qualiQualiAnalysis(data, row, column):
    separeData(data[row]); separeData(data[column])
    analyzedData = pd.DataFrame({"qui²": bda.qui_quadrado(data[row], data[column]), "Coeficiente de Contigência": bda.contingemcy_coeficient(data[row], data[column])}, index=[0])
    st.dataframe(bda.contingency_table(data[row],data[column]), use_container_width=True)
    return analyzedData

def quantiQualiAnalysis(data, row, column, variableType):
    separeData(data[row]); separeData(data[column])
    analyzedData = pd.DataFrame({"r²": bda.rsquare(data[row], data[column])}, index=[0])
    return analyzedData
