import os
import pandas as pd
from wineQuality import logger
from sklearn.model_selection import train_test_split
from wineQuality.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
    
    def splitting_data(self):
        data = pd.read_csv(self.config.data_path)
        
        train_set, test_set = train_test_split(data,test_size=0.2,random_state=42)
        
        train_set.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
        
        logger.info('Data splitted into Training and test sets')
        logger.info(f'Train Data shape: {train_set.shape}')
        logger.info(f'Test Data shape: {test_set.shape}')