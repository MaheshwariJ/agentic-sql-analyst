from app.schema_loader import load_schema_text
from app.agent import SQLAgent


def test_generate_simple_sql():
    schema = load_schema_text()
    agent = SQLAgent(schema)
    sql = agent.generate_sql('Show total amount by country for all time')
    assert 'SELECT' in sql.upper()
