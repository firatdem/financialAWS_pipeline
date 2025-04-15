import shutil
import re
from fastapi import UploadFile, HTTPException
from config import UPLOAD_DIR
from datetime import datetime
from pathlib import Path

ALLOWED_EXTENSIONS = {".pdf"}

def sanitize_filename(filename: str) -> str:
    # Remove path separators (e.g., ../ or \)
    filename = Path(filename).name

    # Replace spaces with underscores
    filename = filename.replace(" ", "_")

    # Remove special characters (keep alphanumeric, dash, underscore, dot)
    filename = re.sub(r"[^a-zA-Z0-9._-]", "", filename)

    return filename

async def save_pdf(uploaded_file: UploadFile) -> str:
    original_filename = uploaded_file.filename.lower()
    if not any(original_filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Unsupported file type. Only PDFs allowed.")

    sanitized_name = sanitize_filename(original_filename)

    # Add timestamp to filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    timestamped_name = f"{timestamp}_{sanitized_name}"

    # Save file
    file_path = UPLOAD_DIR / timestamped_name
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return str(file_path)
