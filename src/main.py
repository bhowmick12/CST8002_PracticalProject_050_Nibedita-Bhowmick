# ------------------------------------------------------
# Filename: main.py
# Author: Nibedita Bhowmick
# Date: 2024-06-11
# Version: 1.0
# Description:
#     This script loads data from a CSV file, processes it
#     into Record objects, and displays a subset of the records.
# ------------------------------------------------------


import csv
from record import Record


def display_full_name():
    full_name = "Nibedita Bhowmick"
    print(f"\nAuthor: {full_name}")


def load_data(file_path):
    records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip column headers if present

            for row in reader:
                if len(row) >= 15:  # Ensure the row has at least 15 columns
                    record = Record(*row[:15])  # Pass exactly 15 fields
                    records.append(record)
                else:
                    print(f"Skipping row with insufficient data: {row}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return records



if __name__ == "__main__":
    display_full_name()
    dataset_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"

    records = load_data(dataset_path)

    # Display records
    for record in records[:5]:  # Show only first 5 for testing
        print(record)
