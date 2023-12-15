from data_cleaning import data_cleaning
from sklearn.calibration import LabelEncoder

def feat_eng():
    data = data_cleaning()

    label_encoder = LabelEncoder()
    column_types = data.dtypes
    print(column_types)

    columns_to_encode = ['scheme_name', 'fund_house', 'scheme_type', 'scheme_category', 'date']
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    data.to_csv("mutual_fund_net_value.csv")

    return data

feat_eng()
