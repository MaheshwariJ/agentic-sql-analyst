# sql_executor.py
import duckdb
import pandas as pd

class SQLExecutor:
    def __init__(self):
        self.con = duckdb.connect("data/sample.db")

    def run(self, sql):
        try:
            df = self.con.execute(sql).df()
            return df, None
        except Exception as e:
            return None, str(e)
