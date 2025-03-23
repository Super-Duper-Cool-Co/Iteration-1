import csv
import pandas as pd
import atexit
from Animal import *

# Define filename
filename = "Files/SDCC_Database.csv"

# Load data from CSV
def load_data():
    fields = []
    animalList = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)  # Extract field names
        for row in csvreader:
            newAnimal= Animal(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            animalList.append(newAnimal)
    for field in fields:
        field=field.strip()
        print(f"field= {field}")
    return fields, animalList

# Save data back to CSV
def save_data(fields, rows):
    animals=[]
    for animal in rows:
        animals.append([animal.name, animal.type, animal.diet, animal.province, animal.endagerStatus, animal.population, animal.invasiveStatus, animal.habitat])
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(animals)

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
        row.toString()
6
# Get an animal's description
def get_animal_description(rows,name):
    for row in rows:
        if row.name.upper() == name.upper():
            print(row.name)
            return row
    print("Animal not found.")

# Find animals in a specific province
def find_by_province(rows, province):
    animalslist=[]
    for animal in rows:
        if animal.province== province:
            animalslist.append(animal)
    if len(animalslist)>0:
        return animalslist
    else:
        print("No animals found in this province.")

# Search animals by diet
def search_by_diet(rows,diet):
    animallist=[]
    for animal in rows:
        if animal.diet== diet:
            animallist.append(animal)
    if len(animallist)>0:
        return animallist
    else:
        print("No animals found with this diet.")

# Add a new animal
def add_animal(fields, rows):
    new_animal = []
    for field in fields:
        new_animal.append(input(f"Enter {field}: ").strip())
    animal= Animal(new_animal[0],new_animal[1],new_animal[2],new_animal[3],new_animal[4],new_animal[5],new_animal[6],new_animal[7])
    rows.append(animal)
    save_data(fields, rows)
    print("Animal added successfully.")

# Edit an animal's details
# def edit_animal(fields, rows):
#     """
#     Edits the details of an animal based on its name.

#     Args:
#         fields (list): A list of field names.
#         rows (list): A list of Animal objects.
#     """
#     animal_name = input("Enter the animal name to edit: ").strip().lower()

#     for animal in rows:  # Iterate through Animal objects, not raw rows
#         if animal.name.lower() == animal_name:
#             print("Current details: ", end="")
#             print(animal.toString()) #using print(animal) now that we are using the __str__ method.
#             print(fields)
#             field_to_edit = input("Which field do you want to change? (name, species, breed, etc.): ").strip()

#             if field_to_edit in fields:
#                 new_value = input(f"Enter new value for {field_to_edit}: ").strip()
#                 try:
#                     setattr(animal, field_to_edit, new_value) #use setattr to change the attribute of the animal object.
#                     save_data(fields, rows) #needs to be defined.
#                     print("Animal updated successfully.")
#                     return
#                 except AttributeError:
#                   print(f"Error: Field '{field_to_edit}' does not exist.")
#                   return
#             else:
#                 print(f"Error: Field '{field_to_edit}' not found.")
#                 return

#     print("Animal not found.")

# Delete an animal
def delete_animal(fields, rows):
    animal_name = input("Enter the animal name to delete: ").strip().lower()
    i=0
    for row in rows:
        if row.name.lower() == animal_name:
            rows.pop(i)
            save_data(fields, rows)
            print("Animal deleted successfully.")
            return
        i+=1
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
        name = input("Enter the animal name: ")
        animal=get_animal_description(rows, name)
        animal.toString()
    elif choice == '3':
        province = input("Enter the province animal can be found: ")
        animals=find_by_province(rows, province)
        for animal in animals:
            animal.toString()
    elif choice == '4':
       province = input("Enter the diet the animal can eats: ")
       animals=search_by_diet(rows, province)
       for animal in animals:
            animal.toString()
    elif choice == '5':
        add_animal(fields, rows)
    elif choice == '6':
        edit_animal(fields,rows)
    elif choice == '7':
        delete_animal(fields, rows)
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
