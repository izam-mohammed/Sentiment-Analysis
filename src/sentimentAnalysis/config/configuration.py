from sentimentAnalysis.constants import *
from sentimentAnalysis.utils.common import read_yaml, create_directories
from sentimentAnalysis.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    PredictionConfig,
)


# udpate configuration manager
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):
        """
        Initialize ConfigurationManager instance.

        Parameters:
        - config_filepath: str
            Filepath for the configuration file.
        - params_filepath: str
            Filepath for the parameters file.
        - schema_filepath: str
            Filepath for the schema file.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the configuration object for data ingestion.

        Returns:
        - DataIngestionConfig
            Configuration object for data ingestion.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Get the configuration object for data validation.

        Returns:
        - DataValidationConfig
            Configuration object for data validation.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        delimeter = self.schema.DELIMITER
        target_out = self.schema.TARGET_OUT
        target_col = self.schema.TARGET_COLUMN.name

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
            delimeter=delimeter,
            target_out=target_out,
            target_col=target_col,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Get the configuration object for data transformation.

        Returns:
        - DataTransformationConfig
            Configuration object for data transformation.
        """
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            delimiter=self.schema.DELIMITER,
            text_corpus_name=config.text_corpus_name,
            target_col_encoded_file=config.target_col_encoded_file,
            vectorizer_name=config.vectorizer_name,
            vocabulary_name=config.vocabulary_name,
            test_size=config.test_size,
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Get the configuration object for model training.

        Returns:
        - ModelTrainerConfig
            Configuration object for model training.
        """
        config = self.config.model_trainer
        params = self.params
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            model_params=params.MultinomialNB,
            target_column=schema.name,
            vectorizer_path=config.vectorizer_path,
            vocabulary_path=config.vocabulary_path,
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Get the configuration object for model evaluation.

        Returns:
        - ModelEvaluationConfig
            Configuration object for model evaluation.
        """
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            vectorizer_path=config.vectorizer_path,
        )

        return model_evaluation_config

    def get_prediction_config(self) -> PredictionConfig:
        """
        Get the configuration object for prediction.

        Returns:
        - PredictionConfig
            Configuration object for prediction.
        """
        config = self.config.prediction

        create_directories([config.root_dir])

        prediction_config = PredictionConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            vectorizer_path=config.vectorizer_path,
            data_path=config.data_path,
            prediction_file=config.prediction_file,
        )

        return prediction_config
