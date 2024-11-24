import streamlit as st
import pandas as pd
from io import StringIO

# Function to create CSV output (mock data)
def create_csv_output(query):
    mock_data = """
Activity database;Activity code;Activity name;Activity unit;Activity Location;Activity type;Exchange database;Exchange code;Exchange amount;Exchange unit;Exchange type;Exchange uncertainty type;Exchange loc;Exchange scale;Exchange negative;Notes
new_db;ElectricCar1;Driving of Car;km;Global;Process;new_db;Driving of Car;1;km;Production;NAN;NAN;NAN;NAN;"Driving 1 km in the car's lifetime"
new_db;ElectricCar1;Driving of Car;km;Global;Process;eco-invent;fuel for driving car;1;liter;Technosphere;NAN;NAN;NAN;NAN;"Input: 1 liter of fuel used"
new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;aluminum for car;500;kg;Technosphere;500/900;kg;NAN;NAN;NAN;"Input: 500/900 kg of aluminum for creating car"
new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;copper for car;100;kg;Technosphere;100/900;kg;NAN;NAN;NAN;"Input: 100/900 kg of copper for creating car"
    """
    return mock_data

# Mock-up for LCA Results (CO2 Emissions, Energy, etc.)
def generate_lca_results(query, feedback_incorporated=False):
    # Based on feedback, the results might change
    if feedback_incorporated:
        # If feedback was incorporated, modify results (e.g., adjust CO2 emissions)
        results = {
            "CO₂ Emissions (kg)": 130.0,  # adjusted from original value
            "Energy Consumption (kWh)": 35.0,
            "Water Use (L)": 190.0,  # adjusted
            "Material Use (kg)": 590.0  # adjusted
        }
    else:
        # Default results
        results = {
            "CO₂ Emissions (kg)": 150.0,
            "Energy Consumption (kWh)": 35.0,
            "Water Use (L)": 200.0,
            "Material Use (kg)": 600.0
        }
    return results

# Streamlit App
def main():
    # App Title and Description
    st.title("🌍 Life Cycle Assessment (LCA) Generator")
    st.write(
        """
        Welcome to the **LCA AI Machine**! This app helps you generate detailed Life Cycle Assessment (LCA) tables 
        based on your query. Provide a description of your scenario, and we'll generate an interactive, downloadable LCA table.
        """
    )

    # Sidebar for Instructions
    with st.sidebar:
        st.header("How to Use")
        st.markdown(
            """
            1. Enter your query describing the LCA scenario in the text box.
            2. Click **Generate LCA Table** to process your query.
            3. View the table output below.
            4. Provide feedback on the generated table.
            5. Optionally, validate whether the feedback should be used for the final LCA result.
            6. Download the final LCA report.
            """
        )
        st.info("🔍 Tip: Be as detailed as possible in your query for better results!")

    # Query Input Section
    st.header("Enter Your LCA Scenario")
    query = st.text_area(
        "Describe the scenario you want to analyze:",
        placeholder="Example: I want to create an LCA for a car driving 900 km. It uses 200 kg of fuel...",
        height=150,
    )

    # Session state for CSV output and feedback
    if "csv_output" not in s
