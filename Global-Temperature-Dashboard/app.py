
import plotly.express as px

import pandas as pd
import streamlit as st

url = "https://datahub.io/core/global-temp/_r/-/data/monthly.csv"
df = pd.read_csv(url)

df['Year'] = pd.to_datetime(df['Year'])
df['YearOnly'] = df['Year'].dt.year

df = df.dropna()

st.title("Global Temperature Dashboard")
st.write("This app shows how global temperatures have changed over time.")

min_year = int(df['YearOnly'].min())
max_year = int(df['YearOnly'].max())

year_range = st.sidebar.slider("Select year range", min_year, max_year, (min_year, max_year))

filtered_df = df[(df['YearOnly'] >= year_range[0]) & (df['YearOnly'] <= year_range[1])]
fig = px.line(filtered_df, x="Year", y="Mean", title="Temperature Change Over Time")
st.plotly_chart(fig)
with st.expander("Show raw data"):
    st.write(filtered_df)

