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
    """
    Prints the author's full name.

    This function is used to display the full name of the script's author.
    It serves as an example of a standalone function and is typically called
    at the beginning of the script.
    """
    full_name = "Nibedita Bhowmick"
    print(f"\nAuthor: {full_name}")


def load_data(file_path):
    """
    Reads the dataset from the specified file path and stores records in a list.

    This function reads a CSV file, processes each row into a Record object,
    and stores these objects in a list for further use. It includes error handling
    for file operations and data validation to ensure rows have sufficient columns.

    Parameters:
    - file_path (str): The path to the CSV file to be loaded.

    Returns:
    - list: A list of Record objects representing the rows in the dataset.

    Exceptions:
    - FileNotFoundError: If the file is not found at the specified path.
    - Exception: For any other errors during file reading or processing.
    """
    records = []  # Initialize an empty list to store Record objects
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row if present

            for row in reader:
                # Validate that the row has at least 15 fields
                if len(row) >= 15:
                    # Create a Record object using the first 15 columns of the row
                    record = Record(*row[:15])
                    records.append(record)
                else:
                    # Log a warning if the row has insufficient data
                    print(f"Skipping row with insufficient data: {row}")

    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: The file was not found.")
    except Exception as e:
        # Handle other errors that may occur
        print(f"Error reading file: {e}")

    return records


if __name__ == "__main__":
    """
    Main execution block of the script.

    This section performs the following tasks:
    1. Displays the author's full name.
    2. Loads data from the specified CSV file into a list of Record objects.
    3. Prints the first 8 records for demonstration and testing purposes.
    """
    # Display the author's full name
    display_full_name()

    # Specify the path to the dataset
    dataset_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"

    # Load records from the dataset
    records = load_data(dataset_path)

    # Display the first 8 records from the dataset
    for record in records[:8]:  # Adjust the slice to control the number of records displayed
        print(record)
