from business import DataManager
from record import Record

def display_menu():
    print("1. Load Data")
    print("2. Save Data")
    print("3. Display Records")
    print("4. Add New Record")
    print("5. Update Record")
    print("6. Delete Record")
    print("7. Exit")

def display_full_name():
    print("Program by Nibedita Bhowmick")

def main():
    data_manager = DataManager()

    while True:
        display_full_name()
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            file_path = input("Enter the CSV file path: ").strip()
            try:
                data_manager.load_records(file_path)
                print("Data loaded successfully.")
            except Exception as e:
                print(f"Error loading file: {e}")

        elif choice == "2":
            try:
                data_manager.save_records()
                print("Data saved successfully.")
            except Exception as e:
                print(f"Error saving data: {e}")


        elif choice == "3":

            if not data_manager.records:

                print("No records available.")

            else:

                for i, record in enumerate(data_manager.records[:10], start=1):  # Limit to 100 records

                    print(f"{i}. {record}")

                    if i % 10 == 0:
                        display_full_name()





        elif choice == "4":
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

            # Convert "Yes" or "No" to boolean values
            if designated_facility == "yes":
                designated_facility = True
            elif designated_facility == "no":
                designated_facility = False
            else:
                print("Error: Designated Facility must be 'Yes' or 'No'.")
                continue


            # Convert numerical values safely
            try:
                max_children = int(max_children)
                max_infants = int(max_infants)
                max_preschool = int(max_preschool)
                max_school_age = int(max_school_age)
            except ValueError:
                print("Error: Max values must be numbers.")
                continue


            # Create and add new record
            new_record = Record(
                region, district, license_number, facility_name, facility_type,
                facility_address_1, facility_address_2, facility_address_3,
                max_children, max_infants, max_preschool, max_school_age,
                language, operator_id, designated_facility
            )

            data_manager.add_record(new_record)
            print("New record added successfully.")

        elif choice == "5":
            try:
                index = int(input("Enter record index to update: ")) - 1
                if 0 <= index < len(data_manager.records):
                    # Gather updated details
                    print("Enter updated details (leave blank to keep existing value).")
                    existing_record = data_manager.records[index]

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

                    updated_record = Record(
                        region, district, license_number, facility_name, facility_type,
                        facility_address_1, facility_address_2, facility_address_3,
                        max_children, max_infants, max_preschool, max_school_age,
                        language, operator_id, designated_facility
                    )

                    data_manager.update_record(index, updated_record)
                    print("Record updated successfully.")
                else:
                    print("Error: Index out of range.")
            except ValueError:
                print("Error: Invalid index.")

        elif choice == "6":
            try:
                data_manager.save_records()
                print("Data saved successfully.")
            except Exception as e:
                print(f"Error saving data: {e}")
            print("Exiting program.")
            break

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
