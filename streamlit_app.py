import streamlit as st
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
            4. Rate the table to help improve future outputs.
            5. Optionally, download the table as a CSV file.
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

    # Session state for CSV output
    if "csv_output" not in st.session_state:
        st.session_state.csv_output = None

    # Generate Button
    if st.button("Generate LCA Table"):
        st.session_state.csv_output = create_csv_output(query)

    # Output Section
    if st.session_state.csv_output:
        st.header("LCA Table Output")
        st.success("✅ Table generated successfully!")
        
        # Display CSV as plain text
        st.text(st.session_state.csv_output)

        # Rating System
        st.subheader("Rate the Table")
        rating = st.slider("How would you rate the table?", min_value=1, max_value=5, value=3, step=1)
        feedback = st.text_area("Additional Feedback (optional)", placeholder="E.g., The table looks good, but some units are incorrect.")
        
        if st.button("Submit Feedback"):
            # Collect feedback into a local list (can be saved to a database)
            if "feedback_data" not in st.session_state:
                st.session_state.feedback_data = []
            
            # Append feedback
            st.session_state.feedback_data.append({
                "Query": query,
                "Rating": rating,
                "Feedback": feedback
            })
            st.success("Thank you for your feedback! It has been recorded.")
        
        # Feedback Display (for debugging/tracking purposes)
        if st.session_state.feedback_data:
            st.subheader("Collected Feedback (Preview)")
            st.write(pd.DataFrame(st.session_state.feedback_data))

        # Download Section
        @st.cache_data
        def convert_df_to_csv(dataframe):
            return dataframe.to_csv(index=False, sep=";")

        st.download_button(
            label=" Download LCA Table as CSV",
            data=st.session_state.csv_output,
            file_name="lca_output.csv",
            mime="text/csv",
        )
    
    # Footer Section
    st.markdown("---")
    st.markdown(
        """
        **Developed by [Your Name or Organization](#)**  
        💡 Empowering sustainable decision-making through data-driven LCAs.  
        """
    )

# Run the app
if __name__ == "__main__":
    main()
