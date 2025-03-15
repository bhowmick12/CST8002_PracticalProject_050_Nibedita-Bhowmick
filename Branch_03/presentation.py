# ------------------------------------------------------
# Filename: presentation.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 2.3
# Description:
#     This script manages records for a childcare facility system.
#     It allows the user to load, save, display, add, update, delete, and sort records.
# ------------------------------------------------------

from business import Business  # Handles record operations
from record import Record  # Represents a single record


def display_menu():
    """Displays the menu options."""
    print("\n--- Childcare Records Management ---")
    print("1. Load Data")
    print("2. Display Records")
    print("3. Add New Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Sort Records")
    print("7. Save Records")
    print("8. Exit")


def display_full_name():
    """Displays the author's full name."""
    print("Program by Nibedita Bhowmick")


def display_records(business):
    """Display all records."""
    if not business.records:
        print("⚠ No records available.")
    else:
        print("\nDisplaying records:")
        for i, record in enumerate(business.records[:100], start=1):
            print(f"{i}. {record}")  # Uses `__str__()` for display
            if i % 10 == 0:
                display_full_name()


def main():
    """Main function handling user interactions."""
    business = Business()  # Initialize the business layer

    while True:
        display_full_name()
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            # Load data from the CSV file
            #file_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"
            file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"
            #file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test_03.csv"
            try:
                business.load_records(file_path)
                print("✅ Data loaded successfully.")
            except Exception as e:
                print(f"❌ Error loading file: {e}")

        elif choice == "2":
            # Display all records
            display_records(business)

        elif choice == "3":
            # Add a new record
            try:
                region = input("Region: ").strip()
                district = input("District: ").strip()
                license_number = input("License Number: ").strip()
                facility_name = input("Facility Name: ").strip()
                facility_type = input("Facility Type: ").strip()
                facility_address_1 = input("Address Line 1: ").strip()
                facility_address_2 = input("Address Line 2 (Optional): ").strip() or None
                facility_address_3 = input("Address Line 3 (Optional): ").strip() or None
                max_children = int(input("Max Children: ").strip())
                max_infants = int(input("Max Infants: ").strip())
                max_preschool = int(input("Max Preschool: ").strip())
                max_school_age = int(input("Max School Age: ").strip())
                language = input("Language: ").strip()
                operator_id = input("Operator ID: ").strip()
                designated_facility = input("Designated Facility (Yes/No): ").strip().lower() == "yes"

                new_record = Record(
                    region, district, license_number, facility_name, facility_type,
                    facility_address_1, facility_address_2, facility_address_3,
                    max_children, max_infants, max_preschool, max_school_age,
                    language, operator_id, designated_facility
                )
                business.add_record(new_record)
                print("✅ New record added successfully.")
            except ValueError:
                print("❌ Error: Max Children, Max Infants, Max Preschool, and Max School Age must be numbers.")

        elif choice == "4":
            # Update an existing record
            try:
                index = int(input("Enter record index to update: ")) - 1
                if 0 <= index < len(business.records):
                    existing_record = business.records[index]

                    print("\nEnter new details (Press Enter to keep existing values):")
                    region = input(f"Region [{existing_record.region}]: ").strip() or existing_record.region
                    district = input(f"District [{existing_record.district}]: ").strip() or existing_record.district
                    license_number = input(f"License Number [{existing_record.license_number}]: ").strip() or existing_record.license_number
                    facility_name = input(f"Facility Name [{existing_record.facility_name}]: ").strip() or existing_record.facility_name
                    facility_type = input(f"Facility Type [{existing_record.facility_type}]: ").strip() or existing_record.facility_type
                    facility_address_1 = input(f"Address Line 1 [{existing_record.facility_address_1}]: ").strip() or existing_record.facility_address_1
                    facility_address_2 = input(f"Address Line 2 [{existing_record.facility_address_2}]: ").strip() or existing_record.facility_address_2
                    facility_address_3 = input(f"Address Line 3 [{existing_record.facility_address_3}]: ").strip() or existing_record.facility_address_3
                    max_children = int(input(f"Max Children [{existing_record.max_children}]: ").strip() or existing_record.max_children)
                    max_infants = int(input(f"Max Infants [{existing_record.max_infants}]: ").strip() or existing_record.max_infants)
                    max_preschool = int(input(f"Max Preschool [{existing_record.max_preschool}]: ").strip() or existing_record.max_preschool)
                    max_school_age = int(input(f"Max School Age [{existing_record.max_school_age}]: ").strip() or existing_record.max_school_age)
                    language = input(f"Language [{existing_record.language}]: ").strip() or existing_record.language
                    operator_id = input(f"Operator ID [{existing_record.operator_id}]: ").strip() or existing_record.operator_id
                    designated_facility = input(f"Designated Facility (Yes/No) [{existing_record.designated_facility}]: ").strip().lower() == "yes"

                    updated_record = Record(
                        region, district, license_number, facility_name, facility_type,
                        facility_address_1, facility_address_2, facility_address_3,
                        max_children, max_infants, max_preschool, max_school_age,
                        language, operator_id, designated_facility
                    )
                    business.update_record(index, updated_record)
                    print("✅ Record updated successfully.")
                else:
                    print("❌ Error: Index out of range.")
            except ValueError:
                print("❌ Error: Invalid index.")

        elif choice == "5":
            index = int(input("Enter record index to delete: ")) - 1
            business.delete_record(index)
            print("✅ Record deleted successfully.")

        elif choice == "6":
            # Sorting functionality
            print("\nSorting options:")
            print("1. Region")
            print("2. District")
            print("3. Facility Name")
            print("4. Max Children")

            sort_choice = input("Choose a column to sort by (1-4): ").strip()

            column_map = {
                "1": "region",
                "2": "district",
                "3": "facility_name",
                "4": "max_children"
            }

            if sort_choice in column_map:
                try:
                    business.sort_records(column_map[sort_choice])
                    print(f"✅ Records sorted successfully by '{column_map[sort_choice]}'.")
                    display_records(business)  # Display the sorted records

                except AttributeError:
                    print(f"❌ Error: Attribute '{column_map[sort_choice]}' not found in records.")
                except Exception as e:
                    print(f"❌ Unexpected error: {e}")
            else:
                print("❌ Invalid selection. Please enter a number between 1 and 4.")

        elif choice == "7":
            business.save_records()
            print("✅ Data saved successfully.")

        elif choice == "8":
            print("🔴 Exiting program.")
            break

        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
