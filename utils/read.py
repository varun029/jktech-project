import pandas as pd

def read_file(path):
    df=pd.read_csv(path)
    print(df.dtypes)
    print('\n')
    print(df.head())
    print('\n')
    print(f'The number of rows and columns in the dataset are: {df.shape}')
    print('\n')
    return df