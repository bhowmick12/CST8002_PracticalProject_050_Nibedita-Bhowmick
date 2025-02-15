# ------------------------------------------------------
# Filename: business.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 1.1
# Description:
#     This script loads data from a CSV file, processes it
#     into Record objects, and allows basic record management
#     operations such as adding, updating, deleting, and retrieving records.
# ------------------------------------------------------

# Import necessary functions from persistence.py to handle data loading and saving
from persistence import load_data, save_data, generate_output_filename
# Import the Record class from record.py to work with individual records
from record import Record


class Business:
    """
    The DataManager class is responsible for managing a collection of records.
    It provides methods to load, save, add, update, delete, and retrieve records.
    """

    def __init__(self):
        """
        Initializes the DataManager with an empty list of records.
        """
        self.records = []

    def load_records(self, file_path):
        """
        Loads records from a specified file and stores them in the records list.

        :param file_path: (str) Path to the file containing stored records.
        """
        self.records = load_data(file_path)  # Load data from the specified CSV file

    def save_records(self):
        """
        Saves the current list of records to a new output file.
        The filename is generated dynamically.
        """
        output_filename = generate_output_filename()  # Generate a unique output filename
        save_data(self.records, output_filename)  # Save records to the generated file
        print(f"Data saved to {output_filename}")  # Inform the user where the data was saved

    def add_record(self, record):
        """
        Adds a new record to the records list.

        :param record: (Record) A Record object to be added.
        """
        self.records.append(record)  # Append the new record to the list

    def update_record(self, index, updated_record):
        """
        Updates an existing record at the given index with a new record.

        :param index: (int) The position of the record in the list that needs to be updated.
        :param updated_record: (Record) The new Record object to replace the existing one.
        """
        if 0 <= index < len(self.records):  # Ensure the index is within valid bounds
            self.records[index] = updated_record  # Update the record at the specified index

    def delete_record(self, index):
        """
        Deletes a record from the records list at the specified index.

        :param index: (int) The position of the record to be deleted.
        """
        if 0 <= index < len(self.records):  # Ensure the index is within valid bounds
            del self.records[index]  # Remove the record from the list

    def get_record(self, index):
        """
        Retrieves a record from the records list at the specified index.

        :param index: (int) The position of the record to retrieve.
        :return: (Record or None) The Record object if the index is valid, otherwise None.
        """
        if 0 <= index < len(self.records):  # Ensure the index is within valid bounds
            return self.records[index]  # Return the requested record
        return None  # Return None if the index is out of range
