import pandas as pd

def remove_outliers(df,column_name):
    q1=df[column_name].quantile(0.25)
    q3=df[column_name].quantile(0.75)
    iqr=q3-q1

    lower_bound=q1-1.5*iqr
    upper_bound=q3-1.5*iqr

    df_cleaned=df[(df[column_name]>=lower_bound) & (df[column_name]<=upper_bound)].copy()

    return df_cleaned

    