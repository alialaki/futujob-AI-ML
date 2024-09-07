import streamlit as st
import pandas as pd
import json
import requests
import dotenv
from dotenv import load_dotenv

# Security best practice: Store API key securely

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    st.error("Please set the 'RAPID_API_KEY' environment variable.")
    st.stop()

url = "https://jsearch.p.rapidapi.com/search-filters"

querystring = {"query": "Node.js developer in New-York,USA", "date_posted": "all"}

headers = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
}

# Handle potential API errors gracefully
try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
except requests.exceptions.RequestException as e:
    st.error(f"API request failed: {e}")
    st.stop()

st.title(' FutuJob resume tailoring AI app')
st.info('This is app builds a machine learning model!')

# Example: Display sample data (replace with your actual data manipulation)
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Job Title': ['Software Engineer', 'Data Scientist', 'Product Manager']})
st.write(df)

# Handle successful API response
data = response.json()

def download_json_file(json_data, filename="job_search_results.json"):
    """Saves the JSON data to a file."""
    with open(filename, "w") as f:
        json.dump(json_data, f, indent=4)
    st.success(f"JSON data saved to: {filename}")

if st.button("Download JSON Data"):
    download_json_file(data)

st.title("JSON Data (Preview)")
st.code(json.dumps(data, indent=4))  # Display formatted JSON data

# Optionally display individual elements based on API response structure
# for key, value in data.items():
#     st.write(f"**{key}:** {value}")
