from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
      ingested_data_file_path: str
      ingested_data_raw_file_path: str
      feature_store_file_path: str
      train_file_path: str
      test_file_path: str