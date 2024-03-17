from dateutil.parser import parse
import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import yaml
class RDSDatabaseConnector:
    def __init__(self, load_credentials):
        self.loadcredentials = load_credentials
    
    def load_credentials(self):
        import yaml
        from yaml.loader import SafeLoader
        with open(self.loadcredentials) as credentialsfile:
            data = yaml.load(credentialsfile, Loader=SafeLoader)
        return(data)
                
    
    def initialisesqlalchemy(self):
                import psycopg2
                import sqlalchemy
                from sqlalchemy import create_engine
                import pandas as pd
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
            print(df)
    
    def save_table_local(self):
            sql_query= pd.read_sql_table('loan_payments', (self.initialisesqlalchemy()))
            df=pd.DataFrame(sql_query)
            df.to_csv("local.csv")
    
    def load_data_from_local_machine(self):
            import pandas as pd
            local_database = pd.read_csv(r"/home/zuzana/Desktop/AICORE/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/local.csv")
            df = pd.DataFrame(local_database)
            return(df)

"""data = load_data_from_local_machine()
data.grade = data.grade.astype('string') 
data.home_ownership = data.home_ownership.astype('string') 
data.verification_status = data.verification_status.astype('string')
data.payment_plan = data.payment_plan.astype('string') 
data.purpose = data.purpose.astype('string') 
data.application_type = data.application_type.astype('string') 
data['issue_date'] = data['issue_date'].apply(parse)
data['earliest_credit_line'] = data['earliest_credit_line'].apply(parse)

print(data.head())"""
cred = (r"/home/zuzana/Desktop/exploratory-data-analysis---customer-loans-in-finance282/.git/credentials.yaml")
c = RDSDatabaseConnector(cred)
c.extract_data_as_dataframe()