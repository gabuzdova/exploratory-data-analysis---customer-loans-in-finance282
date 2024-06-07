#Importing modules:
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.parser  import parse 
import yaml
from yaml.loader import SafeLoader
import sys


#Creating class that connects database I will be working on:
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = self.load_credentials(credentials)
#Function that loads credentials:    
    def load_credentials(self, credentials):
        with open(credentials, "r") as credentialsfile:
            data = yaml.load(credentialsfile, Loader=SafeLoader)
        return(data)
                
    
    def initialisesqlalchemy(self):
                ENDPOINT = self.credentials["RDS_HOST"]
                PASSWORD = self.credentials["RDS_PASSWORD"]
                USER = self.credentials['RDS_USER']
                DATABASE = self.credentials['RDS_DATABASE']
                PORT= self.credentials['RDS_PORT']
                DATABASE_TYPE= "postgresql"
                DBAPI="psycopg2"
                engine= create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
                return engine.connect()
    
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
    #sys.path.append("/home/zuzana/Desktop/exploratory-data-analysis---customer-loans-in-finance282/credentials.yaml")
    db_connector = RDSDatabaseConnector("credentials.yaml")
    #print(db_connector.credentials)
    engine = db_connector.initialisesqlalchemy()
    #print(engine)
    df = (db_connector.extract_data_as_dataframe())
    #print(df)
    svtable = db_connector.save_table_local()
    #print(svtable)
    ldcred = db_connector.load_data_from_local_machine()
    print(ldcred)