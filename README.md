# Financial Document Processing Pipeline

A modular, cloud-ready pipeline designed to ingest, process, and extract structured data from financial documents like invoices, loan applications, and bank statements. Built with a focus on clean architecture, scalability, and future AWS deployment.

---

## Current Features (Ingestion Layer Complete)

### Step 1: Ingestion Layer

- **Built with FastAPI** to expose a secure `/upload/` REST API.
- Supports **batch PDF uploads** via multipart form data.
- Performs **extension validation** (only `.pdf` allowed).
- Automatically **sanitizes filenames** to strip dangerous characters.
- Appends **timestamps** to avoid filename collisions and track uploads.
- Stores files to a configurable local `uploads/` directory.

---

## How to Run

```bash
cd ingestion_service
pip install -r requirements.txt
python main.py
```

Visit the interactive docs: http://127.0.0.1:8000/docs

## Example Upload Response
```bash
{
  "message": "2 files uploaded successfully.",
  "paths": [
    "uploads/20250415_142314_invoice_april_2024.pdf",
    "uploads/20250415_142402_invoice_march.pdf"
  ]
}
```

## Tech Stack
```bash
Python 3.x
FastAPI
Uvicorn
Async file handling
Modular structure (future Docker + AWS ready)
```

## Roadmap

### ✅ Step 1: Ingestion Layer (Complete)
- [x] Build `/upload/` REST endpoint with FastAPI
- [x] Support batch uploads of PDF files
- [x] Validate file extensions (only `.pdf`)
- [x] Sanitize filenames and remove unsafe characters
- [x] Add timestamps to filenames to prevent collisions
- [x] Store files to a configurable local `uploads/` directory

---

### Step 2: Preprocessing Layer (Next)
- [ ] Split multi-page PDFs into individual pages (if needed)
- [ ] Perform OCR using Tesseract (or Textract for AWS)
- [ ] Enhance scanned images (deskew, binarize, clean)
- [ ] Store raw OCR output for further parsing

---

### Step 3: Parsing Layer
- [ ] Use regex and/or spaCy to extract structured fields (invoice #, date, amount, etc.)
- [ ] Design parser classes per document type (invoices, loan forms, etc.)
- [ ] Build a fallback parser for unknown layouts

---

### Step 4: Data Storage Layer
- [ ] Store structured data in DynamoDB or PostgreSQL
- [ ] Link stored data to original document
- [ ] Optional: Add metadata like upload time, user, processing status

---

### Step 5: Analytics & Reporting (Optional)
- [ ] Create a dashboard with Dash, Streamlit, or Superset
- [ ] Add filters, document search, and summary metrics
- [ ] Export parsed data to Excel/CSV

---

### Deployment & DevOps
- [ ] Dockerize all services
- [ ] Add `.env` config support and use environment variables
- [ ] Implement S3 storage for cloud deployments
- [ ] Deploy to AWS (ECS, Lambda, or EC2)

---

### Security & Future Enhancements
- [ ] Add API key or token-based authentication
- [ ] Enforce file size limits and MIME-type validation
- [ ] Build an audit log of uploads and extraction results
- [ ] Implement version control for processed files

---

## Project Status
> **In Progress** – Step 1 complete. Remaining steps outlined and modular architecture established.

---

## Author

**Firat Demirbulakli**  
[GitHub](https://github.com/firatdem) • [Email](mailto:firat.demirbulakli97@outlook.com) • [Linkedin](https://www.linkedin.com/in/firat-demirbulakli-4361302a8/)
