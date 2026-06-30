from pathlib import Path

# Project Root Directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Dataset Path
HEART_DATASET = RAW_DATA_DIR / "heart_disease_dataset.csv"

# Models Directory
MODELS_DIR = PROJECT_ROOT / "models"

# Reports Directory
REPORTS_DIR = PROJECT_ROOT / "reports"