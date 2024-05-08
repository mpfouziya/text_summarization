from src.text_summarization.components.model_trainer import ModelTrainer
from src.text_summarization.config.configuration import ConfigurationManager
from src.text_summarization.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()

        except Exception as e:
            raise e
