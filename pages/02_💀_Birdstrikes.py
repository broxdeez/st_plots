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
            color = alt.condition(click, alt.Color('Wildlife Size:O'), alt.value("lightgray"))
        )
        .properties(
            width = 550,
            selection = click
        )
    )
    combine = line_chart & bar_chart
st.altair_chart(combine, use_container_width=True)
st.divider()

st.subheader('Birdstrike count by Airport & Aircraft Type')
with echo_expander(code_location="above", label="code ⚡️"):
    click_1 = alt.selection_single(fields=['Airport Name'])
    top_n_aircraft = df['Aircraft Make Model'].value_counts().index[:10]
    top_n_airport = df['Airport Name'].value_counts().index[:10]
    line = (
        alt.Chart(df[df['Aircraft Make Model'].isin(top_n_aircraft)])
        .mark_bar()
        .encode(
            x = alt.X('count():Q'),
            y = alt.Y('year(Flight Date)'),
            color = alt.Color('Aircraft Make Model:N'),
            order = alt.Order('count()', sort='descending')
        )
        .transform_filter(click_1)
        .properties(
            width = 500
        )
    )
    bar = (
        alt.Chart(df[df['Airport Name'].isin(top_n_airport)])
        .mark_bar()
        .encode(
            x = alt.X('Airport Name', sort='-y'),
            y = 'count()',
            color = alt.condition(click_1, alt.value('indigo'), alt.value('lightgray'))
        )
        .properties(
            selection = click_1,
            width = 500
        )
    )
    combine = line & bar
st.altair_chart(combine, use_container_width=True)
st.divider()



