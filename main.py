from projectml import logger
from projectml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from projectml.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from projectml.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from projectml.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from projectml.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline






STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj1 = DataIngestionTrainingPipeline()
    obj1.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj2 = DataValidationTrainingPipeline()
    obj2.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME= "Data Transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj3 = DataTransformationTrainingPipeline()
    obj3.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME= "Model Trainer stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj4 = ModelTrainerTrainingPipeline()
    obj4.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Evaluation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj5 = ModelEvaluationTrainingPipeline()
    obj5.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

