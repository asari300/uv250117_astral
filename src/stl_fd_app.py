import pandas as pd
import streamlit as st
import plotly.express as px
import fireducks.pandas as fd


# Function to analyze data with fireducks
def analyze_data(csv_file):
    df = fd.read_csv(csv_file, sep='\t')
    # Pivot the table for easier plotting
    df_long = df.melt(id_vars=['週'], var_name='variable', value_name='value')
    return df_long


# Function to create a line plot
def create_line_plot(df):
    fig = px.line(
        df,
        x="週",
        y="value",
        color="variable",
        labels={"週": "Week", "value": "Search Interest", "variable": "Search Term"},
        title="Search Trends for Python Tools",
    )
    return fig


# Main Streamlit app
st.title("Python Tool Search Trends")
csv_file_path = "data/csv/multiTimeline.tsv"
df = analyze_data(csv_file_path)
fig = create_line_plot(df)
st.plotly_chart(fig, use_container_width=True)
