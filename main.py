import pandas as pd
import numpy as np

#loading the dataset
df=pd.read_csv('/Users/vandana/Desktop/steam-200k.csv')

#basic info about dataset
print('dataset info: ')
print(df.info())

#print first 5 rows
print(df.head())

#check for missing values
print('\nMissing Value count:')
print(df.isnull().sum())

# Percentage of missing values
print("\nPercentage of Missing Values:")
print((df.isnull().sum() / len(df)) * 100)

#count duplicate rows
duplicate_rows=df.duplicated().sum()
print(f'total duplicate rows: {duplicate_rows}')

if duplicate_rows>0:
    print('Duplicate rows are:\n')
    print(df[df.duplicated()])