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

#Read credentials from yaml file and return a dictionary called credentials_for_url. Requires path and file name of yaml file containing credentials
	def read_db_creds(self): 
		db_creds = self.credentials
		with open(db_creds, "r") as file:
			credentials = yaml.safe_load(file) 
			#Rename the keys and create a dictionary we can use for create_engine
			keyMapping = {
			"HOST":"host",
			"USER":"project_user",
            "PASSWORD":"password",
			"RDS_DATABASE":"database",
            "RDS_PORT":"port",
			}
			credentials_for_url = {keyMapping.get(k,k): v for k,v in credentials.items()}
		return credentials_for_url


#Function to use the db credentials returned by read_db_creds. Initialise and return an sqlalchemy db engine
	def init_db_creds(self):
		credentials = self.read_db_creds()
		url = URL.create(**credentials)
		engine = create_engine(url, echo=True)
		return engine