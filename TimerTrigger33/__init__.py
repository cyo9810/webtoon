import csv
import datetime
import imp
import json
import logging
import sys
import time
import os
from encodings import utf_8_sig  # 액셀파일에서 한글깨질때

import azure.functions as func
import requests
from bs4 import BeautifulSoup
from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError

sys.path.append("./")
from . import weather_az1

# import weather_az1

# def main(mytimer: func.TimerRequest) -> None:
"""
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = (
        datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    )
"""
def main(mytimer: func.TimerRequest, tablePath:func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()


    if mytimer.past_due:
        logging.info("The timer is past due!")

    logging.info("Python timer trigger function ran at %s", utc_timestamp)

    # TODO: The key of the data should in english
    # data_weather=weather_az1.scrape_weather()
    
    # data_weather = weather_az1.scrape_weather()
    # data_weather["PartitionKey"] = "temp"
    # data_weather["RowKey"] = utc_timestamp
    # print(data_weather)
    # new_data = {"PartitionKey": "temp", "RowKey": utc_timestamp}
    

    print("weather!!")
    tags = weather_az1.scrape_weather()
    logging.info("tags data %s",tags)
    #print(tags)
    #weather_data = []

    new_data = {
        "curr_temp": tags[0],
        "cast": tags[1],
        "s_list": tags[2],
        "chart_list": tags[3],
        "rank5": tags[4],
        "rank6": tags[5],
        "rank7": tags[6],
        "rank8": tags[7],
        "rank9": tags[8],
        "rank10": tags[9],
        
        "PartitionKey": "temp",
        "RowKey": time.time() #utc_timestamp
    }
    print("new_data=",new_data)
    #weather_data.append(new_data)
    #print("weather_dat=", weather_data)


    tablePath.set(json.dumps(new_data)) # 1 행씩 전달, list [] 필요 없음, dictionary(string) 전달

    #logging.info("tags data %s",new_data)
    
    
    #----------
     
    # # Create a service client of table storage
    # try:
    #     conn_string = os.getenv("AzureWebJobsStorage")
    #     table_service_client = TableServiceClient.from_connection_string(
    #         conn_str=conn_string
    #     )
    # except:
    #     logging.error("Error while creating table storage service client")

    # # Create a table client in order to create entities
    # try:
    #     table_name = "WeatherData"
    #     table_client = table_service_client.get_table_client(table_name=table_name)
    # except HttpResponseError as error:
    #     logging.error(f"Error while creating table client: {error}")

    # # Create entities in the table
    # try:
    #     entity = table_client.create_entity(entity= new_data)
    #     logging.info(f"Successfully created entity: {entity}")
    # except HttpResponseError as error:
    #     logging.error(f"Error while creating entity at table {error}")
    #------- 