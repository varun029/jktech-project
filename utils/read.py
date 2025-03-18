import pandas as pd

def read_file(path):
    df=pd.read_csv(path)
    print(df.dtypes)
    print(df.head())
    print('\n')
    return df