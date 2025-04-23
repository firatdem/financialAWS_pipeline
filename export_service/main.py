from fastapi import FastAPI
from fastapi.responses import FileResponse
from export_service.exporter import export_as_csv
import uvicorn
from pathlib import Path

app = FastAPI()


@app.get("/export/csv")
def download_csv():
    export_path = export_as_csv()
    return FileResponse(
        path=export_path,
        filename=Path(export_path).name,
        media_type='text/csv'
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8004)
