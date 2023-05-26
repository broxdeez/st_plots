import streamlit as st
import altair as alt
from altair import datum
from vega_datasets import data
import plotly.express as px
import pandas as pd
from streamlit_extras.echo_expander import echo_expander

alt.data_transformers.disable_max_rows()

url = "https://raw.githubusercontent.com/vega/vega-datasets/main/data/birdstrikes.csv"
df = pd.read_csv(url,encoding='UTF-8')

st.subheader('Sample Data')
st.caption(f"Count: {len(df)} rows")
st.dataframe(df.head())
st.divider()

st.subheader("")
with echo_expander(code_location="above", label="code ⚡️"):
    click = alt.selection_single(fields=['Wildlife Size'])
    line_chart = (
        alt.Chart(df)
        .mark_line()
        .encode(
            x = 'year(Flight Date):T',
            y = 'count()',
            color = 'Phase of flight'
        )
        .transform_filter(
            click
        )
        .properties(
            width = 550
        )
    )
    bar_chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            y = alt.X('Wildlife Size', sort='-x'),
            x = 'count()',
            color = alt.condition(click, 'Wildlife Size', alt.value("lightgray"))
        )
        .properties(
            width = 550,
            selection = click
        )
    )
    combine = line_chart & bar_chart
st.altair_chart(combine, use_container_width=True)