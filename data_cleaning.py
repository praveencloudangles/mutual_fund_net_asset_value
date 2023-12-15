from data_analysis import data_analysis

def data_cleaning():
    data = data_analysis()
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    return data

data_cleaning()