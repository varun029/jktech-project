import pandas as pd
import numpy as np
from utils.read import read_file
from utils.missing import miss_val_column
from utils.missing import miss_val_percentage
from utils.drop import drop_column
from utils import duplicate

#loading the dataset
df_steam=read_file('/Users/vandana/Desktop/steam-200k.csv')

#add column names
column_names=['user_id','game-title','behavior','value','unknown']
df_steam.columns=column_names

#drop unnecessary columns
df=drop_column(df_steam,'unknown')

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

#find exact duplicate rows
exact_duplicates=duplicate.exact_duplicate_rows(df)

#count the number of exact duplicates
num_exact_duplicates=duplicate.num_exact_duplicates(df)

#drop exact duplicates
df_cleaned=duplicate.drop_duplicate_rows(df)

#comparison
duplicate.comparison_df(df,df_cleaned)

