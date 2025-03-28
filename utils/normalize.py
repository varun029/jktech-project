import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt
import seaborn as sns

def normalize_text(df,column_name):
    df[column_name]=df[column_name].str.strip().str.lower().replace(r'\s+',' ',regex=True)
    return df

def normalize_numeric(df,column_name):
    df[column_name]=pd.to_numeric(df[column_name],errors='coerce')
    return df

def normalize_robust(df,column_name):
    scaler=RobustScaler()
    df[column_name]=scaler.fit_transform(df[[column_name]])
    return df   

def normalize_log(df,column_name):
    df[column_name]=np.log1p(df[column_name])
    return df