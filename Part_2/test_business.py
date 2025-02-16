# test_business.py
import unittest
from business import DataManager
from record import Record

class TestBusinessLayer(unittest.TestCase):
    def test_add_record(self):
        data_manager = DataManager()
        record = Record("Region1", "District1", "123", "Facility1", "Daycare", "Address 1", "", "", 30, 10, 10, 10, "English", "Operator1", True)
        data_manager.add_record(record)
        self.assertEqual(len(data_manager.records), 1)
        self.assertEqual(data_manager.records[0], record)

if __name__ == "__main__":
    unittest.main()
