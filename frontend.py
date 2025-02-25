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
btn.place(x = '415',y='5') 
#Load an image in the script
img= (Image.open("bigmapofcanada.png"))

#Resize the Image using resize method
resized_image= img.resize((300,205))
new_image= ImageTk.PhotoImage(resized_image)

# all widgets will be here
# Execute Tkinter
root.mainloop()


