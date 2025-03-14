import pandas as pd
import numpy as np
from utils.read import read_file
from utils.missing import miss_val_column
from utils.missing import miss_val_percentage
from utils.drop import drop_column

#loading the dataset
df=read_file('/Users/vandana/Desktop/steam-200k.csv')

#add column names
column_names=['user_id','game-title','behavior','value','unknown']
df.columns=column_names

#drop unnecessary columns
df_dropped=drop_column(df,'unknown')

#basic info about dataset
print('dataset info: ')
print(df_dropped.describe())

#print first 5 rows
print(df_dropped.head())
print('\n')

#check for missing values
missing_values=miss_val_column(df_dropped)

# Percentage of missing values
percent_missing=miss_val_percentage(df_dropped,missing_values)

#count duplicate rows
duplicate_rows=df_dropped.duplicated().sum()
print(f'total duplicate rows: {duplicate_rows}')

if duplicate_rows>0:
    print('Duplicate rows are:\n')
    print(df_dropped[df_dropped.duplicated()])



