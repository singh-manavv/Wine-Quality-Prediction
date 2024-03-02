from wineQuality import logger
from wineQuality.pipeline import (  DataIngestionTrainPipeline, 
                                    DataValidationTrainPipeline, 
                                    DataTransformationTrainPipeline,
                                    ModelTrainingPipeline,
                                    ModelEvaluationPipeline)


STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage started<<<<<')
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation'
try:
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage started<<<<<')
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation'
try:
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage started<<<<<')
    data_Transformation = DataTransformationTrainPipeline()
    data_Transformation.main()
    logger.info(f'>>>>>>>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training'
try:
    logger.info(f'>>>>> {STAGE_NAME} stage started<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation'
try:
    logger.info(f'>>>>> {STAGE_NAME} stage started<<<<<')
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f'>>>>> {STAGE_NAME} stage finished<<<<<\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
except Exception as e:
    logger.exception(e)
    raise e