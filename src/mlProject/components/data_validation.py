import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir) # Read the data
            all_cols = list(data.columns)  # List down all the columns

            all_schema = self.config.all_schema.keys()   # Check with schema.yaml that all the columns present in your data set or not

            
            for col in all_cols:  # If all not present return  status as False ese True , status file will be in artifacts 
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
        
