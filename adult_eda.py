# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D 

df = pd.read_csv('C:\\Tools\\python_lab\\adult\\adult.csv', engine='python')
print("="*20)
print("DATASET INFORMATION")
df.info()
print("="*20)

#LIST OF CATEGORICAL VARIABLES
col_list = list(df.columns)
categ_list = []
num_list = []

for col in col_list:
    if df[col].dtype == 'object' :
        new_var_name = 'CATEG_'+df[col].name
        print("Nouvelle var => " + new_var_name)
        df[new_var_name] = df[col].astype('category')
        df.drop(df[col].name, axis=1)
        categ_list.append(new_var_name)
    else:
        num_list.append(df[col].name)


print("="*20)
print("CATEGORICAL VARS")
print("="*20)
print("\t \n".join(categ_list))

print("="*20)
print("NUMERIC VARS")
print("="*20)
print("\t \n".join(num_list))

print(df['CATEG_income'].unique())

print("="*20)
print("CREATION VAR TARGET")
print("="*20)

df['target'] = (df['CATEG_income'] == '>50K').astype(int)

# Quantile cut for numeric vars using pandas Qcut
numeric_df = df[num_list]

def standardize_column(col):
    col_mean = col.mean()
    col_std = col.std(ddof=0)
    return (col - col_mean) / col_std

def decile(col):
    return pd.qcut(col, q=10, duplicates='drop')

# appliquer sur toutes les cols 
binned_num = numeric_df.apply(decile)

# Df contenant les variables standardise
std_num = numeric_df.apply(standardize_column)


# Df contenant les variables discretisees en deciles
decile_num = numeric_df.apply(decile)






