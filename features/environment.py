import sys
from pathlib import Path

# Allows Behave step definitions to import from src/
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
