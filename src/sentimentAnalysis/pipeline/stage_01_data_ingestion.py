from sentimentAnalysis.config.configuration import ConfigurationManager
from sentimentAnalysis.components.data_ingestion import DataIngestion
from sentimentAnalysis import logger


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        """
        Initialize DataIngestionTrainingPipeline instance.
        """
        pass

    def main(self):
        """
        Execute the main steps of the data ingestion training pipeline.

        Returns:
            None
        """
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
