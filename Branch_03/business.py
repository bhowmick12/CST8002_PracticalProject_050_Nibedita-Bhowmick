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
        self.records = load_data(file_path)  # Load data from the specified CSV file

    def save_records(self):
        """
        Saves the current list of records to a new output file.
        The filename is generated dynamically.
        """
        output_filename = generate_output_filename()  # Generate a unique output filename
        save_data(self.records, output_filename)  # Save records to the generated file
        print(f"✅ Data saved to {output_filename}")  # Inform the user where the data was saved

    def add_record(self, record):
        """Adds a new record to the records list."""
        self.records.append(record)

    def update_record(self, index, updated_record):
        """Updates an existing record at the given index with a new record."""
        if 0 <= index < len(self.records):
            self.records[index] = updated_record

    def delete_record(self, index):
        """Deletes a record from the records list at the specified index."""
        if 0 <= index < len(self.records):
            del self.records[index]

    def get_record(self, index):
        """Retrieves a record from the records list at the specified index."""
        return self.records[index] if 0 <= index < len(self.records) else None

    def sort_records(self, sort_key):
        """
        Sorts records based on a specified attribute.

        :param sort_key: (str) The attribute name to sort by.
        """
        try:
            # Ensure there are records to sort
            if not self.records:
                print("⚠ No records to sort.")
                return

            # Check if the attribute exists in Record objects
            if hasattr(self.records[0], sort_key):  # Check if the attribute exists in the Record class
                self.records.sort(key=lambda record: getattr(record, sort_key))
                print(f"✅ Records sorted successfully by '{sort_key}'.")
            else:
                print(f"❌ Error: Invalid attribute '{sort_key}' for sorting.")
        except Exception as e:
            print(f"❌ Unexpected error while sorting: {e}")
