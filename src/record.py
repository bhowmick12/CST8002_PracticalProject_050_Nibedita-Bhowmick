class Record:
    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3,
                 max_children, max_infants, max_preschool, max_school_age,
                 language, operator_id, designated_facility):
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


