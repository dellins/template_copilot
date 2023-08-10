import requests
import json
import streamlit as st

def consume_url(message, history):
    url = "https://y9s346bpuj.execute-api.us-east-1.amazonaws.com/default/bedrock_opensearch_demo"
    body = {
        "message": message,
        "history": history,
        "action": 'template'
    }
    headers = {'Content-Type': 'application/json', 'x-api-key': 'LF1LAK6AKF9Zk1gJMRWKZ5ERJ2oMraAf6V58owSt'}
    response = requests.post(url, headers=headers, data=json.dumps(body))
    
    if response.status_code == 200:
        data = response.json()

        # Process the data as needed
        print(data)

        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)

st.title("Template Co-pilot")

title = st.text_input('Type command here', 'Generate a group template for a consignment type with 1 list and 1 linked-list')

response = consume_url(title, "")

body = response['body']['message']

st.button('Generate')
st.divider()

st.code(body, language="yaml", line_numbers=False)
