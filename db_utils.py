from dateutil.parser import parse
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import yaml
#class RDSDatabaseConnector:
 #   def __init(self):
def loadcredentials():
            import yaml
            from yaml.loader import SafeLoader
            with open(r"/home/zuzana/Desktop/AICORE/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/credentials.yaml") as credentialsfile:
                data = yaml.load(credentialsfile, Loader=SafeLoader)
                return(data)
def initialisesqlalchemy():

            hst=(list(loadcredentials().values())[0])
            pswd=(list(loadcredentials().values())[1])
            usr=(list(loadcredentials().values())[2])
            dtbs=(list(loadcredentials().values())[3])
            prt=(list(loadcredentials().values())[4])
            DATABASE_TYPE= "postgresql"
            DBAPI="psycopg2"
            USER=usr
            PASSWORD=pswd
            PORT=prt
            DATABASE=dtbs
            ENDPOINT=hst
            engine= create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
            return engine
def extract_data_as_dataframe():
            sql_data= pd.read_sql_table('loan_payments', initialisesqlalchemy())
            df=pd.DataFrame(sql_data)
            return df
def save_table_local():
            sql_query= pd.read_sql_table('loan_payments', (initialisesqlalchemy()))
            df=pd.DataFrame(sql_query)
            df.to_csv("local.csv")
def load_data_from_local_machine():
            local_database = pd.read_csv(r"/home/zuzana/Desktop/AICORE/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/local.csv")
            df = pd.DataFrame(local_database)
            return(df)
data = load_data_from_local_machine()
data.grade = data.grade.astype('string') 
data.home_ownership = data.home_ownership.astype('string') 
data.verification_status = data.verification_status.astype('string')
data.payment_plan = data.payment_plan.astype('string') 
data.purpose = data.purpose.astype('string') 
data.application_type = data.application_type.astype('string') 
data['issue_date'] = data['issue_date'].apply(parse)
data['earliest_credit_line'] = data['earliest_credit_line'].apply(parse)

print(data.head())