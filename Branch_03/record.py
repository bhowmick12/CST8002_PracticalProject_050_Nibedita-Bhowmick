class Record:
    """Represents a childcare record with sorting capability."""

    def __init__(self, region, district, facility_name, facility_type, address, max_children):
        self.region = region
        self.district = district
        self.facility_name = facility_name
        self.facility_type = facility_type
        self.address = address
        self.max_children = max_children

    def display_info(self):
        """Return a formatted string representation of the record."""
        return f"{self.facility_name} - {self.region}, {self.district} (Capacity: {self.max_children})"
