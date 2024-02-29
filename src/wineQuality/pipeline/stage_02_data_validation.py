from wineQuality.config import ConfigurationManager
from wineQuality.components import DataValidation
from wineQuality import logger

STAGE_NAME = 'Data Validation'

class DataValidationTrainPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_columns()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> {STAGE_NAME} stage started<<<<<')
        obj = DataValidationTrainPipeline()
        obj.main()
        logger.info(f'>>>>> {STAGE_NAME} stage finished<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e