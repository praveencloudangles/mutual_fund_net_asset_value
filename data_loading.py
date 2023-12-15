print("data loading---------------")
import pandas as pd

def data_loading():

    df = pd.read_csv("mutual_funds_data.csv")
    return df
data_loading()