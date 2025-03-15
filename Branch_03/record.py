# ------------------------------------------------------
# Filename: record.py
# Author: Nibedita Bhowmick
# Due date: 2025-03-16
# Version: 1.1
# Description:
#     This module defines the Record class, which represents an individual childcare facility record.
#     The class includes attributes for facility details and methods for displaying the record.
# ------------------------------------------------------

class Record:
    """
    The Record class represents a single childcare facility record.
    It includes attributes such as location details, capacity, and operator information.
    """

    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3,
                 max_children, max_infants, max_preschool, max_school_age,
                 language, operator_id, designated_facility):
        """
        Initializes a Record instance with the provided attributes.

        :param region: (str) The region where the facility is located.
        :param district: (str) The district of the facility.
        :param license_number: (str) The facility's license number.
        :param facility_name: (str) The name of the childcare facility.
        :param facility_type: (str) The type of childcare facility.
        :param facility_address_1: (str) The primary address line.
        :param facility_address_2: (str or None) The secondary address line (optional).
        :param facility_address_3: (str or None) The tertiary address line (optional).
        :param max_children: (int) The maximum number of children allowed in the facility.
        :param max_infants: (int) The maximum number of infants allowed.
        :param max_preschool: (int) The maximum number of preschool-age children allowed.
        :param max_school_age: (int) The maximum number of school-age children allowed.
        :param language: (str) The primary language spoken at the facility.
        :param operator_id: (str) The unique identifier of the facility operator.
        :param designated_facility: (bool) Indicates whether the facility is designated (True/False).
        """
        # Assign values to instance variables
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
        """
        Returns a string representation of the Record instance.

        :return: (str) A formatted string containing all attributes of the record.
        """
        return (f"{self.region}, {self.district}, {self.license_number}, {self.facility_name}, "
                f"{self.facility_type}, {self.facility_address_1}, {self.facility_address_2}, "
                f"{self.facility_address_3}, {self.max_children}, {self.max_infants}, "
                f"{self.max_preschool}, {self.max_school_age}, {self.language}, "
                f"{self.operator_id}, {self.designated_facility}")
