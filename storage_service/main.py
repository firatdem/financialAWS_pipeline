from fastapi import FastAPI
from pathlib import Path
from storage_service.db import get_conn, insert_invoice
import uvicorn

app = FastAPI()


@app.get("/init-db/")
def init_db():
    """
    Initializes the invoices table in the database using models.sql
    """
    try:
        conn = get_conn()
        cur = conn.cursor()

        schema_path = Path(__file__).resolve().parent / "models.sql"
        with open(schema_path, "r") as f:
            schema_sql = f.read()

        cur.execute(schema_sql)
        conn.commit()
        cur.close()
        conn.close()

        return {"message": "✅ Table initialized successfully."}
    except Exception as e:
        return {"error": f"❌ DB initialization failed: {str(e)}"}


@app.get("/test-insert/")
def test_insert():
    """
    Inserts a sample invoice into the database
    """
    sample_data = {
        "order_id": "INV-1001",
        "customer_id": "CRED123",
        "order_date": "2025-04-15",
        "contact_name": "Jane Doe",
        "address": "123 Main St",
        "city": "New York",
        "postal_code": "10001",
        "country": "USA",
        "phone": "(212) 555-1234",
        "fax": "212-555-5678",
        "total_price": "$1,249.99"
    }

    try:
        insert_invoice(sample_data, "invoice_sample_page_1.png")
        return {"message": "✅ Sample invoice inserted."}
    except Exception as e:
        return {"error": f"❌ Insert failed: {str(e)}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)
