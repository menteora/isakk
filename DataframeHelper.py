import pandas as pd
import datetime
import numpy as np

# Merge 2 lists with join | Unire le due liste
def join_two_df(df_master, df_slave, index_master, index_slave):
    df_master = df_master.set_index(index_master)
    merged_df = df_master.join(df_slave.set_index(index_master), on=index_slave).reset_index()
    return merged_df

# Merge 2 lists without lost records | Unire le due liste senza escludere nessun record
def merge_two_df_and_get_all_records(df_master, df_slave, index_master, index_slave):
    merged_df = pd.merge(df_master, df_slave, on=[index_master,index_slave], how="outer", indicator=True)
    #df_master = df_master.set_index(index_master)
    #merged_df = df_master.merge(df_slave.set_index(index_master), right_on=index_slave, left_on=index_master,  how = "outer", suffixes=('_master', '_slave'),right_index=True,left_index=True)
    return merged_df

# Convert column to list
def columns_to_list(df):
    return df.columns.tolist()

# Get only columns inside list
def get_column_inside_list(df, custom_list):
    return df[df.columns.intersection(custom_list)]

# Order column | Ordinare la colonna
def order_by(df, field, ascending=True):
    df = df.sort_values(by=[field], ascending=ascending) # False descending
    return df

# Convert column into datetime field | Convertire la colonna data in formato data
def convert_to_dateonly(df, date_field, format='%d/%m/%Y'):
    df[date_field] = pd.to_datetime(df[date_field], format=format).dt.date # with date format
    return df

# Filter column equal to
def filter_column_equal_to(df, column, filter):
    filtered = df[column]==filter
    return df[filtered]

def fill_column_with_value(df, name, value):
    df[name] = value
    return df

def filter_column_from_list(df, columns = []):
    """ Filtra le colonne da prendere dentro un dataframe partendo da una lista"""
    return df[columns]

def get_columns_name_as_dict(df):
    """ Ritorna le colonne dentro il dataframe come un dict"""

    df_headers_dict = {}
    
    for col in df.columns:

        idx = df.columns.get_loc(col)
        df_headers_dict[col] = idx

    return df_headers_dict
