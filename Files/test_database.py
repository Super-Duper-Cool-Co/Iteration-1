import unittest
import csv
from database_manager import DatabaseManager

CSV_FILE = "SDCC_Database.csv"

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        """Load the original CSV content before each test."""
        with open(CSV_FILE, "r") as file:
            self.original_data = file.readlines()
        self.db = DatabaseManager(CSV_FILE)

    def tearDown(self):
        """Restore the original CSV after each test."""
        with open(CSV_FILE, "w") as file:
            file.writelines(self.original_data)

    def test_add_animal(self):
        """Test adding an animal through the DatabaseManager."""
        new_animal = ["Test Animal", "Test Class", "Test Diet", "Test Province", "Test Status", "123", "Test Origin", "Test Habitat"]
        self.db.add_animal(new_animal)

        with open(CSV_FILE, "r") as file:
            data = file.readlines()
            self.assertIn(",".join(new_animal) + "\n", data)

    def test_search_animal(self):
        """Test searching for an existing animal."""
        search_name = "Moose"
        result = self.db.search_animal(search_name)
        self.assertIsNotNone(result)

    def test_edit_animal(self):
        """Test editing an animal's population field."""
        edit_name = "dog"
        updated_population = "1000"

        success = self.db.edit_animal(edit_name, updated_population)
        self.assertTrue(success)

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == edit_name:
                    self.assertEqual(row[5], updated_population)

    def test_delete_animal(self):
        """Test deleting an animal entry."""
        delete_name = "Test Animal"
        self.db.add_animal(["Test Animal", "Test Class", "Test Diet", "Test Province", "Test Status", "123", "Test Origin", "Test Habitat"])

        deleted = self.db.delete_animal(delete_name)
        self.assertTrue(deleted)

        with open(CSV_FILE, "r") as file:
            data = file.read()
            self.assertNotIn(delete_name, data)

if __name__ == "__main__":
    unittest.main()