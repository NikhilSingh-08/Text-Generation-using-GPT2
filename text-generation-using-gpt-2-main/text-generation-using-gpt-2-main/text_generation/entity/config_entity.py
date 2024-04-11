import os
from datetime import datetime
from text_generation import constant

class TrainingPipelineConfig:

    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = constant.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(constant.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp

class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, constant.DATA_INGESTION_DIR_NAME)
        self.data_ingestion_raw_file_path: str = os.path.join(self.data_ingestion_dir, constant.DATA_INGESTION_RAW_DIR_NAME)
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, constant.DATA_INGESTION_FEATURE_STORE_DIR)
        self.ingested_data_file_path: str = os.path.join(self.data_ingestion_dir, constant.DATA_INGESTION_INGESTED_DIR)
        self.train_file_path: str = os.path.join(self.ingested_data_file_path, constant.TRAIN_FILE_NAME)
        self.test_file_path: str = os.path.join(self.ingested_data_file_path, constant.TEST_FILE_NAME)
        self.train_test_split_ratio : float = constant.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO