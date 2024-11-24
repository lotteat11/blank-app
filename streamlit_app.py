import streamlit as st
import csv
from io import StringIO

# Your function to create CSV output
def create_csv_output(query):
    mock_data = """
    Activity database; Activity code; Activity name; Activity unit; Activity Location; Activity type; Exchange database; Exchange code; Exchange amount; Exchange unit; Exchange type; Exchange uncertainty type; Exchange loc; Exchange scale; Exchange negative; Notes
    new_db;ElectricCar1;Driviving of Car;km;Global;Process;new_db;Driviving of Car;1;km;Production;NAN;NAN;NAN;NAN;"Driving 1 km in the car's lifetime"
    new_db;ElectricCar1;Driviving of Car;km;Global;Process;eco-invent;fuel for driving car;1;liter;Technosphere;NAN;NAN;NAN;NAN;"Input: 1 liter of fuel used"
    new_db;ElectricCar1;Driviving of Car;kg;Global;Process;eco-invent;aluminum for car;500;kg;Technosphere;500/900;kg;NAN;NAN;NAN;"Input: 500/900 kg of aluminum for creating car"
    new_db;ElectricCar1;Driviving of Car;kg;Global;Process;eco-invent;copper for car;100;kg;Technosphere;100/900;kg;NAN;NAN;NAN;"Input: 100/900 kg of copper for creating car"
    """
    return mock_data

# Streamlit App
def main():
    st.title("LCA AI MACHINE")

    # User Input for query
    query = st.text_area("Enter your LCA Query", "I want to create a LCA for a car driving 900 km. It uses 200 kg of fuel...")

    # Create session state for CSV output
    if "csv_output" not in st.session_state:
        st.session_state.csv_output = None

    # When the button is pressed, generate the CSV output
    if st.button("Generate LCA Table"):
        # Call the function with the query input
        st.session_state.csv_output = create_csv_output(query)

    # Show the CSV output if it exists in session state
    if st.session_state.csv_output:
        st.subheader("LCA Table Output")
        st.text(st.session_state.csv_output)

        st.text("Please rate the matrix 1-5.")
        rating = st.text_input("Rate the table:", "")

        if rating:
            st.write(f"Thank you for rating the table: {rating}")

            st.text_area("Do you want to continue?", "Yes...")

            if st.button("Matching"):
                st.subheader("Find Relevant Background Data")
                st.text("This data is correct")
                st.subheader("Result")

                # Allow user to download the CSV file
                @st.cache_data
                def convert_to_csv(data):
                    csv_file = StringIO()
                    csv_writer = csv.writer(csv_file, delimiter=";")
                    for row in data.splitlines():
                        csv_writer.writerow(row.split(";"))
                    return csv_file.getvalue()

                # Convert the CSV string into downloadable file
                csv_data = convert_to_csv(st.session_state.csv_output)

                # Provide download link
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="lca_output.csv",
                    mime="text/csv"
                )

# Run the app
if __name__ == "__main__":
    main()
