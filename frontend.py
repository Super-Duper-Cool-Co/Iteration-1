# Import Module

import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('700x400')
Searchbar = Entry(root)
Searchbar.pack()
SearchString = StringVar(Searchbar, "Search Animals")
Searchbar.config(textvariable = SearchString)
btn = Button(root, text = 'Search', ) 
btn.place(x = '415',y='0') 
try:
    img = Image.open("bigmapofcanada.png")  # Open the image
    resized_image = img.resize((500, 305))  # Resize the image
    new_image = ImageTk.PhotoImage(resized_image)  # Convert to Tkinter PhotoImage

    # Example of how to display the image in a Tkinter window:
    
    label = tk.Label(root, image=new_image)
    label.image = new_image  # Keep a reference!
    label.pack()
    

except FileNotFoundError:
    print("Error: bigmapofcanada.png not found.")
except Exception as e:
    print(f"An error occurred: {e}")

root.mainloop()


