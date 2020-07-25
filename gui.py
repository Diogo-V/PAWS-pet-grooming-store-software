from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()  # Creates root window
root.title('PAWS - Pet Grooming Store Software')  # Window title
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='images/paw.ico'))  # Puts an icon on the window
root.attributes('-zoomed', True)  # Initializes windows as
root.resizable(FALSE, FALSE)  # Blocks window resizing




# Closes main window
root.mainloop()
