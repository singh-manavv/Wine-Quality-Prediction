import os
import pandas as pd
from wineQuality import logger
from wineQuality.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir,index_col='Id')
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schemas.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation Status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation Status: {validation_status}')
            return validation_status
        except Exception as e:
            raise e