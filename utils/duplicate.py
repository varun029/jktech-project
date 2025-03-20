import pandas as pd
from rapidfuzz import fuzz,process

def exact_duplicate_rows(df):
    exact_duplicates=df[df.duplicated()]
    print(exact_duplicates.head())
    print('\n')
    return exact_duplicates

def num_exact_duplicates(df):
    num_exact_duplicates=df.duplicated().sum()
    print(f'The number of exact duplicate rows are: {num_exact_duplicates}')
    print('\n')
    return num_exact_duplicates

def drop_duplicate_rows(df):
    df_dropped=df.drop_duplicates()
    print(df_dropped.head())
    print('\n')
    return df_dropped

def comparison_df(df,df_cleaned):
    print(f'Number of rows before dropping exact duplicates are {df.shape[0]}\n')
    print(f'Number of rows after dropping exact duplicates are {df_cleaned.shape[0]}\n')
    print(f'The difference of rows after dropping exact duplicates is: {df.shape[0]-df_cleaned.shape[0]}\n')

def find_partial_duplicates(df,column_name,threshold=80):
    unique_values=df[column_name].unique()
    partial_duplicates={}

    for title in unique_values:
        matches = process.extract(title, unique_values, scorer=fuzz.ratio, limit=5)
        similar_titles=[match[0] for match in matches if match[1]>= threshold and match[0]!=title]


        if similar_titles:
            partial_duplicates[title]=similar_titles

    return partial_duplicates
