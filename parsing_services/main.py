from fastapi import FastAPI, Query, HTTPException
from parsing_services.parser import run_ocr_and_parse_single
import uvicorn

app = FastAPI()


@app.get("/run-parser/")
def trigger_ocr_and_regex(filename: str = Query(..., description="PNG filename in processed_images folder")):
    try:
        result = run_ocr_and_parse_single(filename)
        return {
            "message": f"OCR and parsing complete for '{filename}'",
            "data": result
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
