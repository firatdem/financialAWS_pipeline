from fastapi import FastAPI, Query, HTTPException
from preprocessing_service.preprocess import pdf_to_images
from ingestion_service.config import UPLOAD_DIR
from pathlib import Path
import uvicorn

app = FastAPI()


@app.get("/preprocess/")
def run_preprocessing(filename: str = Query(..., description="PDF filename in the uploads folder")):
    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found.")

    image_paths = pdf_to_images(str(pdf_path))
    return {
        "message": f"Preprocessing completed for {filename}",
        "images": image_paths
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
