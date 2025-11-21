# schema_loader.py
import duckdb

def load_schema():
    con = duckdb.connect("data/sample.db")
    tables = con.execute("SHOW TABLES").fetchall()

    schema_text = ""
    for (table,) in tables:
        cols = con.execute(f"DESCRIBE {table}").fetchall()
        schema_text += f"TABLE {table}:\n"
        for name, dtype, *_ in cols:
            schema_text += f" - {name}: {dtype}\n"
        schema_text += "\n"
    return schema_text
