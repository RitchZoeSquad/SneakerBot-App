import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import Checkbutton


root = tkinter.Tk()
root.title("Smacker")
root.geometry("200x200")
messagebox.showinfo("Title", "Welcome to Smacker World")
# create a label
label = ttk.Label(root, text="Hello World")
label.pack()
# create a button
button = ttk.Button(root, text="Click Me!")
button.pack()
# create a checkbutton
checkbutton = Checkbutton(root, text="Check Me!")
checkbutton.pack()
# create a spinbox
spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()
# create a scrolledtext
scrolledtext = scrolledtext.ScrolledText(root, width=40, height=10)
scrolledtext.pack()
# create a menu
menu = Menu(root)
root.config(menu=menu)
# create a submenu
submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New")
submenu.add_command(label="Open")
submenu.add_command(label="Save")
submenu.add_separator()
submenu.add_command(label="Exit")
# create a toolbar
toolbar = ttk.Frame(root)
toolbar.pack(side=tkinter.TOP, fill=tkinter.X)
# create a toolbar button
button = ttk.Button(toolbar, text="Button 1")
button.pack(side=tkinter.LEFT)
# create a toolbar button
button = ttk.Button(toolbar, text="Button 2")
button.pack(side=tkinter.LEFT)
# create a toolbar button
root.mainloop() 

