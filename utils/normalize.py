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