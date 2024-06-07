import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
from dateutil.parser  import parse 


class Plotter :
    def __init__(self, df):
        self.df = df
    def histogram(self, column_name, bins_num):
        data.hist(column_name, bins = bins_num)
        return(plt.show())
    def density_plot(self, column_name):
        sns.histplot(data, x= column_name, kde =True)
        sns.despine()
        plt.show()
    def box_and_whiskers(self, column_name):
        fig = px.box(data, y= column_name, width = 800, height = 1000)
        return(fig.show())
    def violin_plot(self, column_name):
        sns.violinplot( data, y = column_name)
        sns.despine()
        plt.show()
    def discrete_prob_distribution(self, column_name):
        plt.rc("axes.spines", top=False, right=False)
        probs = data[column_name].value_counts(normalize=True)
        dpd=sns.barplot(y=probs.index, x=probs.values, color='b')
        plt.xlabel('Values')
        plt.ylabel('Probability')
        plt.title('Discrete Probability Distribution')
        return(plt.show())
    def pie_chart(self, column_name ):
        df = data[column_name].value_counts()
        fig = px.pie(values=df.values, names=df.index, title='Pie Chart of Loan Purpose', width=600)
        return(fig.show())
    def cumulative_density_function(self, column_name, column_name_1):
        sns.histplot(data[column_name], cumulative=True, stat='density', element="poly")
        plt.title('Cumulative Distribution Function (CDF)')
        plt.xlabel('column_name_1')
        plt.ylabel('Cumulative Probability')
        return(plt.show())
    def scatter_plots(self, column_name, column_name_1):
        sns.scatterplot(data, x=column_name, y=column_name_1)
        return(plt.show())
    def bar_chart(self, column_name, column_name_1):
        sns.barplot(data, y=column_name, x=column_name_1)
        return(plt.show())
    def pair_plots(self):
        sns.pairplot(data)
        return(plt.show())