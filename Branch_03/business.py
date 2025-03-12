class DataManager:
    """Manages records and implements sorting functionality."""

    def __init__(self):
        self.records = []  # Using a list to store records

    def add_record(self, record):
        """Adds a new record to the list."""
        self.records.append(record)

    def sort_records(self, column):
        """Sorts records based on a given column."""
        column_map = {
            "region": lambda r: r.region.lower(),
            "district": lambda r: r.district.lower(),
            "facility_name": lambda r: r.facility_name.lower(),
            "max_children": lambda r: int(r.max_children)  # Ensure numerical sorting
        }

        if column in column_map:
            self.records.sort(key=column_map[column])
            print(f"Records sorted by {column}.")
        else:
            print("Invalid column name. Cannot sort.")

    def display_records(self):
        """Displays all records in sorted order."""
        for record in self.records:
            print(record.display_info())
