import numpy as np
import pandas as pd

def media(data):
    return data.mean()

def mediana(data, variableType):
    if variableType == "Quantitativo":
        mediana = data.median()
    elif variableType == "Qualitativo":
        mediana = data.iloc[len(data) // 2]
    return mediana

def moda(data):
    return data.mode()

def variancia(data):
    return data.var()

def desvMedio(data):
    return np.abs(data - data.mean()).mean()

def desvPadrao(data):
    return data.std()

def quartil(data, q=0.25): #coloquei um valor padrão de q1 para essa função
    return data.quantile(q) 

def distInterQ(data):
    Qum = quantil(data,q=0.25)
    Qtres = quantil(data,q=0.75)
    return Qtres - Qum