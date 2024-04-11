"""
application constants
"""
import os

APP_HOST = "0.0.0.0"
APP_HOST = 8080


"""
env_variables constants
"""
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ID_ENV_KEY = "AWS_SECRET_ACCESS-KEY"
REGION_NAME = "US-EAST-1"

"""
s3_bucket constants
"""
TRAINING_BUCKET_NAME = "text-generation-training-pipeline"
PREDICTION_BUCKET_NAME = "text-generation-datasource"
DATASET = "imdb_dataset"


"""--------------------------------------------------------------training_pipeline constants----------------------------------------------------------------------------------------------------------
"""
# defining common constant variable for training pipeline

PIPELINE_NAME: str = "text_generation"
ARTIFACT_DIR: str = "artifact"
MODEL_NAME: str = "gpt-2"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH: str = os.path.join('config', 'schema.yaml')


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_RAW_DIR_NAME: str = "raw_dataset"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_FEATURE_STORE_DIR = "feature-store"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
CSV_FILE_NAME: str = "imdb.csv"
