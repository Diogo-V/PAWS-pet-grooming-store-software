from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- ROOT AND NOTEBOOK --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


root = Tk()  # Creates root window
root.title('PAWS - Pet Grooming Store Software')  # Window title
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='images/paw.ico'))  # Puts an icon on the window
root.attributes('-zoomed', True)  # Initializes windows as

# Creates root notebook
notebook = ttk.Notebook(root)
notebook.pack()

# Changes style of notebook tabs
ttk.Style().theme_settings(ttk.Style().theme_use(), {"TNotebook.Tab": {"configure": {"padding": [190.4, 9]}}})

# Creates frames inside the notebook
frameAppointments = ttk.Frame(notebook, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
frameDatabase = ttk.Frame(notebook, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
frameStatistics = ttk.Frame(notebook, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

# Puts the frames on the screen
frameAppointments.pack(fill="both", expand=True)
frameDatabase.pack(fill="both", expand=True)
frameStatistics.pack(fill="both", expand=True)

# Creates tabs inside our notebook
notebook.add(frameAppointments, text='Appointments')
notebook.add(frameDatabase, text='Database')
notebook.add(frameStatistics, text='Statistics')


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- APPOINTMENTS FRAME -------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------ DATABASE FRAME ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------- STATISTICS FRAME --------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# Closes main window
root.mainloop()
