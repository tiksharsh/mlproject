# https://pythonhow.com/what/what-to-do-to-import-files-from-different-folder-in-python/#:~:text=To%20import%20a%20file%20from,searches%20for%20modules%20and%20packages.

import os
import sys
import pandas as pd
import numpy as np

sys.path.append("src")
from logger import logging
from exception import CustomException

from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig

from sklearn.model_selection import train_test_split
from dataclasses import dataclass




@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact',"train.csv")
    test_data_path: str = os.path.join('artifact',"test.csv")
    raw_data_path: str = os.path.join('artifact',"data.csv")
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered into data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Exported or Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train & Test split initiated")
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed!!")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            
            )
        except Exception as e:
            logging.info("Indside Data Ingestion exception!!")
            raise CustomException(e, sys)
      
# Below code is created for data_ingestion file testing purpose  

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data =  obj.initiate_data_ingestion()
    data_tranformation = DataTransformation()
    data_tranformation.initiate_data_transformation(train_data, test_data)
        
    
