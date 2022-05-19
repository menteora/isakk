# StandarClass
from sqlalchemy import create_engine
from pathlib import Path
import json

def getEngineFromConfig(config_file):
    if Path(config_file).exists():
        with open(config_file, 'r') as f:
            config_json = json.load(f)
    user = config_json['authentication']['user']
    password = config_json['authentication']['password']
    host = config_json['authentication']['host']
    database = config_json['authentication']['database']
    conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
    return create_engine(conn_str)

def getEngineFromConfigWithUserAndPassword(config_file, user, password):
    if Path(config_file).exists():
        with open(config_file, 'r') as f:
            config_json = json.load(f)
    host = config_json['authentication']['host']
    database = config_json['authentication']['database']
    conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
    return create_engine(conn_str)

def getEngineFromJson(config_json):
    user = config_json['authentication']['user']
    password = config_json['authentication']['password']
    host = config_json['authentication']['host']
    database = config_json['authentication']['database']
    conn_str = 'mssql+pymssql://'+user+':'+password+'@'+host+'/'+database
    return create_engine(conn_str)