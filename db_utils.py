import yaml
import pandas as pd
#class RDSDatabaseConnector:
 #   def __init(self, loadcredentials)
def loadcredentials():
    import yaml
    from yaml.loader import SafeLoader
    with open(r"/home/zuzana/Desktop/AICORE kurz/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/credentials.yaml") as credentialsfile:
        data = yaml.load(credentialsfile, Loader=SafeLoader)
        return(data)
def initialisesqlalchemy():
    import psycopg2
    import sqlalchemy
    from sqlalchemy import create_engine

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
initialisesqlalchemy()
