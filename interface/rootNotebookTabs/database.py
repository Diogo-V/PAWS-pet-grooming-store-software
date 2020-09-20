from tkinter import *
from tkinter.ttk import *

from interface.databaseNotebookTabs.appointments import Appointments
from interface.databaseNotebookTabs.clients import Clients
from interface.databaseNotebookTabs.history import History
from interface.databaseNotebookTabs.links import Links
from interface.databaseNotebookTabs.pets import Pets


class Database(Frame):
    """
    Frame that holds buttons and options to access, modify and update each entry of our database.
    """

    def __init__(self, master, root, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        :param root: Main application frame window -> Frame
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

        # Creates notebook's tabs -> pets, clients, links, appointments and history
        self.petsFrame = Pets(self.notebook, root)
        self.clientsFrame = Clients(self.notebook, root)
        self.linkFrame = Links(self.notebook, root)
        self.appointmentsFrame = Appointments(self.notebook, root)
        self.historyFrame = History(self.notebook)

        # Adds the previously created tabs to the notebook
        self.notebook.add(self.petsFrame, text='Animais')
        self.notebook.add(self.clientsFrame, text='Clientes')
        self.notebook.add(self.linkFrame, text='Relação')
        self.notebook.add(self.appointmentsFrame, text='Marcações')
        self.notebook.add(self.historyFrame, text='Histórico')

    def refreshAllTabs(self):
        """Refreshes all tree inside each tab of our database."""
        self.petsFrame.updateTree()
        self.clientsFrame.updateTree()
        self.linkFrame.updateTree()
        self.appointmentsFrame.updateTree()
