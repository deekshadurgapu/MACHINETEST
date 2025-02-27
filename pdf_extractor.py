# pdf_extractor.py
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import camelot

def extract_text(pdf_path):
    """
    Extracts text from the PDF.
    For each page, it first attempts to extract text using pdfplumber.
    If the extracted text is minimal (likely a scanned image), it converts the page to an image and applies OCR.
    
    :param pdf_path: Path to the PDF file.
    :return: Combined text from all pages.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            # If text is very short, assume it's a scanned page and use OCR
            if len(page_text.strip()) < 20:
                try:
                    # Convert only the current page to an image
                    images = convert_from_path(pdf_path, first_page=i, last_page=i)
                    if images:
                        ocr_text = pytesseract.image_to_string(images[0])
                        page_text = ocr_text
                except Exception as e:
                    print(f"Error during OCR on page {i}: {e}")
            text += page_text + "\n"
    return text

def extract_tables(pdf_path, pages='all', flavor='stream'):
    """
    Extracts tables from the PDF using Camelot.
    :param pdf_path: Path to the PDF file.
    :param pages: Pages to extract tables from (default 'all').
    :param flavor: 'lattice' for bordered tables, 'stream' for borderless tables.
    :return: List of Camelot Table objects.
    """
    try:
        tables = camelot.read_pdf(pdf_path, pages=pages, flavor=flavor)
        return tables
    except Exception as e:
        print(f"Error extracting tables: {e}")
        return []