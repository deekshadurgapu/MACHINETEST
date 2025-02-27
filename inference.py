# inference.py
import argparse
from pdf_extractor import extract_text, extract_tables
from json_formatter import segment_financial_statements, format_to_json, format_tables_to_json

def main(pdf_path):
    # Step 1: Extract text from the PDF (using OCR if needed)
    print("Extracting text from PDF...")
    text = extract_text(pdf_path)

    # Step 2: Extract tables from the PDF (Camelot will use Ghostscript internally)
    print("Extracting tables from PDF...")
    tables = extract_tables(pdf_path, pages='all', flavor='stream')

    tables_json = format_tables_to_json(tables)
    
    # Step 3: Segment text into standalone and consolidated statements
    print("Segmenting financial statements...")
    standalone_text, consolidated_text = segment_financial_statements(text)
    
    # Step 4: Format segmented text into JSON
    if standalone_text:
        standalone_json = format_to_json(standalone_text, "Standalone")
        print("\n--- Standalone Financial Statement JSON ---")
        print(standalone_json)
    else:
        print("No standalone financial statement found.")
    
    if consolidated_text:
        consolidated_json = format_to_json(consolidated_text, "Consolidated")
        print("\n--- Consolidated Financial Statement JSON ---")
        print(consolidated_json)
    else:
        print("No consolidated financial statement found.")
    
    # Optionally, print extracted tables in JSON format
    if tables_json:
        print("\n--- Extracted Tables JSON ---")
        for i, table in enumerate(tables_json, 1):
            print(f"Table {i}:")
            print(table)
    else:
        print("No tables extracted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract financial statements from a PDF and convert to JSON.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    args = parser.parse_args()
    main(args.pdf_path)
