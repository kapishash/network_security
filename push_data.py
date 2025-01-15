import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from network_security.logging.logger import logging
from network_security.exception.exception import NetworkSecurityException


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL)

ca=certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def csv_to_json(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records=list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]

            self.collection.insert_many(self.records)
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=="__main__":
        networkobj=NetworkDataExtract()
        FILE_PATH="network_data\phisingData.csv"
        DATABASE="KAPISHANKAR"
        collection="networksecurity"

        records=networkobj.csv_to_json(file_path=FILE_PATH)
        no_of_records=networkobj.insert_data_mongo(records,DATABASE,collection)
        print(no_of_records)