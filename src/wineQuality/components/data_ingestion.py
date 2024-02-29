import os
from urllib import request
from zipfile import ZipFile
from pathlib import Path
from wineQuality import logger
from wineQuality.utils import get_size
from wineQuality.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file)
            logger.info(f'{filename} downloaded with following info: \n{headers}')
        else:
            logger.info(f'File already exists with size : {get_size(Path(self.config.local_data_file))}')
    
    def extract_zipfile(self):
        '''
        zip_file_path : str
        Extracts the zip file into data directory path
        Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)