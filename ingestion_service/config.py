from pathlib import Path

# Directory where uploaded PDFs will be stored
UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
