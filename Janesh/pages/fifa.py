import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import pathlib

FILE_PATH = pathlib.Path(__file__)
FILE_DIR = FILE_PATH.cwd()
dir_of_interest = FILE_DIR/"resources"

IMAGE_PATH = dir_of_interest/"images"/"FIFA.jpg"
DATA_PATH = dir_of_interest/"data" / "Fifa.csv"
st.title(":red[Football] Stats Explorer")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)
team = st.selectbox("Select the Team:", df['Teams'].unique())
col1 , col2 = st.columns(2)
fig_1 = px.histogram(df[df['Teams'] == team], x="Pts")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Teams'] == team], y="Pts")
col2.plotly_chart(fig_2, use_container_width=True)

