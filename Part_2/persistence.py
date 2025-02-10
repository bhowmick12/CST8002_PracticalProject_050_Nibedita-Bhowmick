# persistence.py
import csv
import uuid
from record import Record

def load_data(file_path):
    records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row if present
            for row in reader:
                if len(row) >= 15:
                    record = Record(*row[:15])  # Create Record object
                    records.append(record)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return records

def save_data(records, output_file_path):
    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for record in records:
                writer.writerow([record.region, record.district, record.license_number,
                                 record.facility_name, record.facility_type,
                                 record.facility_address_1, record.facility_address_2,
                                 record.facility_address_3, record.max_children, record.max_infants,
                                 record.max_preschool, record.max_school_age, record.language,
                                 record.operator_id, record.designated_facility])
    except Exception as e:
        print(f"Error saving file: {e}")

def generate_output_filename():
    return f"output_{uuid.uuid4().hex}.csv"
