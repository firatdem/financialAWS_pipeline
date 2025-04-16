import pytesseract
from PIL import Image
from pathlib import Path
import json
import re


def extract_fields(text: str) -> dict:
    # (same as your current implementation, no changes needed)
    fields = {
        "order_id": None,
        "customer_id": None,
        "order_date": None,
        "contact_name": None,
        "address": None,
        "city": None,
        "postal_code": None,
        "country": None,
        "phone": None,
        "fax": None,
        "total_price": None
    }

    patterns = {
        "order_id": r"Order ID:\s*(\d+)",
        "customer_id": r"Customer ID:\s*(\w+)",
        "order_date": r"Order Date:\s*([\d\-]+)",
        "contact_name": r"Contact Name:\s*(.+)",
        "address": r"Address:\s*(.+)",
        "city": r"City:\s*(.+)",
        "postal_code": r"Postal Code:\s*(\d+)",
        "country": r"Country:\s*(.+)",
        "phone": r"Phone:\s*(\([0-9]+\)\s*[0-9\-]+)",
        "fax": r"Fax:\s*(\S+)",
        "total_price": r"TotalPrice\s*([\d.,]+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            value = match.group(1).strip()
            if key == "total_price":
                try:
                    numeric_value = float(value.replace(",", ""))
                    value = "${:,.2f}".format(numeric_value)
                except ValueError:
                    value = None
            fields[key] = value
    return fields


def run_ocr_and_parse_single(filename: str) -> dict:
    """
    Process a single .png file from processed_images/ and save parsed output to parsed_results/
    """
    image_path = Path(__file__).resolve().parents[1] / "preprocessing_service" / "processed_images" / filename
    if not image_path.exists():
        raise FileNotFoundError(f"Image file '{filename}' not found.")

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    parsed = extract_fields(text)

    output_dir = Path(__file__).resolve().parent / "parsed_results"
    output_dir.mkdir(exist_ok=True)

    out_path = output_dir / f"{image_path.stem}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(parsed, f, indent=2)

    return parsed
