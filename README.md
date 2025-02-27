# Financial Statement Extractor

## Overview

This project provides a Gen AI–based solution to extract standalone and consolidated financial statements from PDF documents and convert them into a structured JSON format. The solution leverages freely available Python libraries and system tools, including Tesseract OCR for OCR tasks and Ghostscript for table extraction with Camelot.

The code is designed to handle variations in financial statement formats and can process both digital and scanned PDFs.

## Project Structure


- **pdf_extractor.py:** Contains functions to extract text (with OCR fallback) and tables from PDF files.
- **json_formatter.py:** Contains functions to segment the extracted data into standalone and consolidated statements and format it as JSON.
- **inference.py:** A command-line interface for processing PDFs and outputting JSON for testing purposes.
- **tkinter_app.py:** (Optional) A GUI built with Tkinter to interactively select a PDF and view extracted JSON output.
- **streamlit_app.py:** (Optional) A demo web app built using Streamlit.
- **requirements.txt:** Lists all Python package dependencies.
- **sample_files/:** Contains sample PDFs for testing.

## Tools and Libraries Used

- **Python 3.x**
- **pdfplumber:** For extracting text from PDFs.
- **Camelot (camelot-py[cv]):** For extracting tables from PDFs (requires Ghostscript).
- **pytesseract:** For OCR, using Tesseract.
- **pdf2image:** For converting PDF pages to images for OCR.
- **opencv-python:** For additional image processing if needed.
- **pandas:** For data manipulation.
- **Tkinter:** For building a simple GUI (included with Python).
- **Streamlit:** (Optional) For a web-based demo interface.

## System Dependencies

### Tesseract OCR

Tesseract OCR is required for OCR tasks on scanned PDFs.  
- **Windows:**  
  1. Download the installer from the [Tesseract OCR GitHub releases page](https://github.com/tesseract-ocr/tesseract/releases).  
  2. Install Tesseract (typically installs to `C:\Program Files\Tesseract-OCR`).  
  3. Add the installation directory to your system PATH if not done automatically.
- **macOS:**  
  Install via Homebrew:  
  ```bash
  brew install tesseract
Ghostscript
Ghostscript is required by Camelot for table extraction.

Windows:
Download the installer from the Ghostscript download page.
Install Ghostscript and add the bin folder (e.g., C:\Program Files\gs\gs9.xx\bin) to your system PATH.
