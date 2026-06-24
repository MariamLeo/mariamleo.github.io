import streamlit as st

import pandas as pd

import requests



# Paste your Web App URL here

SHEET_API_URL = "https://script.google.com/macros/s/AKfycbxWE4pfBon26_K4HgxpGwAtTK5lymFYh0e9t9CnNnN8t7X3CicZKl2Tp-flMEXHzUI7/exec"



def load_data():

    response = requests.get(SHEET_API_URL)

    data = response.json()

    return pd.DataFrame(data)



st.title("User Location Dashboard")



try:

    df = load_data()

    

    # Process the data

    counts = df.groupby(['Country', 'Postcode']).size().reset_index(name='Count')

    counts['Label'] = counts['Country'] + ' - ' + counts['Postcode'].astype(str)

    

    # Visualization

    st.bar_chart(counts.set_index('Label')['Count'])

    

except Exception as e:

    st.write("Could not load data. Check your Web App URL.")