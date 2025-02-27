# app.py
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from pdf_extractor import extract_text, extract_tables
from json_formatter import segment_financial_statements, format_to_json, format_tables_to_json

def run_extraction(pdf_path):
    """
    Runs the extraction process on the selected PDF file.
    Extracts text and tables, segments the text into standalone and consolidated financial statements,
    and returns a string that contains JSON outputs.
    """
    result = ""
    # Extract text from PDF
    result += "Extracting text from PDF...\n"
    text = extract_text(pdf_path)
    
    # Extract tables using Camelot (Ghostscript is used internally)
    result += "Extracting tables from PDF...\n"
    tables = extract_tables(pdf_path, pages='all', flavor='lattice')
    tables_json = format_tables_to_json(tables)
    
    # Segment text into standalone and consolidated financial statements
    result += "Segmenting financial statements...\n"
    standalone_text, consolidated_text = segment_financial_statements(text)
    
    if standalone_text:
        standalone_json = format_to_json(standalone_text, "Standalone")
        result += "\n--- Standalone Financial Statement JSON ---\n"
        result += standalone_json + "\n"
    else:
        result += "\nNo standalone financial statement found.\n"
    
    if consolidated_text:
        consolidated_json = format_to_json(consolidated_text, "Consolidated")
        result += "\n--- Consolidated Financial Statement JSON ---\n"
        result += consolidated_json + "\n"
    else:
        result += "\nNo consolidated financial statement found.\n"
    
    if tables_json:
        result += "\n--- Extracted Tables JSON ---\n"
        for i, table in enumerate(tables_json, 1):
            result += f"Table {i}:\n{table}\n"
    else:
        result += "\nNo tables extracted.\n"
        
    return result

def select_file():
    """
    Opens a file dialog for the user to select a PDF file, then processes it.
    """
    filepath = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if filepath:
        # Clear previous output
        text_output.delete(1.0, tk.END)
        try:
            # Run the extraction process and show results in the text widget
            result = run_extraction(filepath)
            text_output.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("Financial Statement Extractor")
root.geometry("800x600")

# Create a frame for the button
frame = tk.Frame(root)
frame.pack(pady=10)

# Button to select a PDF file
select_button = tk.Button(frame, text="Select PDF File", command=select_file, width=20, height=2)
select_button.pack()

# Scrollable text widget to display the extraction results
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
text_output.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
