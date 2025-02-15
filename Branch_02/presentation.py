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
   # print("2. Save Data")  # Option to save data
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

           #file_path = input("Enter the CSV file path: ").strip()  # Ask for file path
            try:
                data_manager.load_records(file_path)  # Load records from the file
                print("Data loaded successfully.")  # Success message
            except Exception as e:  # Handle exceptions during file loading
                print(f"Error loading file: {e}")

        # Handle 'Save Data' option
       #elif choice == "2":
            #print("Data saved successfully.")  # Success message
            #except Exception as e:  # Handle exceptions during saving
                #print(f"Error saving data: {e}")

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

        # Handle 'Add New Record' option
        elif choice == "3":
            # Collect user input for a new record
            region = input("Region: ").strip()
            district = input("District: ").strip()
            license_number = input("License_number: ").strip()
            facility_name = input("Facility Name: ").strip()
            facility_type = input("Facility Type: ").strip()
            facility_address_1 = input("Address Line 1: ").strip()
            facility_address_2 = input("Address Line 2 (Optional): ").strip() or None
            facility_address_3 = input("Address Line 3 (Optional): ").strip() or None
            max_children = input("Max Children: ").strip()
            max_infants = input("Max Infants: ").strip()
            max_preschool = input("Max Preschool: ").strip()
            max_school_age = input("Max School Age: ").strip()
            language = input("Language: ").strip()
            operator_id = input("Operator ID: ").strip()
            designated_facility = input("Designated Facility (Yes/No): ").strip().lower()

            # Convert "Yes" or "No" to boolean values for designated_facility
            if designated_facility == "yes":
                designated_facility = True
            elif designated_facility == "no":
                designated_facility = False
            else:
                print("Error: Designated Facility must be 'Yes' or 'No'.")
                continue

            # Convert numerical fields safely to integers
            try:
                max_children = int(max_children)
                max_infants = int(max_infants)
                max_preschool = int(max_preschool)
                max_school_age = int(max_school_age)
            except ValueError:
                print("Error: Max values must be numbers.")
                continue

            # Create and add the new record
            new_record = Record(
                region, district, license_number, facility_name, facility_type,
                facility_address_1, facility_address_2, facility_address_3,
                max_children, max_infants, max_preschool, max_school_age,
                language, operator_id, designated_facility
            )

            data_manager.add_record(new_record)  # Add the new record to the data manager
            print("New record added successfully.")

        # Handle 'Update Record' option
        elif choice == "4":
            try:
                # Get the index of the record to update
                index = int(input("Enter record index to update: ")) - 1
                if 0 <= index < len(data_manager.records):
                    # Gather updated details from the user
                    print("Enter updated details (leave blank to keep existing value).")
                    existing_record = data_manager.records[index]  # Get existing record

                    # Collect inputs for updated record details
                    region = input(f"Region [{existing_record.region}]: ").strip() or existing_record.region
                    district = input(f"District [{existing_record.district}]: ").strip() or existing_record.district
                    license_number = input(f"License_Number [{existing_record.license_number}]: ").strip() or existing_record.license_number
                    facility_name = input(f"Facility Name [{existing_record.facility_name}]: ").strip() or existing_record.facility_name
                    facility_type = input(f"Facility Type [{existing_record.facility_type}]: ").strip() or existing_record.facility_type
                    facility_address_1 = input(f"Address Line 1 [{existing_record.facility_address_1}]: ").strip() or existing_record.facility_address_1
                    facility_address_2 = input(f"Address Line 2 [{existing_record.facility_address_2}]: ").strip() or existing_record.facility_address_2
                    facility_address_3 = input(f"Address Line 3 [{existing_record.facility_address_3}]: ").strip() or existing_record.facility_address_3
                    max_children = input(f"Max Children [{existing_record.max_children}]: ").strip() or existing_record.max_children
                    max_infants = input(f"Max Infants [{existing_record.max_infants}]: ").strip() or existing_record.max_infants
                    max_preschool = input(f"Max Preschool [{existing_record.max_preschool}]: ").strip() or existing_record.max_preschool
                    max_school_age = input(f"Max School Age [{existing_record.max_school_age}]: ").strip() or existing_record.max_school_age
                    language = input(f"Language [{existing_record.language}]: ").strip() or existing_record.language
                    operator_id = input(f"Operator ID [{existing_record.operator_id}]: ").strip() or existing_record.operator_id
                    designated_facility = input(f"Designated Facility [{existing_record.designated_facility}]: ").strip() or existing_record.designated_facility

                    # Convert numerical fields safely
                    try:
                        max_children = int(max_children)
                        max_infants = int(max_infants)
                        max_preschool = int(max_preschool)
                        max_school_age = int(max_school_age)
                    except ValueError:
                        print("Error: Max values must be numbers.")
                        continue

                    # Create and update the record
                    updated_record = Record(
                        region, district, license_number, facility_name, facility_type,
                        facility_address_1, facility_address_2, facility_address_3,
                        max_children, max_infants, max_preschool, max_school_age,
                        language, operator_id, designated_facility
                    )

                    data_manager.update_record(index, updated_record)  # Update the record in data manager
                    print("Record updated successfully.")
                else:
                    print("Error: Index out of range.")  # Handle invalid index input
            except ValueError:
                print("Error: Invalid index.")  # Handle invalid input for index

        # Handle 'save Record' option
        elif choice == "5":
            try:
                data_manager.save_records()  # Save any changes made
                print("Data saved successfully.")
            except Exception as e:
                print(f"Error saving data: {e}")
            print("Exiting program.")  # Print exit message
            break
            # Handle 'delete Record' option
        elif choice == "6":
            try:
                index = int(input("Enter record index to delete: ")) - 1  # Convert input to zero-based index

                if 0 <= index < len(data_manager.records):  # Check if index is valid
                    deleted_record = data_manager.records.pop(index)  # Remove the record
                    print(f"Record deleted successfully: {deleted_record}")

                    # Save updated records to file
                    data_manager.save_records()
                    print("Changes saved successfully.")
                else:
                    print("Error: Index out of range.")  # Handle out-of-range index

            except ValueError:
                print("Error: Invalid index. Please enter a number.")  # Handle invalid input


        # Handle 'Exit' option
        elif choice == "7":
            print("Exiting program.")  # Print exit message
            break

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
