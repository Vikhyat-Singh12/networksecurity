import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transfromation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig



if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()


        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        datingestionartifacts = data_ingestion.initiate_data_ingestion()
        print(datingestionartifacts)
        logging.info("Data initiation completed")

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(datingestionartifacts,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation completed")


        logging.info("Initiate the data transformation")
        data_tranformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transfromation = DataTransformation(data_validation_artifact,data_tranformation_config)
        data_transfromation_artifact = data_transfromation.initiate_data_transformation()
        print(data_transfromation_artifact)
        logging.info("Data transformation completed")


       
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    