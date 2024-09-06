import streamlit as st
import pandas as pd

st.title('🤖 FutuJob resume tailoring AI app')

st.info('This is app builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/alialaki/data/master/penguins_cleaned.csv')

df
