from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger
from mlProject.entity.config_entity import DataIngestionConfig



STAGE_NAME= " Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
