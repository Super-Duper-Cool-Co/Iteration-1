import csv

CSV_FILE = "SDCC_Database.csv"

class DatabaseManager:
    def __init__(self, file_path=CSV_FILE):
        self.file_path = file_path

    def add_animal(self, animal_data):
        """Adds a new animal entry to the CSV file."""
        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(animal_data)

    def search_animal(self, name):
        """Search for an animal by name and return the row if found."""
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0] == name:
                    return row
        return None

    def edit_animal(self, name, new_population):
        """Edits the population of an animal by name."""
        lines = []
        updated = False
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    row[5] = new_population
                    updated = True
                lines.append(row)

        if updated:
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(lines)
        return updated

    def delete_animal(self, name):
        """Deletes an animal entry from the CSV file."""
        lines = []
        deleted = False
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != name:
                    lines.append(row)
                else:
                    deleted = True

        if deleted:
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(lines)
        return deleted