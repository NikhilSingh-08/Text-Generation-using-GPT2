import os
import sys
from text_generation import constant
from text_generation.entity.config_entity import DataIngestionConfig
from text_generation.entity.artifact_entity import DataIngestionArtifact
from text_generation.logger import logging
from text_generation.exception import text_generationException
from text_generation.constant import SCHEMA_FILE_PATH
from text_generation.utils.main_utils import read_yaml_file
from text_generation.cloud_storage.s3_syncer import s3sync
from text_generation.constant import TRAINING_BUCKET_NAME,DATASET


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise text_generationException (e,sys) from e

    def get_data_from_s3(self)-> None:
        try:
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")

            os.makedirs(self.data_ingestion_config.data_ingestion_dir, exist_ok=True)
            s3_sync = s3sync()
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/{DATASET}"
            s3_sync.sync_folder_from_s3(folder=self.data_ingestion_config.data_ingestion_raw_file_path, aws_bucket_url=aws_bucket_url)

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise text_generationException (e,sys) from e



