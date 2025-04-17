# ------------------------------------------------------
# Filename: test_sorting.py
# Author: Nibedita Bhowmick
# Due Date: 2025-03-16
# Version: 1.1
# Description:
#     This module contains unit tests for verifying the sorting functionality
#     in the Business class. It ensures records are sorted correctly based on
#     various attributes.
# ------------------------------------------------------

import unittest  # Import the unittest module for testing
from business import Business  # Import the Business class
from record import Record  # Import the Record class for record creation


class TestSorting(unittest.TestCase):
    """
    Unit test class for testing the sorting functionality of the Business class.
    """

    def setUp(self):
        """
        Sets up the test environment by initializing a Business instance
        and adding sample records before each test case is executed.
        """
        self.business = Business()  # Initialize the Business class

        # Add test records with complete attributes for sorting validation
        self.business.add_record(
            Record(
                "Ontario", "Toronto", "123456", "Daycare", "Full_time Centre",
                "Address 1", "Address 2", "Address 3", 50, 10, 20, 30,
                "English", "Operator1", True  # Correctly pass designated_facility as a boolean
            )
        )
        self.business.add_record(
            Record(
                "Quebec", "Montreal", "234567", "Test Facility B", "Preschool",
                "456 St", "Address 2", "Address 3", 30, 5, 15, 25,
                "French", "Operator2", False  # Correctly pass designated_facility as a boolean
            )
        )

    def test_sort_by_max_children(self):
        """
        Tests if records are sorted correctly based on the 'max_children' attribute.
        The record with the smallest max_children value should appear first.
        """
        self.business.sort_records("max_children")
        self.assertEqual(self.business.records[0].max_children, 30)  # The first record should have 30 max_children

    def test_sort_by_region(self):
        """
        Tests if records are sorted correctly based on the 'region' attribute.
        Alphabetical order should place 'Ontario' before 'Quebec'.
        """
        self.business.sort_records("region")
        self.assertEqual(self.business.records[0].region, "Ontario")  # The first record should be "Ontario"


# Run the unit tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
