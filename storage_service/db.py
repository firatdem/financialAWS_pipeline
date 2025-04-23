import psycopg2
from datetime import datetime


def get_conn():
    return psycopg2.connect(
        dbname="financials",
        user="user",
        password="password",
        host="127.0.0.1",
        port=5432
    )


def insert_invoice(data: dict, source_file: str):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO invoices (
            source_file, order_id, customer_id, order_date,
            contact_name, address, city, postal_code,
            country, phone, fax, total_price
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        source_file,
        data.get("order_id"),
        data.get("customer_id"),
        data.get("order_date"),
        data.get("contact_name"),
        data.get("address"),
        data.get("city"),
        data.get("postal_code"),
        data.get("country"),
        data.get("phone"),
        data.get("fax"),
        float(data.get("total_price").replace("$", "").replace(",", "")) if data.get("total_price") else None
    ))

    conn.commit()
    cur.close()
    conn.close()
