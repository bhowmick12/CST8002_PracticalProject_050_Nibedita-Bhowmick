# ------------------------------------------------------
# Filename: persistence.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 1.1
# Description:
#     This module provides functions for loading and saving records
#     to a CSV file. It includes error handling to ensure robust file operations.
# ------------------------------------------------------

import csv  # Module for handling CSV file operations
import uuid  # Module for generating unique filenames
from record import Record  # Import the Record class for structured data representation


def load_data(file_path):
    """
    Reads records from a CSV file and returns them as a list of Record objects.

    :param file_path: (str) Path to the CSV file.
    :return: (list) A list of Record objects.
    """
    records = []  # List to store Record objects
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Initialize CSV reader
            headers = next(reader)  # Read and discard the header row

            for row in reader:
                if len(row) >= 15:  # Ensure the row has enough fields
                    record = Record(*row[:15])  # Create a Record object using first 15 fields
                    records.append(record)  # Store the record in the list

        print(f"✅ Successfully loaded {len(records)} records from {file_path}.")

    except FileNotFoundError:
        print(f"⚠ Warning: The file '{file_path}' was not found. No data loaded.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")  # Handle unexpected errors

    return records  # Return the list of loaded records


def save_data(records, output_file_path):
    """
    Writes a list of Record objects to a CSV file.

    :param records: (list) A list of Record objects to be saved.
    :param output_file_path: (str) The output CSV file path.
    """
    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)  # Initialize CSV writer

            # Writing header row (adjust field names as necessary)
            writer.writerow([
                "Region", "District", "License Number", "Facility Name", "Facility Type",
                "Facility Address 1", "Facility Address 2", "Facility Address 3",
                "Max Children", "Max Infants", "Max Preschool", "Max School Age",
                "Language", "Operator ID", "Designated Facility"
            ])

            # Write records to CSV
            for record in records:
                writer.writerow([
                    record.region, record.district, record.license_number,
                    record.facility_name, record.facility_type,
                    record.facility_address_1, record.facility_address_2,
                    record.facility_address_3, record.max_children, record.max_infants,
                    record.max_preschool, record.max_school_age, record.language,
                    record.operator_id, record.designated_facility
                ])

        print(f"✅ Data successfully saved to {output_file_path}.")

    except Exception as e:
        print(f"❌ Error saving file: {e}")  # Handle unexpected errors


def save_test_file(output_file_path):
    """
    Creates an empty CSV file for testing purposes.

    :param output_file_path: (str) The path where the test file will be created.
    """
    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
            pass  # Creates an empty file without writing any data

        print(f"✅ Test file successfully created at {output_file_path}.")

    except Exception as e:
        print(f"❌ Error creating test file: {e}")  # Handle unexpected errors


def generate_output_filename():
    """
    Generates a unique filename for an output file using a UUID.

    :return: (str) A unique filename with a `.csv` extension.
    """
    return f"output_{uuid.uuid4().hex}.csv"  # Generate a unique filename using UUID
