# record.py
# ------------------------------------------------------
# Filename: record.py
# Author: Nibedita Bhowmick
# Date: 2025-02-12
# Version: 1.1
# Description:
# This file defines the Record class used to manage records in the system.
# ------------------------------------------------------

class Record:
    # Initialize a new record with the provided attributes
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

    # Define the string representation of the record object for display
    def __str__(self):
        # Return a formatted string representing the attributes of the record
        return (f"{self.region}, {self.district}, {self.license_number}, {self.facility_name}, "
                f"{self.facility_type}, {self.facility_address_1}, {self.facility_address_2}, "
                f"{self.facility_address_3}, {self.max_children}, {self.max_infants}, "
                f"{self.max_preschool}, {self.max_school_age}, {self.language}, "
                f"{self.operator_id}, {self.designated_facility}")
