CREATE TABLE IF NOT EXISTS invoices (
    id SERIAL PRIMARY KEY,
    source_file TEXT,
    order_id TEXT,
    customer_id TEXT,
    order_date DATE,
    contact_name TEXT,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT,
    phone TEXT,
    fax TEXT,
    total_price NUMERIC(12, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
