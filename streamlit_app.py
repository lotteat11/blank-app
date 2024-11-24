import streamlit as st
import os
import os
import pandas as pd
from langchain_community.chat_models import ChatOllama 
from langchain import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

# List of queries
queries = [
    "Prepare a table for an LCA to assess the environmental impact of a diesel bus per kilometer traveled. The bus is expected to travel a total of 200,000 km over its lifetime. Include the production phase with 3,000 kg of steel and 500 kg of rubber. Account for 40,000 liters of diesel fuel consumed during operations, sourced from the technosphere. Exclude biosphere emissions.",
    "Prepare a table for an LCA to assess the environmental impact of a wind farm per year. The wind farm generates 1,000 MWh of electricity annually over 20 years. Include the production phase with 2,000 kg of aluminum and 500 kg of steel. Account for 20 liters of lubricants annually, sourced from the technosphere. Exclude biosphere emissions.",
    # Add more queries as needed
]

# Streamlit app title
st.title("LCA Queries Writer")

# Displaying the queries
st.header("Queries")
for i, query in enumerate(queries, start=1):
    st.write(f"**Query {i}:** {query}")

# File writing
st.header("Save Queries to File")

# Input for file name
file_name = st.text_input("Enter the file name", "lca_queries_responses.csv")

if st.button("Save to File"):
    # Create the file
    output_directory = "outputs"
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, file_name)

    with open(output_path, "w", encoding="utf-8") as file:
        for query in queries:
            file.write(f"{query}\n")

    st.success(f"Queries successfully saved to {output_path}")
