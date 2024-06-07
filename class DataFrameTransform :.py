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