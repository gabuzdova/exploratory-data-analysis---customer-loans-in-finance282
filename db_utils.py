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
import yaml
from yaml.loader import SafeLoader


#Creating class that connects database I will be working on:
class RDSDatabaseConnector:
    def __init__(self, load_credentials):
        self.loadcredentials = self.load_credentials()
#Function that loads credentials:    
    def load_credentials(self):
        with open(self.loadcredentials) as credentialsfile:
            data = yaml.load(credentialsfile, Loader=SafeLoader)
        return(data)
                
    
    def initialisesqlalchemy(self):
                hst=(list(self.load_credentials().values())[0])
                pswd=(list(self.load_credentials().values())[1])
                usr=(list(self.load_credentials().values())[2])
                dtbs=(list(self.load_credentials().values())[3])
                prt=(list(self.load_credentials().values())[4])
                DATABASE_TYPE= "postgresql"
                DBAPI="psycopg2"
                USER=usr
                PASSWORD=pswd
                PORT=prt
                DATABASE=dtbs
                ENDPOINT=hst
                engine= create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
                return engine
    
    def extract_data_as_dataframe(self):
            sql_data= pd.read_sql_table('loan_payments', self.initialisesqlalchemy())
            df=pd.DataFrame(sql_data)
            return(df)
    
    def save_table_local(self):
            sql_query= pd.read_sql_table('loan_payments', (self.initialisesqlalchemy()))
            df=pd.DataFrame(sql_query)
            df.to_csv("local.csv")
    
    def load_data_from_local_machine(self):
            local_database = pd.read_csv(r"/home/zuzana/Desktop/AICORE/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/local.csv")
            df = pd.DataFrame(local_database)
            return(df)

#Class that converts columns to right datatype:
if __name__ == "__main__":
       e = RDSDatabaseConnector()