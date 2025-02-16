import unittest
from persistence import load_data, save_data, generate_output_filename

class TestPersistence(unittest.TestCase):
    def test_generate_output_filename(self):
        filename = generate_output_filename()
        self.assertTrue(filename.startswith("output_") and filename.endswith(".csv"))

if __name__ == '__main__':
    unittest.main()
