import requests
import streamlit as st
import pandas as pd
import numpy as np
import os
import re
import json
import csv
from dotenv import load_dotenv, dotenv_values, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv("RAPIDAPI_KEY")

# Check if API key is loaded
if not api_key:
    st.error("API key not found. Please set the RAPIDAPI_KEY environment variable.")
# st.title('Uber pickups in NYC')
st.title('Resume Builder')

#DATE_COLUMN = 'date/time'

url = "https://jsearch.p.rapidapi.com/search"

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

# Get user input for job title and location
job_title = st.text_input("Enter Job Title")


    # Make the API call only if both inputs are valid
querystring = {"query": job_title,
               "page": "1", "num_pages": "1", "date_posted": "all"}
    
response = requests.get(url, headers=headers, params=querystring)

print(response.json())
st.write(response.json())


# Open the JSON file
# with open('jobs_titles.json', 'r') as f:
#     data = json.load(f)

# # Extract the job titles
# job_titles = [job['title'] for job in data['data']]

# Write the job titles to a CSV file
# with open('job_titles.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Job Title'])  # Write header row
#     for title in job_titles:
#         writer.writerow([title])

    # ... rest of your code ...
# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     def lowercase(x): return str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)

