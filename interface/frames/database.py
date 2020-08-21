from tkinter import *
from tkinter.ttk import *


class Database(Frame):
    """
    Frame that holds buttons and options to access, modify and update our database.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        """

        # Creates database tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=self.winfo_screenheight(), width=self.winfo_screenmmwidth())
        self.window.pack(fill='both', expand=True)

        # Creates database's notebook
        self.notebook = Notebook(self.window)
        self.notebook.pack(fill='both', expand=True)

        # Creates notebook's frames -> pets, clients, links, appointments and history
        self.petsFrame = Frame(self.notebook)
        self.clientsFrame = Frame(self.notebook)
        self.linkFrame = Frame(self.notebook)
        self.appointmentsFrame = Frame(self.notebook)
        self.historyFrame = Frame(self.notebook)

        # Adds the previously created frames to the notebook
        self.notebook.add(self.petsFrame, text='Animais')
        self.notebook.add(self.clientsFrame, text='Animais')
        self.notebook.add(self.linkFrame, text='Animais')
        self.notebook.add(self.appointmentsFrame, text='Animais')
        self.notebook.add(self.historyFrame, text='Animais')
