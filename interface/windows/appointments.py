from tkinter import *
from tkinter.ttk import *
from database.src.utils.querying import *
from datetime import date


class Appointments(Frame):
    """
    Frame that holds appointments for the day.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        """

        # Creates appointments tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=self.winfo_screenheight(), width=self.winfo_screenwidth())
        self.window.pack(fill='both', expand=True)

        # Creates a search frame and a display frame and puts them on the screen
        self.search = LabelFrame(self.window, text='Pesquisar dia', width=1200, height=100)
        self.display = LabelFrame(self.window, text='Marcações')
        self.search.pack()
        self.display.pack()

        # Creates tree that will display all the appointments for the day
        self.tree = Treeview(self.display, columns=(1, 2, 3, 4, 5, 6))
        self.tree.pack(padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center')
        self.tree.column(2, stretch=NO, anchor='center')
        self.tree.column(3, stretch=NO, anchor='center')
        self.tree.column(4, stretch=NO, anchor='center')
        self.tree.column(5, stretch=NO, anchor='center')
        self.tree.column(6, stretch=NO, anchor='center')

        # Define columns heading
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading(1, text='Nome do animal', anchor='center')
        self.tree.heading(2, text='Nome do cliente', anchor='center')
        self.tree.heading(3, text='Serviços', anchor='center')
        self.tree.heading(4, text='Hora', anchor='center')
        self.tree.heading(5, text='Número de telemóvel', anchor='center')
        self.tree.heading(6, text='Observações', anchor='center')

        # Gets information inside the tree
        self.information = getsDayAppointments(date.today())

        # Puts information in the tree
        self.updateTree(self.information)

    def updateTree(self, rows):
        """
        Description:
        > Creates and updates rows inside our tree view.

        :param rows: list of contents to be display -> list
        """
        for row in rows:
            self.tree.insert('', 'end', values=row)
