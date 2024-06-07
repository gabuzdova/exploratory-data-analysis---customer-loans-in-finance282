#Importing modules:
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
#Creating class that connects database I will be working on:


#Class that converts columns to right datatype:


cred = (r"/home/zuzana/Desktop/exploratory-data-analysis---customer-loans-in-finance282/.git/credentials.yaml")
c = RDSDatabaseConnector(cred)
c.extract_data_as_dataframe()
d = RDSDatabaseConnector(cred)
data = d.load_data_from_local_machine()
testclass = DataTransform(data)

testclass.convert_column_to_datetime("issue_date")
testclass.convert_column_to_string("grade")
testclass.convert_column_to_string("home_ownership")
testclass.convert_column_to_string("verification_status")
testclass.convert_column_to_string("payment_plan")
testclass.convert_column_to_string("purpose")
testclass.convert_column_to_string("application_type")
testclass.convert_column_to_datetime("earliest_credit_line")
#Class that gives dataframe informations:

dataframeinfo = DataFrameInfo(data)
#print(dataframeinfo.percentage_of_null_values())
# plotter class to visualise insight from the data:


      
graphs = Plotter(data)    
#print(graphs.bar_chart("term", "funded_amount"))        

class DataFrameTransform :
    def __init__(self, dataframe):
          self.dataframe = dataframe

    def drop_whole_column(self, column_name):
        self.dataframe = self.dataframe.drop(columns = column_name, axis = 1, inplace = True)
        return self.dataframe
    def imput_median_for_nan(self, column_name):
        self.dataframe = self.dataframe[column_name].fillna(self.dataframe[column_name].median())
        return self.dataframe
    def imput_mean_for_nan(self, column_name):
        self.dataframe = self.dataframe[column_name].fillna(self.dataframe[column_name].mean())
        return self.dataframe
    def imput_mode_for_nan(self, column_name):
        self.dataframe = self.dataframe[column_name].fillna(self.dataframe[column_name].mode())
        return self.dataframe
dataframetransform = DataFrameTransform(data)
dataframetransform.drop_whole_column(["mths_since_last_delinq","next_payment_date","mths_since_last_major_derog", "mths_since_last_record"])
#print(dataframeinfo.percentage_of_null_values())
#print(data["instalment"].head ())
#graphs.scatter_plots("loan_amount", "term" )
#print(data["funded_amount"].tail())
#print(data["funded_amount_inv"].tail())
#print(data["last_payment_date"].isna())
#print(dataframeinfo.percentage_of_null_values())
#dataframetransform.imput_median_for_nan("employment_length")
data.dropna(subset= ["last_credit_pull_date"], how = "all",axis = 0, inplace = True)
data.dropna(subset=["collections_12_mths_ex_med"], how="all", axis= 0, inplace = True )
data.dropna(subset=["last_payment_date"], how="all", axis= 0, inplace = True )
#print(dataframeinfo.percentage_of_null_values())
#print(dataframeinfo.count_of_values_in_column("employment_length"))
#dataframetransform.imput_median_for_nan(data["employment_length"].median())
#print(data["employment_length"].mean())
#print(data["employment_length"].mode())
#data["employment_length"]=data["employment_length"].fillna(data["employment_length"].median())
#print(data["employment_length"].info())
#print(dataframeinfo.percentage_of_null_values())
print(data.info())