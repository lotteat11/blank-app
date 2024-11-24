import streamlit as st
import pandas as pd
from io import StringIO

# Function to create CSV output
def create_csv_output(query):
    mock_data = """
    Activity database;Activity code;Activity name;Activity unit;Activity Location;Activity type;Exchange database;Exchange code;Exchange amount;Exchange unit;Exchange type;Exchange uncertainty type;Exchange loc;Exchange scale;Exchange negative;Notes
    new_db;ElectricCar1;Driving of Car;km;Global;Process;new_db;Driving of Car;1;km;Production;NAN;NAN;NAN;NAN;"Driving 1 km in the car's lifetime"
    new_db;ElectricCar1;Driving of Car;km;Global;Process;eco-invent;fuel for driving car;1;liter;Technosphere;NAN;NAN;NAN;NAN;"Input: 1 liter of fuel used"
    new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;aluminum for car;500;kg;Technosphere;500/900;kg;NAN;NAN;NAN;"Input: 500/900 kg of aluminum for creating car"
    new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;copper for car;100;kg;Technosphere;100/900;kg;NAN;NAN;NAN;"Input: 100/900 kg of copper for creating car"
    """
    return mock_data

# Convert CSV to DataFrame
def convert_csv_to_df(csv_data):
    return pd.read_csv(StringIO(csv_data), sep=";")

# Streamlit App
def main():
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

    # Query Input Section
    query = st.text_area(
        "Describe the scenario you want to analyze:",
        placeholder="Example: I want to create an LCA for a car driving 900 km. It uses 200 kg of fuel...",
        height=150,
    )

    if "csv_output" not in st.session_state:
        st.session_state.csv_output = None

    if st.button("Generate LCA Table"):
        st.session_state.csv_output = create_csv_output(query)

    if st.session_state.csv_output:
        st.header("LCA Table Output")
        st.success("✅ Table generated successfully!")

        # Display the table as text (can be customized later)
        st.text(st.session_state.csv_output)

        # Collect feedback
        st.subheader("Provide Feedback on the Table")
        rating = st.slider("How would you rate the table?", min_value=1, max_value=5, value=3, step=1)
        feedback = st.text_area("Additional Feedback (optional)", placeholder="E.g., The table looks good, but some units are incorrect.")

        if "feedback_data" not in st.session_state:
            st.session_state.feedback_data = []

        # Confirm if feedback should be included
        include_feedback = st.checkbox("Include feedback in final result")

        if include_feedback and st.button("Submit Feedback"):
            st.session_state.feedback_data.append({
                "Query": query,
                "Rating": rating,
                "Feedback": feedback
            })
            st.success("Thank you for your feedback!")

        # Show the feedback if the checkbox is selected
        if include_feedback and st.session_state.feedback_data:
            st.subheader("Final Feedback and Validation")
            st.write(pd.DataFrame(st.session_state.feedback_data))

        # Show Final Result (LCA Summary, CO2 Emission, etc.)
        if include_feedback:
            st.subheader("Final LCA Result Summary")
            st.write(f"### Query Summary: {query}")

            # Mock LCA Results (CO2, Method, etc.)
            st.write("**Estimated CO2 Emissions**: 120 kg CO2")
            st.write("**Method Used**: EcoInvent 3.8")
            st.write("**LCA Type**: Carbon Footprint Analysis")
            st.write("**Notes**: Assumptions based on average car fuel consumption over 900 km")

    # Footer Section
    st.markdown("---")
    st.markdown(
        """
        **Developed by [Your Name or Organization](#)**  
        💡 Empowering sustainable decision-making through data-driven LCAs.  
        """
    )

if __name__ == "__main__":
    main()
