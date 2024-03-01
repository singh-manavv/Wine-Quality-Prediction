from wineQuality.config import ConfigurationManager
from wineQuality.components import DataTransformation
from wineQuality import logger

STAGE_NAME = 'Data Transformation'

class DataTransformationTrainPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.splitting_data()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> {STAGE_NAME} stage started<<<<<')
        obj = DataTransformationTrainPipeline()
        obj.main()
        logger.info(f'>>>>> {STAGE_NAME} stage finished<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e