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