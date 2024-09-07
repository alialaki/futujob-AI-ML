import streamlit as st
import pandas as pd
import json
import requests
import dotenv
from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

url = "https://jsearch.p.rapidapi.com/search-filters"

querystring = {"query":"Node.js developer in New-York,USA","date_posted":"all"}

headers = {
	"x-rapidapi-key": "RAPID_API_KEY",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)



st.title('🤖 FutuJob resume tailoring AI app')

st.info('This is app builds a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/alialaki/data/master/penguins_cleaned.csv')
df


data = response.json()

def main():
    st.title("JSON Data")

    # Display the JSON data as a formatted string
    st.code(json.dumps(data, indent=4))

    # Optionally, display individual elements from the JSON data
    for key, value in data.items():
        st.write(f"**{key}:** {value}")

if __name__ == "__main__":
    main()

