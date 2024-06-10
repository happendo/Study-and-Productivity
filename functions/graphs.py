import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import dataFunctions as df

def boxPlotGraph(data, row, labelY): ## MIssing
    sns.set_style("darkgrid")
    sns.set_theme("paper")
    fig, ax = plt.subplots()
    graph = sns.boxplot(data, y=row, ax=ax)
    graph.set_ylabel(labelY)
    st.pyplot(fig)
    plt.close(fig)

def histogramGraph(data, row, labelX, labelY, rotation=0):
    def sturges_rule(data):
        bn = 1 + (3.322 * np.log10(data.size))
        return round(bn)

    sns.set_style("darkgrid")
    sns.set_theme("paper")
    fig, ax = plt.subplots()
    graph = sns.histplot(data, x=row, binwidth=sturges_rule(data=data))
    graph.set_xlabel(labelX)
    graph.set_ylabel(labelY)
    graph.tick_params(axis='x', rotation=rotation)
    st.pyplot(fig)
    plt.close(fig)

def pieGraph(data, legendTitle): # data assume a contagem aqui.
    sns.set_theme("paper")
    fig, ax = plt.subplots()
    _, _, autotexts = ax.pie(data["data"], labels=None, autopct='%1.1f%%', startangle=90, shadow=True)

    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(9)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    ax.legend(data[legendTitle], title=legendTitle, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)
    plt.close(fig)

def barGraph(data, row, column, side="v"):
    sns.set_style("darkgrid")
    sns.set_theme("paper")
    fig, ax = plt.subplots()
    graph = sns.barplot(data=data, x=row, y=column, orient=side)
    st.pyplot(fig)
    plt.close(fig)

def dispersionGraph(data, row, column, hideTitles=False):
    sns.set_style("darkgrid")
    sns.set_theme("paper")
    fig, ax = plt.subplots()
    graph = sns.scatterplot(data=data, x=row, y=column)
    if hideTitles == True: ax.set_xlabel(""); ax.set_ylabel("")
    st.pyplot(fig)
    plt.close(fig)

def dispersionMapGraph(data, column):
    st.map(df.getLocator(data[column]))
