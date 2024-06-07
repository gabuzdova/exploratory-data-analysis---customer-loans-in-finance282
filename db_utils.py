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
class RDSDatabaseConnector:
    def __init__(self, load_credentials):
        self.loadcredentials = load_credentials
#Function that loads credentials:    
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
            return(df)
    
    def save_table_local(self):
            sql_query= pd.read_sql_table('loan_payments', (self.initialisesqlalchemy()))
            df=pd.DataFrame(sql_query)
            df.to_csv("local.csv")
    
    def load_data_from_local_machine(self):
            import pandas as pd
            local_database = pd.read_csv(r"/home/zuzana/Desktop/AICORE/AICORE/EXPLORATORY DATA ANALYSIS CUSTOMER LOANS IN FINANCE/local.csv")
            df = pd.DataFrame(local_database)
            return(df)

#Class that converts columns to right datatype:
class DataTransform :
        def __init__(self, datas):
            self.datas = datas
        def convert_column_to_string(self, name_of_column):
            self.datas[name_of_column] = self.datas[name_of_column].astype('string')
            return(self.datas[name_of_column])
        def convert_column_to_datetime(self, name_of_column):
            self.datas[name_of_column] = self.datas[name_of_column].apply(parse)
            return self.datas[name_of_column]
        def convert_column_to_integer(self, name_of_column):
            self.datas[name_of_column] = self.datas[name_of_column].astype('int64')
            return(self.datas[name_of_column])
        def convert_column_to_float(self, name_of_column):
            self.datas[name_of_column] = self.datas[name_of_column].astype('float64')
            return(self.datas[name_of_column])


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
class DataFrameInfo : 
    def __init__(self, dataframe):
        self.dataframe = dataframe
    def check_columns_data_types(self):
         return (self.dataframe.dtypes)
    def extract_statistics(self):
        return self.dataframe.describe()
    def count_distinct_values(self):
        return self.dataframe.select_dtypes(include='object').nunique()
    def shape_of_the_tale(self):
        return self.dataframe.shape
    def count_of_null_values(self):
        return self.dataframe.isnull().sum()
    def percentage_of_null_values(self):
        null_counts = self.dataframe.isnull().sum()
        total_rows = len(self.dataframe)
        return (null_counts / total_rows) * 100
    def count_of_value_types(self):
         return self.dataframe.dtypes.value_counts()
    def count_of_values_in_column(self, column_name):
         return self.dataframe[column_name].value_counts()
dataframeinfo = DataFrameInfo(data)
#print(dataframeinfo.percentage_of_null_values())
# plotter class to visualise insight from the data:
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