# Import Module
import csv
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
filename = "Files/SDCC_Database.csv"

# initializing the titles and rows list
fields = []
rows = []
def readRows():
    
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

root=Tk()

def createRoot(root):
    
    
    # Set geometry (widthxheight)
   
    Searchbar = Entry(root)
    Searchbar.pack()
    SearchString = StringVar(Searchbar, "Search Animals")
    Searchbar.config(textvariable = SearchString)
    btn = Button(root, text = 'Search', command=onclick ) 
    btn.place(x = '415',y='0') 
    try:
        img = Image.open("Files/bigmapofcanada.png")  # Open the image
        resized_image = img.resize((500, 305))  # Resize the image
        new_image = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter PhotoImage

        # Example of how to display the image in a Tkinter window:
        
        label = tk.Label(root, image=new_image)
        label.image = new_image  # Keep a reference!
        
        button =Button(root, image=new_image,command=onclick)
        button.pack()
        

    except FileNotFoundError:
        print("Error: bigmapofcanada.png not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def onclick():
    # print("Jonathan")
    # newWindow=Tk()
    # label= Label(newWindow, text="List of Animals")
    # label.config(font=("Courier",14))
    # label.pack()
    # text=Text(newWindow,height=50,width=150)
    # text.pack()
    
    
    print(fields)
    i=0
    for row2 in rows:
        j=0
        for entry in row2:
            e = Entry(root, width=20, fg='blue',font=('Arial',16,'bold'))
                 
            e.grid(row=i, column=j)
            e.insert(END, entry)
            # text.insert(END, entry)
            j+=1
        i+=1
        # text.insert(END,"\n")

    

createRoot(root)
# create root window

readRows()
root.mainloop()

# root window title and dimension



