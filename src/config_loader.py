import os
from pathlib import Path
from typing import Any, Dict, Optional

from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

def load_env(env_file: Optional[Path] = None) -> None:
    """Load environment variables from a .env file."""
    env_path = env_file or BASE_DIR / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)


def load_yaml_config(file_path: Path) -> Dict[str, Any]:
    """Load YAML configuration file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)
