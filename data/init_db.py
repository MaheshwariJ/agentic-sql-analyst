import duckdb
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent
DB_PATH = DATA_DIR / 'sample.db'
CSV_PATH = DATA_DIR / 'sample_data.csv'

if __name__ == '__main__':
    # Let pandas infer everything correctly
    df = pd.read_csv(CSV_PATH, sep=',', header=0)

    print(df.head())

    # Ensure boolean column is actual bool (Pandas sometimes makes object)
    df['approved'] = df['approved'].astype('bool')
    df['created_at'] = pd.to_datetime(df['created_at'])
    print(df.dtypes)


    con = duckdb.connect(str(DB_PATH))
    print(con.execute("SELECT * FROM transactions").fetchdf())

    # Best + safest way:
    con.execute("DROP TABLE IF EXISTS transactions;")
    con.register("df_view", df)
    print(df.head())
    con.execute("CREATE TABLE transactions AS " +
    "SELECT * " +
    "FROM df_view;")

    print(f"Created {DB_PATH}")
