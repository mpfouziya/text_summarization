from src.text_summarization.components.model_evaluation import ModelEvaluation
from src.text_summarization.config.configuration import ConfigurationManager
from src.text_summarization.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()

        except Exception as e:
            raise e