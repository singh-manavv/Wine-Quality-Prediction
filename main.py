from wineQuality import logger
from wineQuality.pipeline import DataIngestionTrainPipeline


STAGE_NAME = 'Data Ingestion'

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage started<<<<<')
        data_ingestion = DataIngestionTrainPipeline()
        data_ingestion.main()
        logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    except Exception as e:
        logger.exception(e)
        raise e