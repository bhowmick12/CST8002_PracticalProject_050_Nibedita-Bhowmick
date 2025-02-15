# ------------------------------------------------------
# Filename: presentation.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 1.1
# Description:
#     This script manages records for a facility management system.
#     It allows the user to load, save, display, add, update, and delete records.
# ------------------------------------------------------

# Importing necessary modules
from business import Business  # Manages the data (loading, saving, etc.)
from record import Record  # Represents a single record

# Function to display the main menu to the user
def display_menu():
    print("1. Load Data")  # Option to load data
    print("2. Display Records")  # Option to display all records
    print("3. Add New Record")  # Option to add a new record
    print("4. Update Record")  # Option to update an existing record
    print("5. Save Record")  # Option to save record
    print("6. Delete Record")  # Option to delete an existing record
    print("7. Exit")  # Option to exit the program


# Function to display the full name of the program author
def display_full_name():
    print("Program by Nibedita Bhowmick")

# Main function that runs the program
def main():
    data_manager = Business()  # Initialize DataManager object to handle records

    # Continuously display the menu until the user chooses to exit
    while True:
        display_full_name()  # Display author information
        display_menu()  # Display menu options
        choice = input("Select an option: ").strip()  # Get user input for the option

        # Handle 'Load Data' option
        if choice == "1":
            file_path  = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"
            #file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"

            # file_path = input("Enter the CSV file path: ").strip()  # Ask for file path
            try:
                data_manager.load_records(file_path)  # Load records from the file
                print("Data loaded successfully.")  # Success message
            except Exception as e:  # Handle exceptions during file loading
                print(f"Error loading file: {e}")

                # Handle 'Display Records' option

        elif choice == "2":
                # Check if there are any records to display
                if not data_manager.records:
                    print("No records available.")  # No records available message
                else:
                    # Display up to 100 records
                    for i, record in enumerate(data_manager.records[:100], start=1):
                        print(f"{i}. {record}")  # Print each record
                        if i % 10 == 0:  # Print author name after every 10 records
                            display_full_name()

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
