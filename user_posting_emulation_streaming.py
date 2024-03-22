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
from database_utils import DatabaseConnector

dc = DatabaseConnector(credentials="rds_creds.yaml")



random.seed(100)

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()



def stream_data_to_kinesis():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = dc.create_db_connector()

        with engine.connect() as connection:
            #Extract pin data
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)

            for row in pin_selected_row:
                pin_result = dict(row._mapping)
                invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-12d6e5017cf5-pin/record"
                #To send JSON messages you need to follow this structure
                pin_payload = json.dumps({
                "StreamName": "streaming-12d6e5017cf5-pin",
                "Data": pin_result,
                "PartitionKey": str(random.randrange(100))
                })
                headers = {'Content-Type': 'application/json'}
                pin_response = requests.request("PUT", invoke_url, headers=headers, data=pin_payload)
                print(pin_response.json())

            #Extract geolocation data of each pin
            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)

            for row in geo_selected_row:
                geo_result = dict(row._mapping)
                invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-12d6e5017cf5-geo/record"
                #To send JSON messages you need to follow this structure
                geo_payload = json.dumps({
                "StreamName": "streaming-12d6e5017cf5-geo",
                "Data": geo_result,
                "PartitionKey": str(random.randrange(100))
                }, cls=DateTimeEncoder)
                headers = {'Content-Type': 'application/json'}
                geo_response = requests.request("PUT", invoke_url, headers=headers, data=geo_payload)
                print(geo_response.json())

            #Extract user data for each pin
            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
  
            for row in user_selected_row:
                user_result = dict(row._mapping)
                invoke_url = "https://y6zlosa988.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-12d6e5017cf5-user/record"
                #To send JSON messages you need to follow this structure
                user_payload = json.dumps({
                "StreamName": "streaming-12d6e5017cf5-user",
                "Data": user_result,
                "PartitionKey": str(random.randrange(100))
                }, cls=DateTimeEncoder)
                headers = {'Content-Type': 'application/json'}
                user_response = requests.request("PUT", invoke_url, headers=headers, data=user_payload)
                print(user_response.json())

            print("pin response:", pin_response.status_code)
            print("geo response:", geo_response.status_code)
            print("user response:", user_response.status_code)

if __name__ == "__main__":
    stream_data_to_kinesis()
    print('Working')
    