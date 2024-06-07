import pandas as pd
import numpy as np
import dataFunctions as df
import graphs as gp
import streamlit as st

def doThatBaby(data, column, labelX, graphType, key, variableType, labelG=None,labelF=None,labelY=None, labelZ=None, statistics=True):
    
    if statistics == True:
        if variableType == "Quantitativo":
            textOption = 'Medidas de Frequência, Posição e Dispersão'
        else:
            textOption = 'Medidas de Frequência e Posição'
        selected_option = st.selectbox("Selecione uma opção:", ['Gráfico', textOption], key=key)
        if selected_option == 'Gráfico':
            if graphType == "boxPlotGraph":
                gp.boxPlotGraph(data, row=column, labelY=labelY)
            elif graphType == "histogramGraph":
                gp.histogramGraph(data, column, labelX=labelX, labelY=labelY, rotation=labelZ)
            elif graphType == "pieGraph":
                gp.pieGraph(df.countFrequency(df.separeData(data[column]), labelX=labelZ, labelY=labelY, labelZ=None), labelZ)
            elif graphType == "barGraph":
                if labelZ == "v":
                    gp.barGraph(df.countFrequency(df.separeData(data[column]), labelX=labelX), row=labelX, column="Frequência Absoluta", side=labelZ)
                elif labelZ == "h":
                    gp.barGraph(df.countFrequency(df.separeData(data[column]), labelX=labelX), row="Frequência Absoluta", column=labelX, side=labelZ)
            elif graphType == "dispersionGraph":
                gp.dispersionGraph(data, row=labelX, column=labelY)
            elif graphType == "mapGraph":
                gp.dispersionMapGraph(data=data, column=column)
        elif selected_option == textOption:
            st.dataframe(df.sumData(df.countFrequency(df.separeData(data[column]), labelX=labelX), drop=[labelF], axis=labelG), use_container_width=True)
            if variableType == "Quantitativo":
                col1, col2 = st.columns(2)
                with col1:
                    st.dataframe(df.getPositionS(data[column], variableType="Quantitativo"), use_container_width=True, hide_index=True)
                with col2:
                    st.dataframe(df.getDispersionS(df.separeData(data[column])), use_container_width=True, hide_index=True)
            elif variableType == "Qualitativo":
                st.dataframe(df.getPositionS(data[column], variableType="Qualitativo",), use_container_width=True, hide_index=True)
    elif statistics == False:
        if graphType == "boxPlotGraph":
                gp.boxPlotGraph(data, row=column, labelY=labelY)
        elif graphType == "histogramGraph":
            gp.histogramGraph(data, column, labelX=labelX, labelY=labelY)
        elif graphType == "pieGraph":
            gp.pieGraph(df.countFrequency(df.separeData(data[column]), labelX=labelZ, labelY=labelY, labelZ=None), labelZ)
        elif graphType == "barGraph":
            if labelZ == "v":
                gp.barGraph(df.countFrequency(df.separeData(data[column]), labelX=labelX), row=labelX, column="Frequência Absoluta", side=labelZ)
            elif labelZ == "h":
                gp.barGraph(df.countFrequency(df.separeData(data[column]), labelX=labelX), row="Frequência Absoluta", column=labelX, side=labelZ)
        elif graphType == "dispersionGraph":
            gp.barGraph(data, row=labelX, column=labelY)