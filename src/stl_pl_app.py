import pandas as pd
import streamlit as st
import plotly.express as px
import polars as pl


# Function to analyze data with polars
def analyze_data(csv_file):
    df = pl.read_csv(csv_file, separator='\t')
    # Pivot the table for easier plotting
    df_long = df.unpivot(
        index=['週'],  # 修正箇所
        on=[
            "python poetry",
            "python venv",
            "python conda",
            "python mamba",
            "python uv",
        ],
        variable_name='variable',
        value_name='value',
    )
    df_long = df_long.rename({'週': 'Week'})
    return df_long.to_pandas()


# Function to create a line plot
def create_line_plot(df):
    fig = px.line(
        df,
        x="Week",  # 修正箇所
        y="value",
        color="variable",
        labels={
            "Week": "週",
            "value": "検索インタレスト",
            "variable": "検索キーワード",
        },
        title="Pythonツールの検索トレンド",
    )
    return fig


# Main Streamlit app
st.title("Python Tool Search Trends")
csv_file_path = "data/csv/multiTimeline.tsv"
df = analyze_data(csv_file_path)
fig = create_line_plot(df)
st.plotly_chart(fig, use_container_width=True)
