
from dataclasses import dataclass, field
from typing import List, Optional
import os

@dataclass()
class DataIngestionConfig:
    # """Data Ingestion Configuration"""
    # dataset_download_url: str = field(default="")
    # raw_data_dir: str = field(default="")
    # ingested_data_dir: str = field(default="")
    # ingested_train_dir: str = field(default="")
    # ingested_test_dir: str = field(default="")
    row_data_path: str = os.path.join("artifacts", "data.csv")
    train_data_path: str = os.path.join("artifacts", "train")
    test_data_path: str = os.path.join("artifacts", "test")
    