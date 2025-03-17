import csv
import pandas as pd
import atexit

# Define filename
filename = "Files/SDCC_Database.csv"

# Load data from CSV
def load_data():
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)  # Extract field names
        for row in csvreader:
            rows.append(row)
    return fields, rows

# Save data back to CSV
def save_data(fields, rows):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

# Display menu
def display_menu():
    print("\nChoose an option:")
    print("1. Get all animal's description")
    print("2. Get one animal's description")
    print("3. Find animals in a specific province")
    print("4. Search animals by diet")
    print("5. Add a new animal")
    print("6. Edit an animal's details")
    print("7. Delete an animal")
    print("8. Exit")

# Display all animals and their descriptions
def display_all_animals(rows):
    print("\nAll Animals and Their Descriptions:")
    for row in rows:
        print(f"{row[0]} - Class: {row[1]}, Diet: {row[2]}, Province: {row[3]}, Status: {row[4]}, Population: {row[5]}, Native/Invasive: {row[6]}, Habitat: {row[7]}")

# Get an animal's description
def get_animal_description(rows):
    animal_name = input("Enter the animal name: ").strip().lower()
    for row in rows:
        if row[0].lower() == animal_name:
            print(f"{row[0]} - Class: {row[1]}, Diet: {row[2]}, Province: {row[3]}, Status: {row[4]}, Population: {row[5]}, Native/Invasive: {row[6]}, Habitat: {row[7]}")
            return
    print("Animal not found.")

# Find animals in a specific province
def find_by_province(rows):
    province = input("Enter the province: ").strip().upper()
    found = [row for row in rows if row[3] == province]
    if found:
        for row in found:
            print(row[0])
    else:
        print("No animals found in this province.")

# Search animals by diet
def search_by_diet(rows):
    diet = input("Enter diet type (Carnivore, Herbivore, Omnivore): ").strip().capitalize()
    found = [row for row in rows if row[2] == diet]
    if found:
        for row in found:
            print(row[0])
    else:
        print("No animals found with this diet.")

# Add a new animal
def add_animal(fields, rows):
    new_animal = []
    for field in fields:
        new_animal.append(input(f"Enter {field}: ").strip())
    rows.append(new_animal)
    save_data(fields, rows)
    print("Animal added successfully.")

# Edit an animal's details
def edit_animal(rows):
    animal_name = input("Enter the animal name to edit: ").strip().lower()
    for row in rows:
        if row[0].lower() == animal_name:
            print("Current details:", row)
            field_to_edit = input("Which field do you want to change? (Class, Diet, Province, etc.): ").strip()
            if field_to_edit in fields:
                new_value = input(f"Enter new value for {field_to_edit}: ").strip()
                row[fields.index(field_to_edit)] = new_value
                save_data(fields, rows)
                print("Animal updated successfully.")
                return
    print("Animal not found.")

# Delete an animal
def delete_animal(rows):
    animal_name = input("Enter the animal name to delete: ").strip().lower()
    for i, row in enumerate(rows):
        if row[0].lower() == animal_name:
            rows.pop(i)
            save_data(fields, rows)
            print("Animal deleted successfully.")
            return
    print("Animal not found.")

def write_to_html():
    columns = ["Animal","Class","Diet","Province","Endangered Status","Population","Native/Invasive","Habitat"]
    df = pd.read_csv('Files/SDCC_Database.csv', names=columns)

    html_string =df.to_html()
    Func = open('Files/list.html','w')
    Func.write(html_string)
    Func.close()

atexit.register(write_to_html)

# Main loop
fields, rows = load_data()
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        display_all_animals(rows)
    elif choice == '2':
        get_animal_description(rows)
    elif choice == '3':
        find_by_province(rows)
    elif choice == '4':
        search_by_diet(rows)
    elif choice == '5':
        add_animal(fields, rows)
    elif choice == '6':
        edit_animal(rows)
    elif choice == '7':
        delete_animal(rows)
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
