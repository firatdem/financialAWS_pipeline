from pdf2image import convert_from_path
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
from ingestion_service.config import UPLOAD_DIR
import os

# Define where to save temporary images
OUTPUT_DIR = Path(__file__).resolve().parent / "processed_images"
OUTPUT_DIR.mkdir(exist_ok=True)


def clear_output_folder(folder: Path):
    """
    Removes all PNG images in the given output folder.
    """
    for file in folder.glob("*.png"):
        file.unlink()


def enhance_image(img: Image.Image) -> Image.Image:
    """
    Applies grayscale, contrast enhancement, and binarization to the image.
    """
    # Convert to grayscale
    img = img.convert("L")

    # Enhance contrast slightly
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.5)

    # Binarize (threshold)
    img = img.point(lambda x: 0 if x < 180 else 255, '1')  # Simple black/white threshold

    return img


def pdf_to_images(pdf_path: str) -> list:
    """
    Converts a PDF into a list of enhanced image paths (one per page).
    Saves images as PNGs in OUTPUT_DIR.
    """
    if not Path(pdf_path).exists():
        print(f"[ERROR] File not found: {pdf_path}")
        return []

    # Clear old image files before processing
    clear_output_folder(OUTPUT_DIR)

    try:
        pages = convert_from_path(pdf_path, dpi=300)
    except Exception as e:
        print(f"[ERROR] Failed to convert PDF: {e}")
        return []

    image_paths = []
    base_name = Path(pdf_path).stem

    for i, page in enumerate(pages):
        # Enhance each page before saving
        enhanced = enhance_image(page)

        img_filename = f"{base_name}_page_{i+1}.png"
        img_path = OUTPUT_DIR / img_filename
        enhanced.save(img_path, "PNG")

        image_paths.append(str(img_path))

    return image_paths
