from business import DataManager
from record import Record

def main():
    data_manager = DataManager()

    while True:
        print("\nMenu:")
        print("1. Add New Record")
        print("2. Display Records")
        print("3. Sort Records")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            # Collect user input for a new record
            region = input("Enter Region: ").strip()
            district = input("Enter District: ").strip()
            facility_name = input("Enter Facility Name: ").strip()
            facility_type = input("Enter Facility Type: ").strip()
            address = input("Enter Address: ").strip()
            max_children = input("Enter Max Children Capacity: ").strip()

            try:
                max_children = int(max_children)  # Ensure it's a number
                new_record = Record(region, district, facility_name, facility_type, address, max_children)
                data_manager.add_record(new_record)
                print("Record added successfully.")
            except ValueError:
                print("Error: Max Children must be a number.")

        elif choice == "2":
            print("\nDisplaying records:")
            data_manager.display_records()

        elif choice == "3":
            print("\nSorting options:")
            print("1. Region")
            print("2. District")
            print("3. Facility Name")
            print("4. Max Children")
            sort_choice = input("Choose a column to sort by: ").strip()

            column_map = {"1": "region", "2": "district", "3": "facility_name", "4": "max_children"}

            if sort_choice in column_map:
                data_manager.sort_records(column_map[sort_choice])
                print("Records sorted successfully!")
            else:
                print("Invalid selection.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
