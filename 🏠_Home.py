import streamlit as st
import altair as alt
from vega_datasets import data
import pandas as pd

st.title('Interactive Data Viz')

'''
 This demo uses data from [Vega Datasets](https://github.com/vega/vega-datasets/tree/main/data) to visualize different plot types
 using the [Vega-Altair](https://altair-viz.github.io/index.html) / [Plotly](https://plotly.com/python/plotly-express/) library
'''

'''
 The sidebar 👈 lists the datasets that are analyzed and it follows the below format
    - View sample data
    - Summary Statistics
    - Plots
'''