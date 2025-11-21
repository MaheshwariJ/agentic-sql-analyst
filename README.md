# Agentic SQL Analyst (NL → SQL → Charts)

An agent that converts natural language questions into SQL, executes the SQL against a local DuckDB dataset, attempts automatic fixes for failing queries, and returns a dataframe + suggested visualization.

## Highlights
- NL → SQL using an LLM
- Execution on DuckDB (local demo) with an automatic fix loop
- Simple Streamlit frontend to demo queries + charts
- Clean, modular code for easy extension

## Quickstart
1. Clone the repo
2. Create a virtualenv and activate it

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
3.	Copy .env.example to .env and set OPENAI_API_KEY.
4.	Initialize sample DB (creates data/sample.db):
python data/init_db.py
5.	Run the API server:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
6.	Run the Streamlit frontend in a separate shell:
streamlit run frontend/streamlit_app.py
Open the Streamlit UI at the address printed by Streamlit and try queries like: - “Show approval rate by country for the last 30 days” - “Average transaction amount per country, last month”
Files
See the app/ folder for core logic: agent.py (LLM interaction), sql_executor.py (DuckDB wrapper), schema_loader.py (generate schema text), chart_selector.py (chart heuristics), and main.py (FastAPI playground).
Extending to BigQuery
•	Replace sql_executor.py to call BigQuery client
•	Add authentication and a service-account based config
•	Expand prompts to include dataset-level context

