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

@dataclass(frozen=True)
class ModelTrainerConfig:
    #parameters from config.yaml
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    #parameters from params.yaml
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path