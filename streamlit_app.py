import requests
import json
import streamlit as st


st.title("Template Co-pilot")

title = st.text_input('Type command here', 'Generate a group template for a consignment type with 1 list and 1 linked-list and 1 heirarchy')

st.button('Generate')
st.divider()
body = """
templateName: consignment_group_template
templateType: group

type: consignment
description: consignment of items
referenceType: CBR
referenceSuffix: Z

data:
  - name: linked-list
    lookUpId: 1
    title: A title for the linked list
    reference:
      templateName: linked_list_1_consignment_template
      templateType: linked_list
  - name: linked-list
    lookUpId: 2
    title: Another title for the linked list
    subTitle: And an optional sub title
    reference:
      templateName: linked_list_2_consignment_template
      templateType: linked_list
  - name: list
    lookUpId: 1
    title: A title for list
    description: >
      A long, optional description that can be added to help explain.
    reference:
      templateName: list_consignment_template
      templateType: list
  - name: hierarchy
    lookUpId: 1
    title: A title fro the hierarchy
    subTitle: A sub title for the hierarchy.
    description: >
      A descriptive body of text to explain more about it.
    reference:
      templateName: hierarchy_template
      templateType: hierarchy
"""
st.code(body, language="yaml", line_numbers=False)
