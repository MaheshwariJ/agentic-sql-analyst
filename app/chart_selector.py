# chart_selector.py
def choose_chart(df):
    # If time series → line chart
    if "date" in df.columns or "created_at" in df.columns:
        return "line"
    # If categorical + numeric → bar chart
    if df.select_dtypes(include=["number"]).shape[1] == 1:
        return "bar"
    return "table"
