from dataclasses import dataclass
from pathlib import Path

# The dataclass decorator simplifies the creation of classes by automatically generating special 
# methods like __init__, __repr__, __eq__, etc.
# frozen=True parameter makes the class immutable, 
# meaning once an instance is created, its attributes cannot be modified.
@dataclass(frozen=True)


class DataIngestionConfig:
    # Root directory where all data ingestion-related files will be stored
    root_dir: Path
    
    # stores the URL from which the dataset will be downloaded.
    source_URL: str
    
    # Represents the path on the local filesystem where the downloaded dataset will be saved 
    local_data_file: Path
    
    #  directory where the downloaded zip file will be extracted after download.
    unzip_dir: Path
