import numpy as np 
import pandas as pd
from scipy.stats import chisquare
import dataFunctions as df
import streamlit as st
import estatistica as stc

#Variável Quantitativa + Quantitativa
def covariancia(varx, vary):
    return varx.cov(vary)

# def covTeste(varx, vary):
#     if varx.index[-1] != vary.index[-1]:
#         return False
#     else:
#         ola = 0
#         olaMediaX = 0
#         olaMediaY = 0
#         for i in varx:
#             for t in vary:
#                 ola += i*t
#                 olaMediaX += i
#                 olaMediaY += t
#         numero = varx.index[-1]+1
#         olaMediaX = olaMediaX/numero
#         olaMediaY = olaMediaY/numero
#         total = ola/numero - olaMediaX*olaMediaY

#         print(total)
#         return total

def Pearson_Coef(vary, varx):
    return varx.corr(vary, method='pearson')

#Variável Quanlitativa + Quanlitativa
def qui_quadrado(varx,vary):
    frequency_matrix = pd.crosstab(varx, vary)
    def expected_matrix():
        #sum of columns and rows
        columns_sum = np.array([frequency_matrix[x].sum() for x in frequency_matrix.columns])
        rows_sum = np.array([frequency_matrix.loc[y].sum() for y in frequency_matrix.index.tolist()])
        total_sum = (frequency_matrix.sum()).sum()
        #Generate the matrix of expected values
        expects_matrix = np.zeros_like(frequency_matrix, dtype=float)
        for i in range(frequency_matrix.shape[0]):
            for j in range(frequency_matrix.shape[1]):
                expects_matrix[i, j] = (rows_sum[i] * columns_sum[j]) / total_sum
        return expects_matrix
    
    #quisquare calculus
    qui_quad = (((frequency_matrix - expected_matrix())**2) / expected_matrix()).sum().sum()
    return qui_quad

def contingency_table(varx, vary):
    frequency_matrix = pd.crosstab(varx, vary)
    frequency_matrix.rename(columns={})
    return frequency_matrix

def contingemcy_coeficient(varx, vary):
    frequency_matrix = pd.crosstab(varx, vary)
    total_sum = frequency_matrix.sum().sum()
    qui = qui_quadrado(varx,vary)
    cont_coef = np.sqrt(qui / (qui + total_sum))
    return cont_coef

#Variável Quanlitativa + Quantitativa
def rsquare(varx, vary):
    datain= pd.crosstab(vary, columns=varx)
    print(datain)
    total_sum = datain.sum()

    def variancia(datain):
        var = np.sum(((datain - datain.mean()))**2)/(total_sum - 1)
        return var
        
    def pondvariancia(varx, vary):
        cols = [varx[i] for i in varx]
        res = np.zeros_like(varx, dtype=float)
        for j in cols:
            tot = j.sum()
            pond = (tot * variancia(j))/(tot)
            np.append(res, pond)
            return res.sum()
    r_quad = 1 - pondvariancia(varx,vary)/variancia(varx)
    return r_quad