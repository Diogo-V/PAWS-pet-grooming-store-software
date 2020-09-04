from math import floor
from operator import itemgetter

from database.src.query.databaseNotebookTabs.appointments import getsAllAppointments, getsRequestedAppointments
from database.src.utils.constants import typeOfAnimal
from interface.databaseNotebookTabs.popupWindows.appointments.deletion import WindowDeleteAppointment
from interface.databaseNotebookTabs.popupWindows.appointments.insertion import WindowInsertAppointment
from interface.rootNotebookTabs.popupWindows.appointments.information import *


class Appointments(Frame):
    """
    Frame that holds information about appointments. Has buttons and a tree that allows interactions with the database.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> notebook
        """

        # Creates appointments tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=self.winfo_screenheight(), width=self.winfo_screenwidth())
        self.window.pack(fill='both', expand=True)

        # Creates a database frame, search frame and a display frame to better organize our UI
        self.database = LabelFrame(self.window, text=' Manutenção das entradas ', width=1500, height=100)
        self.search = LabelFrame(self.window, text=' Pesquisar entradas ', width=1500, height=100)
        self.display = LabelFrame(self.window, text=' Visualização das entradas ')
        self.database.pack(padx=20, pady=(10, 0), fill="both", expand=True)
        self.search.pack(padx=20, pady=10, fill="both", expand=True)
        self.display.pack(padx=20, pady=(0, 20), fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.database.grid_propagate(False)
        self.search.grid_propagate(False)
        self.display.grid_propagate(False)

        # Creates buttons to insert, delete and update our entries inside the database
        self.insert = Button(self.database, text='Inserir nova entrada', command=lambda: WindowInsertAppointment(self))
        self.delete = Button(self.database, text='Deletar entrada existente',
                             command=lambda: WindowDeleteAppointment(self))
        self.change = Button(self.database, text='Alterar entrada')
        self.insert.pack(side=LEFT, padx=(310, 0), pady=20)
        self.delete.pack(side=LEFT, padx=(115, 0), pady=20)
        self.change.pack(side=LEFT, padx=(125, 125), pady=20)

        # Allocates memory for the entry values
        petName = StringVar(self.search)
        petType = StringVar(self.search)
        clientName = StringVar(self.search)
        clientPhone = StringVar(self.search)

        # Creates labels and entry fields and puts them on the screen. Used to search inside the database
        self.labelPetName = Label(self.search, text='Nome do animal:')
        self.labelPetName.pack(side=LEFT, padx=(25, 5), pady=20)
        self.entryPetName = Entry(self.search, textvariable=petName)
        self.entryPetName.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelPetType = Label(self.search, text='Tipo de animal:')
        self.labelPetType.pack(side=LEFT, padx=(10, 5), pady=20)
        self.boxPetType = Combobox(self.search, textvariable=petType, state="readonly", values=[''] + typeOfAnimal)
        self.boxPetType.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelClientName = Label(self.search, text='Nome do cliente:')
        self.labelClientName.pack(side=LEFT, padx=(10, 5), pady=20)
        self.entryClientName = Entry(self.search, textvariable=clientName)
        self.entryClientName.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelClientPhone = Label(self.search, text='Telemóvel:')
        self.labelClientPhone.pack(side=LEFT, padx=(10, 5), pady=20)
        self.entryClientPhone = Entry(self.search, textvariable=clientPhone)
        self.entryClientPhone.pack(side=LEFT, padx=(0, 15), pady=20)

        # Creates search button and puts it on the screen
        self.button = Button(self.search, text='Procurar', command=self.updateTree)
        self.button.pack(side=RIGHT, padx=(10, 25), pady=20)

        # Creates tree that will display all the links
        self.tree = Treeview(self.display, columns=(0, 1, 2, 3, 4, 5, 6), height=900)
        self.tree.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))
        self.tree.column(2, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))
        self.tree.column(3, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))
        self.tree.column(4, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))
        self.tree.column(5, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))
        self.tree.column(6, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/6 - 14))

        # Define columns heading
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading(0, text='', anchor='w')
        self.tree.heading(1, text='Nome do animal', anchor='center')
        self.tree.heading(2, text='Tipo de animal', anchor='center')
        self.tree.heading(3, text='Nome do cliente', anchor='center')
        self.tree.heading(4, text='Telemóvel', anchor='center')
        self.tree.heading(5, text='Dia', anchor='center')
        self.tree.heading(6, text='Hora', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbar = Scrollbar(self.display, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Initializes appointments tree view with default rows (every single appointment)
        self.refreshTree()

        # Links double click on a row with a window popup
        self.tree.bind('<Double 1>', self.displayAppointmentWindow)

    def getsEntries(self):
        """
        Description:
        > Gets values inside each entry box and creates a list with those values.
        """
        return [self.entryPetName.get(), self.boxPetType.get(), self.entryClientName.get(), self.entryClientPhone.get()]

    def updateTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets information in entries
        [petName, petType, clientName, clientPhone] = self.getsEntries()

        # If no information was typed, just refresh page
        if petName == '' and petType == '' and clientName == '' and clientPhone == '':
            self.refreshTree()
        else:

            # Gets rows that are going to be displayed
            rows = getsRequestedAppointments([petName, petType, clientName, clientPhone])

            # Displays our queried rows
            self.displayTreeRows(rows)

    def displayAppointmentWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected appointment.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.tree.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:

            # Gets row information
            info = self.tree.item(item, 'values')

            # Since we only need the appointment id to query trough the database, we discard the rest
            appointmentID = info[0]

            # Creates toplevel window that will display the information about this appointment
            WindowAppointment(self, appointmentID)

    def displayTreeRows(self, rows):
        """
        Description:
        > Sorts rows according to pet's name and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.tree.delete(*self.tree.get_children())

        # Sorts rows according to pet's name
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def refreshTree(self):
        """Refreshes all the entries inside the tree. Show default entries."""

        # Gets default rows
        rows = getsAllAppointments()

        # Puts and displays rows in tree
        self.displayTreeRows(rows)
