# 📄 Financial Document Processing Pipeline

A modular, cloud-ready pipeline designed to ingest, process, and extract structured data from financial documents like invoices, loan applications, and bank statements. Built with a focus on clean architecture, scalability, and future AWS deployment.

---

## ✅ Current Features

### 🔹 Step 1: Ingestion Layer (Complete)

- **Built with FastAPI** to expose a secure `/upload/` REST API.
- Supports **batch PDF uploads** via multipart form data.
- Performs **extension validation** (only `.pdf` allowed).
- Automatically **sanitizes filenames** to strip dangerous characters.
- Appends **timestamps** to avoid filename collisions and track uploads.
- Stores files to a configurable local `uploads/` directory.

### 🔹 Step 2: Preprocessing Layer (Complete)

- **Exposes `/preprocess/` API** to trigger image generation from uploaded PDFs.
- Converts PDFs to high-resolution **300 DPI** images using `pdf2image`.
- Applies **grayscale conversion**, **contrast enhancement**, and **binarization** for OCR readiness.
- Implements **automated cleanup** of the `processed_images/` folder before each run.
- Saves each page as a separate `.png` image for downstream processing.

### 🔹 Step 3: Parsing Layer (Complete)

- **Exposes `/run-parser/` API** to run OCR and extract structured data from images.
- Uses Tesseract OCR to convert .png files to raw text.
- Applies regex-based field extraction (e.g. invoice number, date, price, etc.).
- Outputs parsed results as .json files in the parsed_results/ folder.

### 🔹 Step 4: Data Storage Layer (Complete
- **Exposes `/init-db/` and `/test-insert` APIs** fpr DB scehma setup and insertion testing.
- Uses **PostgreSQL** running inside a **Docker container**
- Extracted fields from Step 3 are saved into a structured `invoices` table
- Credentials managed via `.env` file in project root
   
### 🔹 Step 5: Export Layer (Complete)
- **Exposes `/export/csv` endpoint** for downloading all stored invoices.
- Pulls all data from PostgreSQL and converts it into a **downloadable CSV file.**
- Supports future expansion for Excel/JSON export and filter-based querying.
  
---

## 🛠️ How to Run (Each process is modular, by design can be run completely independent of one another, still need to create universal main to call all at once.)

Prelim steps:

git clone https://github.com/firatdem/financialAWS_pipeline.git

THEN,

Create env to match the docker-compose.yml. Did not include .env (although not really secret...) for keeping good practice reasons.

### ▶️ Step 1: Run Ingestion Service

```bash
pip install -r requirements.txt
cd ingestion_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8000/docs

### ▶️ Step 2: Run Preprocessing Service

```bash
cd preprocessing_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8001/docs

### ▶️ Step 3: Run Parsing Service

```bash
cd parsing_services
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8002/docs

### ▶️ Step 4: Run Storage Service (PostgreSQL required)

```bash
docker-compose up -d  # Starts the Postgres container
cd storage_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8003/docs

### ▶️ Step 5: Run Export Service

```bash
cd export_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8004/docs

---

## 📥 Example Upload Response

```json
{
  "message": "2 files uploaded successfully.",
  "paths": [
    "uploads/20250415_142314_invoice_april_2024.pdf",
    "uploads/20250415_142402_invoice_march.pdf"
  ]
}
```

## 🖼️ Example Preprocess Response
```json
{
  "message": "Preprocessing completed for invoice_april_2024.pdf",
  "images": [
    "processed_images/invoice_april_2024_page_1.png",
    "processed_images/invoice_april_2024_page_2.png"
  ]
}
```

---

🧰 Tech Stack
- Python 3.x
- FastAPI (REST Framework)
- PostgreSQL (via Docker)
- Tesseract OCR
- Pandas (for CSV export)
- Pillow / pdf2image (for image conversion)
- dotenv + Uvicorn + psycopg2
- Modular folder structure (AWS-ready, EC2 compatible)

---

## 🛤️ Roadmap

### ✅ Step 1: Ingestion Layer
### ✅ Step 2: Preprocessing Layer
### ✅ Step 3: Parsing Layer
### ✅ Step 4: Data Storage Layer
### ✅ Step 5: Export Layer (Add filters to exports!!!)

---

## 🚀 Deployment & DevOps

- Docker Compose support for PostgreSQL
- .env used for managing credentials
- Future AWS-ready: S3 for file storage, EC2 for app hosting, RDS for managed DB
 
---

## 🔐 Security & Enhancements

- Add API key or token-based authentication  
- Enforce file size limits and MIME-type validation  
- Build an audit log of uploads and extraction results  
- Implement version control for processed files  

---

## 📌 Project Status

✅ **In Progress** – Full ingestion-to-storage pipeline is implemented and testable. Dashboard and cloud deployment are next.

---

## 👤 Author

**Firat Demirbulakli**  
[GitHub](https://github.com/) • [Email](mailto:) • [LinkedIn](https://linkedin.com/)
