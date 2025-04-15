from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from file_handler import save_pdf
import uvicorn

app = FastAPI()


@app.post("/upload/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    saved_paths = []
    for file in files:
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail=f"{file.filename} is not a PDF.")

        path = await save_pdf(file)
        saved_paths.append(path)

    return {
        "message": f"{len(saved_paths)} files uploaded successfully.",
        "paths": saved_paths
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
