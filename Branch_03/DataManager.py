# ------------------------------------------------------
# Filename: DataManager.py
# Author: Nibedita Bhowmick
# Due date: 2025-03-16
# Version: 1.1
# Description:
#     This script defines the DataManager class, which is responsible for managing
#     records by loading data from a CSV file on startup, storing records in memory,
#     and saving data back to the CSV file. It includes error handling for robust file operations.
# ------------------------------------------------------

import csv  # Import the CSV module for handling file operations
from record import Record  # Import the Record class to represent individual records


class DataManager:
    """
    The DataManager class manages records by loading them from a CSV file on startup,
    storing them in memory, and saving changes back to the file.
    """

    def __init__(self, file_path="data.csv"):
        """
        Initializes the DataManager with a specified file path and an empty list of records.

        :param file_path: (str) The path to the CSV file where records are stored.
        """
        self.records = []  # Stores records in memory as a list of Record objects
        self.file_path = file_path  # The file where records are persisted
        self.load_records_on_startup()  # Automatically load data when an instance is created

    def load_records_on_startup(self):
        """
        Reads records from the CSV file at startup and stores them in memory.
        Implements error handling for missing or corrupted files.
        """
        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)  # Create a CSV reader object
                next(reader)  # Skip the header row if applicable

                for i, row in enumerate(reader):
                    if i >= 100:  # Restrict to 100 records for performance reasons
                        print("⚠ Limit reached: Only the first 100 records are loaded.")
                        break

                    # Convert CSV row into a Record object assuming matching attributes
                    record = Record(*row)
                    self.records.append(record)  # Append the record to the list

            print(f"✅ Successfully loaded {len(self.records)} records from {self.file_path}.")

        except FileNotFoundError:
            print(f"⚠ Warning: The file '{self.file_path}' was not found. No data loaded.")
        except Exception as e:
            print(f"❌ Error loading records: {e}")  # Handle unexpected errors

    def save_records(self):
        """
        Saves all stored records to the CSV file.
        Ensures data integrity by handling file writing errors.
        """
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)  # Create a CSV writer object

                # Writing a header row (adjust column names as per data structure)
                writer.writerow(["Region", "District", "Facility Name", "Facility Type", "Address", "Max Children"])

                # Convert each Record object to a list before writing to CSV
                for record in self.records:
                    writer.writerow(record.to_list())

            print(f"✅ Data successfully saved to {self.file_path}.")
        except Exception as e:
            print(f"❌ Error saving records: {e}")  # Handle unexpected errors

    def sort_records(self, attribute):
        """
        Sorts records based on the specified attribute.

        :param attribute: (str) The attribute to sort by (e.g., 'region', 'district', etc.).
        """
        try:
            # Sort the records in ascending order based on the specified attribute
            self.records.sort(key=lambda record: getattr(record, attribute))
            print(f"✅ Records successfully sorted by '{attribute}'.")
        except AttributeError:
            print(f"❌ Error: Attribute '{attribute}' not found in records. Sorting failed.")
        except Exception as e:
            print(f"❌ Unexpected error while sorting: {e}")
