# streamlit_app.py
import streamlit as st
import requests
import pandas as pd
import altair as alt

st.title("Agentic Data Analyst")

question = st.text_input("Ask a data question:")

if st.button("Run"):
    res = requests.post("http://localhost:8000/query", json={"question": question}).json()
    df = pd.DataFrame(res.get("data", []))
    st.write(df)

    # Chart
    if not df.empty and len(df.columns) >= 2:
        if "created_at" in df.columns:
            chart = alt.Chart(df).mark_line().encode(
                x="created_at:T",
                y=df.columns[1]
            )
        else:
            chart = alt.Chart(df).mark_bar().encode(
                x=df.columns[0],
                y=df.columns[1]
            )
        st.altair_chart(chart, use_container_width=True)
    elif not df.empty:
        st.info("Need at least two columns to plot a chart.")
