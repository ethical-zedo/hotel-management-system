import sqlite3
from pathlib import Path

DB_NAME = "hotel.db"

def execute_script(sql_file: str):
    """Run the DDL (and optionally INSERTS) located in `sql_file`."""
    with sqlite3.connect(DB_NAME) as conn, open(sql_file, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    print("✓ Database created / refreshed:", DB_NAME)

if __name__ == "__main__":
    # ❶ build empty schema
    execute_script("schema_sqlite.sql")      # Creates the schema
    execute_script("sample_data.sql")   

    # ❷ OPTIONAL — populate the tables with the sample data from the PDF.
    #    Copy the INSERT statements into `sample_data.sql`
    #    and uncomment the next line.
    # execute_script("sample_data.sql")
