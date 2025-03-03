import csv
filename = "SDCC_Database.csv"

# initializing the titles and rows list
fields = []
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
 # extracting field names through first row
    fields = next(csvreader)
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

         # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))


print(fields[0]+fields[1]+fields[2])
print(rows[0])
print(rows[1])
print(rows[2])
print(type(rows[0]))
item=input("select an id")
item=int(item)
print(rows[item])
IDSelection = input("What ID do you want to edit")
IDSelection=int(IDSelection)
change = input("What do you want to change")
if(change == 'name'):
    newName = input("What is the new name: ")
    rows[IDSelection][1] = newName

else:
    newDescription = input("What is the new description: ")
    rows[IDSelection][1] = newDescription

print("Add new Item")
newId=len(rows)
newDesc = ""
newItem = ""
newRow = []

while(newDesc=="" or newId=="" or NewItem==""):
    NewItem = input("What book do you want to add")
    newDesc=input("What is the description of the book")
    newRow=[newId,NewItem,newDesc]

rows.append(newRow)



print("rows[0][0]"+rows[0][0])
# print(rows[1])
# print(rows[2])
# print(rows)