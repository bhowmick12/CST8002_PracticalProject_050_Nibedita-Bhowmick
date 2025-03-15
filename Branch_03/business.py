# ------------------------------------------------------
# Filename: business.py
# Author: Nibedita Bhowmick
# Due date: 2025-03-16
# Version: 1.1
# Description:
#     This script loads data from a CSV file, processes it
#     into Record objects, and allows basic record management
#     operations such as adding, updating, deleting, and retrieving records.
# ------------------------------------------------------

from persistence import load_data, save_data, generate_output_filename
from record import Record

class Business:
    """
    The Business class is responsible for managing a collection of records.
    It provides methods to load, save, add, update, delete, retrieve, and sort records.
    """

    def __init__(self):
        """Initializes the Business class with an empty list of records."""
        self.records = []

    def load_records(self, file_path):
        """
        Loads records from a specified file and stores them in the records list.

        :param file_path: (str) Path to the file containing stored records.
        """
        try:
            self.records = load_data(file_path)  # Load data from the specified CSV file
            print(f"✅ Successfully loaded {len(self.records)} records from {file_path}.")
        except Exception as e:
            print(f"❌ Error loading records: {e}")

    def save_records(self):
        """
        Saves the current list of records to a new output file.
        The filename is generated dynamically.
        """
        try:
            if not self.records:
                print("⚠ No records to save.")
                return

            output_filename = generate_output_filename()  # Generate a unique output filename
            save_data(self.records, output_filename)  # Save records to the generated file
            print(f"✅ Data saved to {output_filename}")
        except Exception as e:
            print(f"❌ Error saving records: {e}")

    def add_record(self, record):
        """
        Adds a new record to the records list.

        :param record: (Record) A Record object to be added.
        """
        if isinstance(record, Record):
            self.records.append(record)
            print(f"✅ Record added successfully: {record}")
        else:
            print("❌ Error: Invalid record type. Expected a Record object.")

    def update_record(self, index, updated_record):
        """
        Updates an existing record at the given index with a new record.

        :param index: (int) The index of the record to update.
        :param updated_record: (Record) The updated Record object.
        """
        try:
            if 0 <= index < len(self.records) and isinstance(updated_record, Record):
                self.records[index] = updated_record
                print(f"✅ Record at index {index} updated successfully.")
            else:
                print("❌ Error: Invalid index or record type.")
        except Exception as e:
            print(f"❌ Unexpected error while updating record: {e}")

    def delete_record(self, index):
        """
        Deletes a record from the records list at the specified index.

        :param index: (int) The index of the record to delete.
        """
        try:
            if 0 <= index < len(self.records):
                deleted_record = self.records.pop(index)
                print(f"✅ Record deleted successfully: {deleted_record}")
            else:
                print("❌ Error: Invalid index.")
        except Exception as e:
            print(f"❌ Unexpected error while deleting record: {e}")

    def get_record(self, index):
        """
        Retrieves a record from the records list at the specified index.

        :param index: (int) The index of the record to retrieve.
        :return: (Record or None) The requested Record object, or None if index is invalid.
        """
        try:
            return self.records[index] if 0 <= index < len(self.records) else None
        except Exception as e:
            print(f"❌ Error retrieving record: {e}")
            return None

    def sort_records(self, sort_key, reverse=False):
        """
        Sorts records based on a specified attribute.

        :param sort_key: (str) The attribute name to sort by.
        :param reverse: (bool) Whether to sort in descending order (default is ascending).
        """
        try:
            if not self.records:
                print("⚠ No records to sort.")
                return

            if hasattr(self.records[0], sort_key):  # Check if the attribute exists in the Record class
                self.records.sort(key=lambda record: getattr(record, sort_key), reverse=reverse)
                order = "descending" if reverse else "ascending"
                print(f"✅ Records sorted successfully by '{sort_key}' in {order} order.")
            else:
                print(f"❌ Error: Invalid attribute '{sort_key}' for sorting.")
        except Exception as e:
            print(f"❌ Unexpected error while sorting: {e}")
