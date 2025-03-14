import pandas as pd
import numpy as np
from utils.read import read_file
from utils.missing import miss_val_column
from utils.missing import miss_val_percentage

#loading the dataset
df=read_file('/Users/vandana/Desktop/steam-200k.csv')

column_names=['user_id','game-title','behavior','value','unknown']
df.columns=column_names

#basic info about dataset
print('dataset info: ')
print(df.describe())

#print first 5 rows
print(df.head())
print('\n')

#check for missing values
missing_values=miss_val_column(df)

# Percentage of missing values
percent_missing=miss_val_percentage(df,missing_values)

#count duplicate rows
duplicate_rows=df.duplicated().sum()
print(f'total duplicate rows: {duplicate_rows}')

if duplicate_rows>0:
    print('Duplicate rows are:\n')
    print(df[df.duplicated()])

