import csv
from record import Record


class DataManager:
    def __init__(self, file_path="data.csv"):
        self.records = []
        self.file_path = file_path
        self.load_records_on_startup()

    def load_records_on_startup(self):
        """Loads records from CSV file on startup, handling errors gracefully."""
        try:
            with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row if applicable

                for i, row in enumerate(reader):
                    if i >= 100:
                        print("Limit reached: Only the first 100 records are loaded.")
                        break

                    record = Record(*row)  # Adjust based on Record constructor
                    self.records.append(record)

            print(f"Successfully loaded {len(self.records)} records from {self.file_path}.")

        except FileNotFoundError:
            print(f"Warning: The file '{self.file_path}' was not found. No data loaded.")
        except Exception as e:
            print(f"Error loading records: {e}")

    def save_records(self):
        """Saves records to the CSV file."""
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for record in self.records:
                    writer.writerow(record.to_list())  # Ensure `Record` has a `to_list()` method

            print(f"Data successfully saved to {self.file_path}.")
        except Exception as e:
            print(f"Error saving records: {e}")
