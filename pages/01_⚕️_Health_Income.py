import streamlit as st
import altair as alt
from altair import datum
from vega_datasets import data
import plotly.express as px
import pandas as pd
from streamlit_extras.echo_expander import echo_expander

url = "https://raw.githubusercontent.com/vega/vega-datasets/main/data/gapminder-health-income.csv"
df = pd.read_csv(url)

st.subheader('Data Sample')
st.caption(f"Count: {len(df)} rows")
st.dataframe(df.head())
st.divider()

# plot 1
st.subheader("Population by region")
with echo_expander(code_location="above", label="code ⚡️"):
    c1 = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "sum(population)",
                axis=alt.Axis(labelExpr='datum.value / 1E9 + "B"'),
                title="Population(Billions)",
            ),
            y=alt.Y("region", sort="-x"),
        )
    )
st.altair_chart(c1, use_container_width=True)
st.divider()

#plot 2
st.subheader("Distribution of Income by region")
with echo_expander(code_location="above", label="code ⚡️"):
    fig = (
        px.histogram(
            df, 
            x="income", 
            facet_col="region", 
            color='region',
            facet_col_wrap = 3,
            facet_col_spacing= 0.05,
            
            )
    )
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()

#plot 3
st.subheader('Relation between Income and Health')
with echo_expander(code_location="above", label="code ⚡️"):
    c2 = (
        alt
        .Chart(df)
        .mark_circle()
        .encode(
            x = alt.X('income', scale=alt.Scale(domain=(0,90000))),
            y = alt.Y('health', scale=alt.Scale(domain=(40,90))),
            size = 'population',
            color = 'region'
        )
        .properties(
            width = 800,
            height = 350
        )
    )
st.altair_chart(c2, use_container_width=True)
st.divider()




