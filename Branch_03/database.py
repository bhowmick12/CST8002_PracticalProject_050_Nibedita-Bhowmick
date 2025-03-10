import sqlite3
from record import Record


class DatabaseManager:
    """Handles database operations for childcare records."""

    def __init__(self, db_name="childcare.db"):
        # Connect to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates a table for storing childcare records if it does not exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT,
                district TEXT,
                license_number TEXT,
                facility_name TEXT,
                facility_type TEXT,
                facility_address_1 TEXT,
                facility_address_2 TEXT,
                facility_address_3 TEXT,
                max_children INTEGER,
                max_infants INTEGER,
                max_preschool INTEGER,
                max_school_age INTEGER,
                language TEXT,
                operator_id TEXT,
                designated_facility TEXT
            )
        ''')
        self.conn.commit()

    def add_record(self, record):
        """Insert a new record into the database."""
        self.cursor.execute('''
            INSERT INTO records (region, district, license_number, facility_name, facility_type,
                                 facility_address_1, facility_address_2, facility_address_3,
                                 max_children, max_infants, max_preschool, max_school_age,
                                 language, operator_id, designated_facility)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (record.region, record.district, record.license_number, record.facility_name,
              record.facility_type, record.facility_address_1, record.facility_address_2,
              record.facility_address_3, record.max_children, record.max_infants,
              record.max_preschool, record.max_school_age, record.language,
              record.operator_id, record.designated_facility))
        self.conn.commit()

    def get_all_records(self):
        """Fetch all records from the database."""
        self.cursor.execute("SELECT * FROM records")
        rows = self.cursor.fetchall()
        records = []
        for row in rows:
            record = Record(
                region=row[1], district=row[2], license_number=row[3], facility_name=row[4],
                facility_type=row[5], facility_address_1=row[6], facility_address_2=row[7],
                facility_address_3=row[8], max_children=row[9], max_infants=row[10],
                max_preschool=row[11], max_school_age=row[12], language=row[13],
                operator_id=row[14], designated_facility=row[15]
            )
            records.append(record)
        return records

    def get_record_by_id(self, record_id):
        """Fetch a record by its ID."""
        self.cursor.execute("SELECT * FROM records WHERE id = ?", (record_id,))
        row = self.cursor.fetchone()
        if row:
            return Record(
                region=row[1], district=row[2], license_number=row[3], facility_name=row[4],
                facility_type=row[5], facility_address_1=row[6], facility_address_2=row[7],
                facility_address_3=row[8], max_children=row[9], max_infants=row[10],
                max_preschool=row[11], max_school_age=row[12], language=row[13],
                operator_id=row[14], designated_facility=row[15]
            )
        return None

    def update_record(self, record_id, record):
        """Update an existing record."""
        self.cursor.execute('''
            UPDATE records
            SET region = ?, district = ?, license_number = ?, facility_name = ?, facility_type = ?,
                facility_address_1 = ?, facility_address_2 = ?, facility_address_3 = ?,
                max_children = ?, max_infants = ?, max_preschool = ?, max_school_age = ?,
                language = ?, operator_id = ?, designated_facility = ?
            WHERE id = ?
        ''', (record.region, record.district, record.license_number, record.facility_name,
              record.facility_type, record.facility_address_1, record.facility_address_2,
              record.facility_address_3, record.max_children, record.max_infants,
              record.max_preschool, record.max_school_age, record.language,
              record.operator_id, record.designated_facility, record_id))
        self.conn.commit()

    def delete_record(self, record_id):
        """Delete a record from the database."""
        self.cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    # Create a database manager instance
    db_manager = DatabaseManager()

    # Create a record
    record = Record(
        region="Central", district="Downtown", license_number="12345", facility_name="Sunshine Kids Care",
        facility_type="Daycare", facility_address_1="123 Sunshine St.", facility_address_2="Suite 101",
        facility_address_3="Cityville, ABC 123", max_children=50, max_infants=10, max_preschool=20,
        max_school_age=20, language="English", operator_id="OP5678", designated_facility="Yes"
    )

    # Add the record to the database
    db_manager.add_record(record)

    # Retrieve and print all records
    records = db_manager.get_all_records()
    for r in records:
        print(r)

    # Retrieve and print a record by ID
    retrieved_record = db_manager.get_record_by_id(1)
    if retrieved_record:
        print("Retrieved record:", retrieved_record)

    # Update a record
    record_to_update = Record(
        region="Central", district="Downtown", license_number="12345", facility_name="Updated Sunshine Kids Care",
        facility_type="Daycare", facility_address_1="123 Updated St.", facility_address_2="Suite 102",
        facility_address_3="Cityville, ABC 124", max_children=60, max_infants=15, max_preschool=25,
        max_school_age=30, language="English", operator_id="OP5678", designated_facility="Yes"
    )
    db_manager.update_record(1, record_to_update)

    # Delete a record by ID
    db_manager.delete_record(1)

    # Close the database connection
    db_manager.close()
