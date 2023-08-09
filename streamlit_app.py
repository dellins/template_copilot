import requests
import json
import streamlit as st


st.title("Template Co-pilot")

title = st.text_input('Type command here', 'Generate a group template for a consignment type with 1 list and 1 linked-list and 1 heirarchy')

st.button('Generate')
