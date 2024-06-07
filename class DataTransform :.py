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
        def remove_unwanted_text(self, name_of_column):
            self.datas[name_of_column]= self.datas[name_of_column].replace("[A-Za-z+<]", "", regex = True)
            return(self.datas[name_of_column])