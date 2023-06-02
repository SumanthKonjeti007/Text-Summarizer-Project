from dataclasses import dataclass
from pathlib import Path

#"Entity" is a return type of a function.
@dataclass(frozen=True)
class DataIngestionConfig:
    #it's a data class, mention the variable used in config.yaml for data ingestion.
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#returns the data validation objects inside config.yaml
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path