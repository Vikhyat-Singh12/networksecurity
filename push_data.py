import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)

            records = data.to_dict(orient='records')

            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongo(self, records, databases, collection):
        try:
            self.collection = collection
            self.databases = databases
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            db = self.mongo_client[self.databases]
            coll = db[self.collection]
            coll.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
        


if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "Vikhyat"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_to_mongo(records,DATABASE,Collection)

    print(records)
    print(no_of_records)