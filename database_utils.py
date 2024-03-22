#Python script to read RDS database credentials

#import all dependencies
import yaml
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import pandas as pd
import psycopg2



class DatabaseConnector:
	def __init__(self, credentials):
			self = self
			self.credentials=credentials

#Read credentials from yaml file and return a dictionary called credentials_for_url. 
#Use the dictionary to initialise and return an sqlalchemy db engine
	def create_db_connector(self): 
		db_creds = self.credentials
		with open(db_creds, "r") as file:
			credentials = yaml.safe_load(file) 
			#Rename the keys and create a dictionary we can use for create_engine
			keyMapping = {
			"RDS_HOST":"host",
			"RDS_USER":"username",
            "RDS_PASSWORD":"password",
			"RDS_DATABASE":"database",
            "RDS_PORT":"port",
			}
			credentials_for_url = {keyMapping.get(k,k): v for k,v in credentials.items()}
			#create the sqlalchemy engine
			engine = sqlalchemy.create_engine(f"mysql+pymysql://{credentials_for_url['username']}:{credentials_for_url['password']}@{credentials_for_url['host']}:{credentials_for_url['port']}/{credentials_for_url['database']}?charset=utf8mb4")
			return engine
		



