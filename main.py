from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":

    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("data ingestion initiates")
        data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
