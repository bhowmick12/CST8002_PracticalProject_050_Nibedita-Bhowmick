# ------------------------------------------------------
# Filename: record.py
# Author: Nibedita Bhowmick
# Date: 2024-06-11
# Version: 1.0
# Description:
#     This script defines the Record class, which represents
#     a childcare facility with various attributes. The class
#     includes an initializer and a string representation method
#     for easy printing of record details.
# ------------------------------------------------------

class Record:
    """
       Represents a childcare facility with various attributes such as location, capacity,
       language, and operator details.
       """
    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3,
                 max_children, max_infants, max_preschool, max_school_age,
                 language, operator_id, designated_facility):

        """
        Initializes a Record instance with childcare facility details.

        Parameters:
        - region (str): The region where the facility is located.
        - district (str): The district of the facility.
        - license_number (str): License number of the facility.
        - facility_name (str): Name of the childcare facility.
        - facility_type (str): Type of facility (e.g., daycare, preschool).
        - facility_address_1 (str): Primary address of the facility.
        - facility_address_2 (str, optional): Secondary address details.
        - facility_address_3 (str, optional): Additional address details.
        - max_children (int): Maximum number of children allowed.
        - max_infants (int): Maximum number of infants allowed.
        - max_preschool (int): Maximum number of preschool children allowed.
        - max_school_age (int): Maximum number of school-age children allowed.
        - language (str): Primary language of the facility.
        - operator_id (str): Unique ID of the facility operator.
        - designated_facility (bool): Indicates if the facility is designated.
        """
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
        return (f"{self.region}, {self.district}, {self.license_number}, {self.facility_name}, "
                f"{self.facility_type}, {self.facility_address_1}, {self.facility_address_2}, "
                f"{self.facility_address_3}, {self.max_children}, {self.max_infants}, "
                f"{self.max_preschool}, {self.max_school_age}, {self.language}, "
                f"{self.operator_id}, {self.designated_facility}")