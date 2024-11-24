import streamlit as st
import csv
from io import StringIO

# Your function to create CSV output (modify the response part according to your code)
def create_csv_output(query):
    # Define the template for the LCA output
    qa_and_matrix_template = """
    Based on the context below, generate a table with the following columns:
    Activity database; Activity code; Activity name; Activity unit; Activity Location; Activity type; Exchange database; Exchange code; Exchange amount; Exchange unit; Exchange type; Exchange uncertainty type; Exchange loc; Exchange scale; Exchange negative; Notes
    
    Ensure the output strictly follows these rules:
    1. Use the same name in the "Activity Database" column for all rows.
    2. Define the overall process. This is a production exchange type.
    3. Provide the technosphere and biosphere exchanges rows one by one after the production row.
    4. Ensure that the "Activity code" and "Activity name" columns are uniquely assigned to each production and used for each exchange row for this production.
    5. Remember precise units (e.g., kg, kWh), location (county, region, global).
    6. The "Exchange amount" column should match the amounts provided in the query. Do not fabricate or infer any data.
    7. In the "Notes" column, provide a brief description of the exchange in the row, including its purpose and location.
    8. If any data is missing or unclear, leave the field blank or mark it as "N/A." Do not fabricate any information.
    
    Output Structure: 
    1. Generate the table in CSV format in a Semicolon-separated format.
    2. Add any "Concerns" below the table

    Context: 
    The goal is to create a foreground database for a Technology Life Cycle Assessment (LCA). Each row corresponds to an exchange type.
    
    Question: {query}

    Answer:
    """
    
    # Sample output data (you can replace this with actual logic to parse query)
    # This part is where you would integrate your model's response to generate the actual data
    # Here we generate a mock CSV for the sake of example
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

    # When the button is pressed, generate the CSV output
    if st.button("Generate LCA Table"):
        # Call the function with the query input
        csv_output = create_csv_output(query)

        # Display the CSV output in the app
        st.subheader("Generated foreground Table")
        st.text(csv_output)

        st.subheader("Please help confirm if this is correct")
        st.subheader("Find relevant background data")

        st.subheader("Please help confirm if this is correct")
        st.subheader("Find relevant background data")

        # Allow user to download the CSV file
        @st.cache_data
        def convert_to_csv(data):
            # Use StringIO to simulate a file in memory
            csv_file = StringIO()
            csv_writer = csv.writer(csv_file, delimiter=";")
            for row in data.splitlines():
                csv_writer.writerow(row.split(";"))
            return csv_file.getvalue()

        # Convert the CSV string into downloadable file
        csv_data = convert_to_csv(csv_output)

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
