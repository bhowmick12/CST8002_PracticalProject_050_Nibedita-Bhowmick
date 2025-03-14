import csv  # Import CSV module for reading and writing CSV files
from record import Record  # Import the Record class to handle individual records


class DataManager:
    """
    The DataManager class manages records, loading them from a CSV file on startup
    and providing functionalities to store, retrieve, and save records.
    """

    def __init__(self, file_path="data.csv"):
        """
        Initializes the DataManager with an empty list of records and a file path.

        :param file_path: (str) The path to the CSV file where data is stored.
        """
        self.records = []  # List to store records in memory
        self.file_path = file_path  # Path to the data file
        self.load_records_on_startup()  # Automatically load data on object creation

    def load_records_on_startup(self):
        """
        Loads records from a CSV file when the DataManager instance is created.
        Handles errors if the file does not exist or if unexpected issues occur.
        """
        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)  # Create a CSV reader object
                next(reader)  # Skip header row if applicable

                for i, row in enumerate(reader):
                    if i >= 100:  # Limit to first 100 records for performance reasons
                        print("Limit reached: Only the first 100 records are loaded.")
                        break

                    # Assuming row contains data in order of Record fields
                    record = Record(*row)  # Convert CSV row into a Record object
                    self.records.append(record)  # Store the record in the list

            print(f"Successfully loaded {len(self.records)} records from {self.file_path}.")

        except FileNotFoundError:
            print(f"Warning: The file '{self.file_path}' was not found. No data loaded.")
        except Exception as e:
            print(f"Error loading records: {e}")  # Handle unexpected errors

    def save_records(self):
        """
        Saves the current list of records to the CSV file.
        Handles potential errors during file writing.
        """
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)  # Create a CSV writer object
                # Assuming you want to include a header in your CSV file
                writer.writerow(["Region", "District", "Facility Name", "Facility Type", "Address",
                                 "Max Children"])  # Example header

                for record in self.records:
                    writer.writerow(record.to_list())  # Convert Record object to list for writing

            print(f"Data successfully saved to {self.file_path}.")
        except Exception as e:
            print(f"Error saving records: {e}")  # Handle unexpected errors

    def sort_records(self, attribute):
        """
        Sort records by a given attribute.

        :param attribute: (str) The attribute to sort by (e.g., 'region', 'district', etc.)
        """
        try:
            self.records.sort(key=lambda x: getattr(x, attribute))
            print(f"Records successfully sorted by '{attribute}'.")
        except AttributeError:
            print(f"Error: Attribute '{attribute}' not found in records.")
        except Exception as e:
            print(f"Unexpected error while sorting: {e}")
