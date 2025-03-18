import pandas as pd

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
    print(f'Number of rows in the dataset are {df.shape[0]}\n')
    print(f'Number of rows after dropping exact duplicates are {df_cleaned.shape[0]}\n')
    print(f'The difference of rows after dropping exact duplicates is: {df.shape[0]-df_cleaned.shape[0]}\n')