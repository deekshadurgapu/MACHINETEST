# json_formatter.py
import json
import re

def segment_financial_statements(text):
    """
    Segments the extracted text into standalone and consolidated financial statements.
    Uses regex to look for specific header keywords.
    
    :param text: The complete extracted text.
    :return: A tuple (standalone_statement, consolidated_statement).
    """
    standalone_data = None
    consolidated_data = None

    standalone_match = re.search(
        r"(Standalone Financial Statements[\s\S]+?)(?=Consolidated Financial Statements|$)",
        text, re.IGNORECASE
    )
    consolidated_match = re.search(
        r"(Consolidated Financial Statements[\s\S]+)", text, re.IGNORECASE
    )

    if standalone_match:
        standalone_data = standalone_match.group(1).strip()
    if consolidated_match:
        consolidated_data = consolidated_match.group(1).strip()

    return standalone_data, consolidated_data

def format_to_json(statement_text, statement_type):
    """
    Wraps the financial statement text in a JSON structure.
    
    :param statement_text: The text content of the statement.
    :param statement_type: 'Standalone' or 'Consolidated'.
    :return: A JSON-formatted string.
    """
    data = {
        "statementType": statement_type,
        "content": statement_text
    }
    return json.dumps(data, indent=4)

# json_formatter.py (modified format_tables_to_json)
def format_tables_to_json(tables):
    """
    Converts Camelot Table objects to a list of JSON objects.
    Cleans the extracted text by stripping unnecessary whitespace.
    
    :param tables: List of Camelot Table objects.
    :return: List of cleaned table data.
    """
    tables_json = []
    for table in tables:
        try:
            df = table.df  # Convert the Camelot table to a Pandas DataFrame
            # Clean each cell by stripping extra spaces/newlines
            df_clean = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            table_data = df_clean.to_dict(orient="records")
            tables_json.append(table_data)
        except Exception as e:
            print(f"Error formatting table: {e}")
    return tables_json
