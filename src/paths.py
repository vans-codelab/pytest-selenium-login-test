from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = CURRENT_FILE.parents[1]

LOG_FOLDER = ROOT_DIR / "tests" / "logs"
SCREENSHOT_FOLDER = ROOT_DIR / "tests" / "screenshots"

