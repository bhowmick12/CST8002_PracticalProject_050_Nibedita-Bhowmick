print("\n===============================")
print("Student Name: Nibedita Bhowmick")
print("===============================\n")


import csv
from record import Record


def load_data(file_path):
    records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip column headers if present

            for row in reader:
                record = Record(row[1], row[2], row[3])  # Adjust based on columns
                records.append(record)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return records


if __name__ == "__main__":
    dataset_path = "C:\Licensed_Early_Learning_and_Childcare_Facilities.csv" # Adjust filename
    records = load_data(dataset_path)

    # Display records
    for record in records[:5]:  # Show only first 5 for testing
        print(record)
