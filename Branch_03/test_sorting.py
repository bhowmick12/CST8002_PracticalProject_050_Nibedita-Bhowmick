import unittest
from business import Business  # Import Business class
from record import Record  # Import Record class

class TestSorting(unittest.TestCase):
    def setUp(self):
        """Set up initial test records with all required attributes."""
        self.business = Business()  # Initialize the Business class
        # Add records with all the required attributes for the Record class
        self.business.add_record(
            Record(
                "Ontario", "Toronto", "123456", "Daycare", "Full_time Centre","Address 1", "Address 2", "Address 3",
                50, 10, 20, 30, "English", "Operator1", True  # Correctly pass designated_facility
            )
        )
        self.business.add_record(
            Record(
                "Quebec", "Montreal", "234567","Test Facility B", "Preschool", "456 St", "Address 2", "Address 3",
                30, 5, 15, 25, "French", "Operator2", False  # Correctly pass designated_facility
            )
        )

    def test_sort_by_max_children(self):
        """Ensure sorting by max_children works correctly."""
        self.business.sort_records("max_children")
        self.assertEqual(self.business.records[0].max_children, 30)  # The first record should have 30 max_children

    def test_sort_by_region(self):
        """Ensure sorting by region works correctly."""
        self.business.sort_records("region")
        self.assertEqual(self.business.records[0].region, "Ontario")  # The first record should be "Ontario"

if __name__ == '__main__':
    unittest.main()
