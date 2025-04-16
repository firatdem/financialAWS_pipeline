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

---

## 🛠️ How to Run

### ▶️ Step 1: Run Ingestion Service

```bash
pip install -r requirements.txt
cd ingestion_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8001/docs

### ▶️ Step 2: Run Preprocessing Service

```bash
cd preprocessing_service
python main.py
```
#### Visit the interactive docs: http://127.0.0.1:8000/docs

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

## 🧰 Tech Stack

- Python 3.x  
- FastAPI  
- Uvicorn  
- Pillow  
- pdf2image  
- OpenCV *(optional)*  
- Modular structure *(future Docker + AWS ready)*

---

## 🛤️ Roadmap

### ✅ Step 1: Ingestion Layer (Complete)
- Build `/upload/` REST endpoint with FastAPI  
- Support batch uploads of PDF files  
- Validate file extensions (only `.pdf`)  
- Sanitize filenames and remove unsafe characters  
- Add timestamps to filenames to prevent collisions  
- Store files to a configurable local `uploads/` directory  

### ✅ Step 2: Preprocessing Layer (Complete)
- Convert PDFs to images using `pdf2image`  
- Apply grayscale + contrast enhancement  
- Binarize images for OCR-readiness  
- Expose `/preprocess/` route for file-based image generation  
- Clean `processed_images/` before each run  

### 🔜 Step 3: Parsing Layer
- Use regex and/or spaCy to extract structured fields (invoice #, date, amount, etc.)  
- Design parser classes per document type (invoices, loan forms, etc.)  
- Build a fallback parser for unknown layouts  

### 🔜 Step 4: Data Storage Layer
- Store structured data in DynamoDB or PostgreSQL  
- Link stored data to original document  
- *(Optional)* Add metadata like upload time, user, processing status  

### 🔜 Step 5: Analytics & Reporting *(Optional)*
- Create a dashboard with Dash, Streamlit, or Superset  
- Add filters, document search, and summary metrics  
- Export parsed data to Excel/CSV  

---

## 🚀 Deployment & DevOps

- Dockerize all services  
- Add `.env` config support and use environment variables  
- Implement S3 storage for cloud deployments  
- Deploy to AWS (ECS, Lambda, or EC2)  

---

## 🔐 Security & Enhancements

- Add API key or token-based authentication  
- Enforce file size limits and MIME-type validation  
- Build an audit log of uploads and extraction results  
- Implement version control for processed files  

---

## 📌 Project Status

✅ **In Progress** – Step 1 & Step 2 complete. Pipeline is modular and future-ready.

---

## 👤 Author

**Firat Demirbulakli**  
[GitHub](https://github.com/) • [Email](mailto:) • [LinkedIn](https://linkedin.com/)
