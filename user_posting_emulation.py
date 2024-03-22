import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
import datetime
from json import JSONEncoder
import yaml
from database_utils import DatabaseConnector

dc = DatabaseConnector(credentials="rds_creds.yaml")

random.seed(100)

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()



#Step1: read the database credentials and return a db engine that can be initialised later
engine=dc.init_db_creds()
print(engine)

# class AWSDBConnector:

#     def __init__(self):

#         self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
#         self.USER = 'project_user'
#         self.PASSWORD = ':t%;yCY3Yjg'
#         self.DATABASE = 'pinterest_data'
#         self.PORT = 3306
        
#     def create_db_connector(self):
#         engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
#         return engine


# new_connector = AWSDBConnector()


# def run_infinite_post_data_loop():
#     while True:
#         sleep(random.randrange(0, 2))
#         random_row = random.randint(0, 11000)
#         engine = new_connector.create_db_connector()

#         with engine.connect() as connection:
#             #Extract pin data
#             pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
#             pin_selected_row = connection.execute(pin_string)
            
#             for row in pin_selected_row:
#                 pin_result = dict(row._mapping)
#                 invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/topics/12d6e5017cf5.pin"
#                 #Send JSON data to Kafka
#                 pin_payload = json.dumps({"records": [{"value": pin_result}]}, cls=DateTimeEncoder)
#                 headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
#                 post_response_pin = requests.request("POST", invoke_url, headers=headers, data=pin_payload)


#             #Extract geolocation data of each pin
#             geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
#             geo_selected_row = connection.execute(geo_string)
            
#             for row in geo_selected_row:
#                 geo_result = dict(row._mapping)
#                 invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/topics/12d6e5017cf5.geo"                
#                 #Send JSON data to Kafka
#                 payload = json.dumps({"records": [{"value": geo_result}]}, cls=DateTimeEncoder)
#                 headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
#                 response_geo = requests.request("POST", invoke_url, headers=headers, data=payload)


#             #Extract user data for each pin
#             user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
#             user_selected_row = connection.execute(user_string)
            
#             for row in user_selected_row:
#                 user_result = dict(row._mapping)
#                 invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/topics/12d6e5017cf5.user"                
#                 #Send JSON data to Kafka
#                 payload = json.dumps({"records": [{"value": user_result}]}, cls=DateTimeEncoder)
#                 headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
#                 response_user = requests.request("POST", invoke_url, headers=headers, data=payload)

#             pin_results = print(pin_result)
#             print("pin response:",post_response_pin)
#             #print(pin_response.status_code)
#             #print(geo_result)
#             #print("geo response:",response_geo)
#             #print(user_result)
#             #print("user response:",response_user)



# if __name__ == "__main__":
#     run_infinite_post_data_loop()
#     print('Working')
    
    


