# ------------------------------------------------------
# Filename: persistence.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 1.1
# Description:
#     This module provides functions for loading and saving records
#     to a CSV file. It includes error handling to ensure robust file operations.
# ------------------------------------------------------

import csv  # Import CSV module for handling CSV file operations
import uuid  # Import UUID module for generating unique filenames
from record import Record  # Import the Record class for data representation


def load_data(file_path):
    """
    Loads records from a CSV file and returns a list of Record objects.

    :param file_path: (str) Path to the CSV file.
    :return: (list) A list of Record objects.
    """
    records = []  # Initialize an empty list to store records
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Create a CSV reader object
            headers = next(reader)  # Read and skip the header row if present

            for row in reader:
                if len(row) >= 15:  # Ensure the row contains sufficient columns
                    record = Record(*row[:15])  # Create a Record object using the first 15 fields
                    records.append(record)  # Append the record to the list

    except FileNotFoundError:
        print("Error: File not found.")  # Handle case where the file is missing
    except Exception as e:
        print(f"Error reading file: {e}")  # Handle unexpected errors

    return records  # Return the list of loaded records


def save_data(records, output_file_path):
    """
    Saves a list of Record objects to a CSV file.

    :param records: (list) A list of Record objects to be saved.
    :param output_file_path: (str) The path where the CSV file will be saved.
    """
    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)  # Create a CSV writer object

            for record in records:
                # Convert Record object attributes to a list and write to CSV
                writer.writerow([
                    record.region, record.district, record.license_number,
                    record.facility_name, record.facility_type,
                    record.facility_address_1, record.facility_address_2,
                    record.facility_address_3, record.max_children, record.max_infants,
                    record.max_preschool, record.max_school_age, record.language,
                    record.operator_id, record.designated_facility
                ])

        print(f"Data successfully saved to {output_file_path}.")  # Confirm success

    except Exception as e:
        print(f"Error saving file: {e}")  # Handle unexpected errors


def generate_output_filename():
    """
    Generates a unique filename for output files using a UUID.

    :return: (str) A unique filename with a `.csv` extension.
    """
    return f"output_{uuid.uuid4().hex}.csv"  # Generate a unique filename using a random UUID
