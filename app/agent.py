# agent.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

SQL_SYSTEM_PROMPT = """
You are a senior SQL expert.
Follow rules:
- Only use tables & columns from the schema.
- Output ONLY SQL.
- Never guess nonexistent columns.
"""

class SQLAgent:
    def __init__(self, schema):
        self.schema = schema

    def generate_sql(self, user_query):
        resp = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": SQL_SYSTEM_PROMPT},
                {"role": "user", "content": f"Schema:\n{self.schema}\n\nQuestion: {user_query}"}
            ]
        )
        return resp.choices[0].message.content.strip()

    def fix_sql(self, user_query, error, previous_sql):
        prompt = f"""
SQL failed with error:
{error}

SQL:
{previous_sql}

Fix the SQL. Output ONLY corrected SQL.
"""
        resp = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": SQL_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
        return resp.choices[0].message.content.strip()
