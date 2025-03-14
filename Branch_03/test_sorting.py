import unittest
from business import DataManager
from record import Record

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.data_manager.add_record(Record("Ontario", "Toronto", "Test Facility A", "Daycare", "123 St", 50))
        self.data_manager.add_record(Record("Quebec", "Montreal", "Test Facility B", "Preschool", "456 St", 30))

    def test_sort_by_max_children(self):
        """Ensure sorting by max_children works correctly."""
        self.data_manager.sort_records("max_children")
        self.assertEqual(self.data_manager.records[0].max_children, 30)

    def test_sort_by_region(self):
        """Ensure sorting by region works correctly."""
        self.data_manager.sort_records("region")
        self.assertEqual(self.data_manager.records[0].region, "Ontario")

if __name__ == '__main__':
    unittest.main()
