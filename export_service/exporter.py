import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

EXPORT_DIR = Path(__file__).resolve().parent / "exports"
EXPORT_DIR.mkdir(exist_ok=True)

def export_as_csv() -> str:
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )

    df = pd.read_sql("SELECT * FROM invoices", conn)
    csv_path = EXPORT_DIR / "invoices_export.csv"
    df.to_csv(csv_path, index=False)

    conn.close()
    return str(csv_path)
