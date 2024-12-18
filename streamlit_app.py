import streamlit as st
import pandas as pd
from io import StringIO

# Function to create CSV output (mock data)
def create_csv_output(query):
    mock_data = """
Activity database;Activity code;Activity name;Activity unit;Activity Location;Activity type;Exchange database;Exchange code;Exchange amount;Exchange unit;Exchange type;Exchange uncertainty type;Exchange loc;Exchange scale;Exchange negative;Notes
new_db;ElectricCar1;Driving of Car;km;Global;Process;new_db;Driving of Car;1;km;Production;NAN;NAN;NAN;NAN;"Driving 1 km in the car's lifetime"
new_db;ElectricCar1;Driving of Car;km;Global;Process;eco-invent;fuel for driving car;1;liter;Technosphere;NAN;NAN;NAN;NAN;"Input: 1 liter of fuel used"
new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;aluminum for car;500;kg;Technosphere;500/900;NAN;NAN;NAN;"Input: 500/900 kg of aluminum for creating car"
new_db;ElectricCar1;Driving of Car;kg;Global;Process;eco-invent;copper for car;100;kg;Technosphere;100/900;NAN;NAN;NAN;"Input: 100/900 kg of copper for creating car"
    """
    return mock_data

# Convert CSV to DataFrame
def convert_csv_to_df(csv_data):
    try:
        # Read CSV string into DataFrame, handle semicolon delimiter and quotechar for handling quotes
        df = pd.read_csv(StringIO(csv_data), sep=";", quotechar='"')
        return df
    except Exception as e:
        st.error(f"Error while parsing the CSV data: {e}")
        return None

# Function to convert DataFrame to CSV for download
@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False, sep=";")

# Streamlit App
def main():
    st.title("🌍 LCA Generator")
    st.write(
        """
        Welcome to the **LCA AI Machine**!  This app helps you generate detailed Life Cycle Assessment (LCA) tables 
        based on your query. Unfortunately this is all fake - but imagine this; Provide a description of your scenario, and we'll generate an interactive, downloadable LCA table.
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
        placeholder="Example: Prepare a table for an LCA to assess the environmental impact of a diesel bus per kilometer traveled. The bus is expected to travel a total of 200,000 km over its lifetime. Include the production phase with 3,000 kg of steel and 500 kg of rubber. Account for 40,000 liters of diesel fuel consumed during operations, sourced from the technosphere. Exclude biosphere emissions....",
        height=150,
    )

    if "csv_output" not in st.session_state:
        st.session_state.csv_output = None

    if st.button("Prepare data"):
        st.session_state.csv_output = create_csv_output(query)

    if st.session_state.csv_output:
        st.header("Data preparation")
        st.success("✅ Table generated successfully!")

        # Convert CSV to DataFrame and display it as a clean table
        df = convert_csv_to_df(st.session_state.csv_output)

        # Check if DataFrame is valid
        if df is not None:
            st.dataframe(df, use_container_width=True)

            # Provide feedback options
            st.subheader("Feedback and iteration")
            rating = st.slider("How would you rate the table?", min_value=1, max_value=5, value=3, step=1)
            feedback = st.text_area("Additional Feedback (optional)", placeholder="E.g., The table looks good, but some units are incorrect.")

            if "feedback_data" not in st.session_state:
                st.session_state.feedback_data = []

            # Confirm if feedback should be included
            include_feedback = st.checkbox("Use the currecnt data version final result - next step would be background data matching - skip for now")

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

                # Mock LCA Results (CO2, Method, etc.)
                st.write("**Estimated CO2 Emissions**: 120 kg CO2")
                st.write("**Background data Used**: EcoInvent 3.8")
                st.write("**LCA Type**: Carbon Footprint Analysis")
                st.write("**Notes**: Assumptions based on average car fuel consumption over 900 km")

                # Create a professional table showing the results
                result_data = {
                    "Material/Activity": ["Fuel for Driving", "Aluminum for Car", "Copper for Car"],
                    "Amount": ["1 liter", "500 kg", "100 kg"],
                    "CO2 Emission (kg)": [0.23, 1.1, 0.2],
                    "Energy Consumption (MJ)": [5.5, 20.0, 12.5],
                    "Water Usage (liters)": [0.5, 400, 50],
                    "Recycling Potential (%)": [50, 90, 80]
                }

                result_df = pd.DataFrame(result_data)

                st.subheader("LCA Results Table")
                st.dataframe(result_df, use_container_width=True)

                # Add the download button for the final LCA table
                st.download_button(
                    label="📥 Download Final LCA Report as CSV",
                    data=convert_df_to_csv(result_df),
                    file_name="final_lca_report.csv",
                    mime="text/csv"
                )

    # Footer Section
    st.markdown("---")
    st.markdown(
        """
        **Developed by LCS in AAU And XXX(#)**  
        💡 Empowering sustainable decision-making through data-driven LCAs.  
        """
    )

if __name__ == "__main__":
    main()
