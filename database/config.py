from pathlib import Path
import sys
import importlib.util



BASE_DIR = Path(__file__).resolve().parent.parent


DB_URL = "sqlite:///sqlite.db"