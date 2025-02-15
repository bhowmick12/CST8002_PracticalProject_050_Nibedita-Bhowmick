# ------------------------------------------------------
# Filename: data_manager.py
# Author: Nibedita Bhowmick
# Date: 2024-06-11
# Version: 1.1
# Description:
#     This script loads data from a CSV file, processes it
#     into Record objects, and displays a subset of the records.
# ------------------------------------------------------

import csv
from record import Record


def display_full_name():
    """ Prints the author's full name. """
    full_name = "Nibedita Bhowmick"
    print(f"\nAuthor: {full_name}")


def load_data(file_path, max_records):
    """
    Reads the dataset from the specified file path and stores records in a list.

    Parameters:
    - file_path (str): The path to the CSV file.
    - max_records (int): The maximum number of records to load.

    Returns:
    - list: A list of Record objects.
    """
    records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip header row

            for i, row in enumerate(reader):
                if i >= max_records:
                    break
                if len(row) >= 15:
                    record = Record(*row[:15])
                    records.append(record)
                else:
                    print(f"Skipping row with insufficient data: {row}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return records


def show_record_count(records):
    """ Displays the total number of records loaded. """
    print(f"\nTotal Records Loaded: {len(records)}")


if __name__ == "__main__":
    """ Main execution block of the script. """
    display_full_name()

    #dataset_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"
    dataset_path ="C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"
    # Load records from the dataset
    records = load_data(dataset_path, max_records=101)

    # Display the number of records
    show_record_count(records)

    # Display the first 8 records
    for record in records[:8]:
        print(record)
