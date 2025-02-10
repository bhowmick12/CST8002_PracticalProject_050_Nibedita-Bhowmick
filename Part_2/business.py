# business.py
from persistence import load_data, save_data, generate_output_filename
from record import Record


class DataManager:
    def __init__(self):
        self.records = []

    def load_records(self, file_path):
        self.records = load_data(file_path)

    def save_records(self):
        output_filename = generate_output_filename()
        save_data(self.records, output_filename)
        print(f"Data saved to {output_filename}")

    def add_record(self, record):
        self.records.append(record)

    def update_record(self, index, updated_record):
        if 0 <= index < len(self.records):
            self.records[index] = updated_record

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]

    def get_record(self, index):
        if 0 <= index < len(self.records):
            return self.records[index]
        return None
