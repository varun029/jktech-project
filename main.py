import pandas as pd
import numpy as np
from utils.read import read_file
from utils.missing import miss_val_column
from utils.missing import miss_val_percentage
from utils.drop import drop_column
from utils.duplicate import exact_duplicate_rows,num_exact_duplicates,drop_duplicate_rows,comparison_df,find_partial_duplicates,standardize_titles_shortest
from utils.normalize import normalize_numeric,normalize_text

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
print('\n')

#check for missing values
missing_values=miss_val_column(df)

# Percentage of missing values
percent_missing=miss_val_percentage(df,missing_values)

#find exact duplicate rows
exact_duplicates=exact_duplicate_rows(df)

#count the number of exact duplicates
num_exact_duplicates=num_exact_duplicates(df)

#drop exact duplicates
df_cleaned=drop_duplicate_rows(df)

#comparison
comparison_df(df,df_cleaned)

games=sorted(df_cleaned['game-title'].unique())

with open("game_titles.txt", "w") as f:
    for game in games:
        f.write(game + "\n")

partial_dups=find_partial_duplicates(df,'game-title',threshold=80)

df_cleaned,title_mapping = standardize_titles_shortest(df_cleaned,'game-title',partial_dups)

print("Unique game titles before:", df['game-title'].nunique())
print("Unique game titles after:", df_cleaned['game-title'].nunique())

df_cleaned=normalize_text(df_cleaned,'game-title')
df_cleaned=normalize_text(df_cleaned,'behavior')
df_cleaned=normalize_numeric(df_cleaned,'value')
df_cleaned=normalize_numeric(df_cleaned,'user_id')

print(df.head(15)) 
print('\n')
print(df_cleaned.head(15)) 
print('\n')
print(df.info()) 
print('\n')
print(df_cleaned.info()) 
print('\n')
print(df.nunique()) 
print('\n')
print(df_cleaned.nunique()) 

df_cleaned.to_csv("/Users/vandana/Desktop/cleaned_data.csv", index=False)
