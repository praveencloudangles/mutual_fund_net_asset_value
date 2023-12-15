print("data analysis----------------")
from data_loading import data_loading

def data_analysis():
    data = data_loading()
    print("null values----", data.isnull().sum())
    print("duplicate values----", data.duplicated().sum())
    print("describe----------", data.describe())
    print("shape of data----------", data.nunique())
    
    return data

data_analysis()
