import pandas as pd
import datetime
import numpy as np

# Merge 2 lists with join | Unire le due liste
def join_two_df(df_master, df_slave, index_master, index_slave):
    df_master = df_master.set_index(index_master)
    merged_df = df_master.join(df_slave.set_index(index_master), on=index_slave)
    return merged_df

# Merge 2 lists without lost records | Unire le due liste senza escludere nessun record
def merge_two_df_and_get_all_records(df_master, df_slave, index_master, index_slave):
    merged_df = pd.merge(df_master, df_slave, on=[index_master,index_slave], how="outer", indicator=True)
    #df_master = df_master.set_index(index_master)
    #merged_df = df_master.merge(df_slave.set_index(index_master), right_on=index_slave, left_on=index_master,  how = "outer", suffixes=('_master', '_slave'),right_index=True,left_index=True)
    return merged_df

def columns_to_list(df):
    return df.columns.tolist()

def get_column_inside_list(df, custom_list):
    return df[df.columns.intersection(custom_list)]