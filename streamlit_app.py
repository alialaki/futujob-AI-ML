import streamlit as st
import pandas as pd
import json
import requests

url = "https://jsearch.p.rapidapi.com/search-filters"

querystring = {"query":"Node.js developer in New-York,USA","date_posted":"all"}

headers = {
	"x-rapidapi-key": "673b3befb0mshea186ed7da8eb81p1fd395jsnae3d478a96fb",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



st.title('🤖 FutuJob resume tailoring AI app')

st.info('This is app builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/alialaki/data/master/penguins_cleaned.csv')
df


response = response.json()

st.write(resonse)

