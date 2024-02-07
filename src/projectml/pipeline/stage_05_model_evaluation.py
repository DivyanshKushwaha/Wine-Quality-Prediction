from projectml.config.configuration import ConfigurationManager
from projectml.components.model_evaluation import ModelEvaluation
from projectml import logger


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):        
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

