class Record:
    """Superclass for all records."""
    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3,
                 max_children, max_infants, max_preschool, max_school_age,
                 language, operator_id, designated_facility):
        # Assign values to the instance variables
        self.region = region
        self.district = district
        self.license_number = license_number
        self.facility_name = facility_name
        self.facility_type = facility_type
        self.facility_address_1 = facility_address_1
        self.facility_address_2 = facility_address_2
        self.facility_address_3 = facility_address_3
        self.max_children = max_children
        self.max_infants = max_infants
        self.max_preschool = max_preschool
        self.max_school_age = max_school_age
        self.language = language
        self.operator_id = operator_id
        self.designated_facility = designated_facility

    def __str__(self):
        """Provide a string representation of the record object."""
        return (f"Region: {self.region}, District: {self.district}, License Number: {self.license_number}, "
                f"Facility Name: {self.facility_name}, Type: {self.facility_type}, "
                f"Address: {self.facility_address_1}, {self.facility_address_2}, {self.facility_address_3}, "
                f"Capacity: {self.max_children}, Infants: {self.max_infants}, Preschool: {self.max_preschool}, "
                f"School Age: {self.max_school_age}, Language: {self.language}, "
                f"Operator ID: {self.operator_id}, Designated Facility: {self.designated_facility}")


class CSVRecord(Record):
    """Subclass that formats record as CSV."""
    def display_info(self):
        return (f"{self.region},{self.district},{self.license_number},{self.facility_name},"
                f"{self.facility_type},{self.facility_address_1},{self.facility_address_2},{self.facility_address_3},"
                f"{self.max_children},{self.max_infants},{self.max_preschool},{self.max_school_age},"
                f"{self.language},{self.operator_id},{self.designated_facility}")


class FormattedRecord(Record):
    """Subclass that formats record as readable text."""
    def display_info(self):
        return (f"Facility: {self.facility_name}\n"
                f"Location: {self.region}, {self.district}\n"
                f"License Number: {self.license_number}\n"
                f"Type: {self.facility_type}\n"
                f"Address: {self.facility_address_1}, {self.facility_address_2}, {self.facility_address_3}\n"
                f"Capacity: {self.max_children} (Infants: {self.max_infants}, Preschool: {self.max_preschool}, "
                f"School Age: {self.max_school_age})\n"
                f"Language: {self.language}\n"
                f"Operator ID: {self.operator_id}\n"
                f"Designated Facility: {self.designated_facility}")


# Example usage:

# Create a new record
facility = Record(
    region="Central",
    district="Downtown",
    license_number="12345",
    facility_name="Sunshine Kids Care",
    facility_type="Daycare",
    facility_address_1="123 Sunshine St.",
    facility_address_2="Suite 101",
    facility_address_3="Cityville, ABC 123",
    max_children=50,
    max_infants=10,
    max_preschool=20,
    max_school_age=20,
    language="English",
    operator_id="OP5678",
    designated_facility="Yes"
)

# Print the string representation of the record
print(facility)

# Create a CSV record
csv_record = CSVRecord(
    region="Central",
    district="Downtown",
    license_number="12345",
    facility_name="Sunshine Kids Care",
    facility_type="Daycare",
    facility_address_1="123 Sunshine St.",
    facility_address_2="Suite 101",
    facility_address_3="Cityville, ABC 123",
    max_children=50,
    max_infants=10,
    max_preschool=20,
    max_school_age=20,
    language="English",
    operator_id="OP5678",
    designated_facility="Yes"
)

# Print CSV formatted record
print(csv_record.display_info())

# Create a formatted record
formatted_record = FormattedRecord(
    region="Central",
    district="Downtown",
    license_number="12345",
    facility_name="Sunshine Kids Care",
    facility_type="Daycare",
    facility_address_1="123 Sunshine St.",
    facility_address_2="Suite 101",
    facility_address_3="Cityville, ABC 123",
    max_children=50,
    max_infants=10,
    max_preschool=20,
    max_school_age=20,
    language="English",
    operator_id="OP5678",
    designated_facility="Yes"
)

# Print the formatted record
print(formatted_record.display_info())
