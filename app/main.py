# main.py
from fastapi import FastAPI
from app.agent import SQLAgent
from app.sql_executor import SQLExecutor
from app.schema_loader import load_schema
from pydantic import BaseModel

app = FastAPI()

schema = load_schema()
agent = SQLAgent(schema)
executor = SQLExecutor()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def run_query(payload: QueryRequest):
    question = payload.question
    sql = agent.generate_sql(question)
    df, error = executor.run(sql)

    if error:
        fixed = agent.fix_sql(question, error, sql)
        df, error = executor.run(fixed)
        return {"initial_sql": sql, "fixed_sql": fixed, "error": error,
                "data": df.to_dict(orient="records") if df is not None else None}

    return {"sql": sql, "data": df.to_dict(orient="records")}
