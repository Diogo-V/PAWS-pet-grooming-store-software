from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from database.src.functions.deletion import deleteRecordPetClientLink
from interface.databaseNotebookTabs import links
from database.src.query.databaseNotebookTabs.links import getsPetsForLinksWindow, getsClientsForLinksWindow
from database.src.utils.constants import typeOfAnimal


class WindowDeleteLink(Toplevel):
    """
    Toplevel window used to delete a relationship between an animal and an owner.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Inserir nova relação entre animal e dono')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates instance variable so that it can be used later on
        self.master = master

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates 2 LabelFrames that will hold our search buttons for each section
        self.petsSearch = LabelFrame(self.window, text=' Procurar animais ', width=400, height=100)
        self.clientsSearch = LabelFrame(self.window, text=' Procurar clientes ', width=400, height=100)

        # Creates 2 LabelFrames that will hold our pets and clients' trees, respectively
        self.pets = LabelFrame(self.window, text=' Animais ', width=400, height=400)
        self.clients = LabelFrame(self.window, text=' Clientes ', width=400, height=400)

        # Puts our labelFrames on the screen
        self.petsSearch.grid(column=0, row=0)
        self.clientsSearch.grid(column=2, row=0)
        self.pets.grid(column=0, row=1, rowspan=5)
        self.clients.grid(column=2, row=1, rowspan=5)

        # Blocks resize
        self.petsSearch.grid_propagate(False)
        self.clientsSearch.grid_propagate(False)
        self.pets.grid_propagate(False)
        self.clients.grid_propagate(False)

        # Creates link button and puts it on the screen
        self.link = Button(self.window, text='Deletar ligação', command=self.removeEntries)
        self.link.grid(column=1, row=2, padx=45)

        # Creates needed entry variables
        petName = StringVar(self.petsSearch)
        petType = StringVar(self.petsSearch)
        clientName = StringVar(self.clientsSearch)

        # Creates search fields for pets
        self.labelPetName = Label(self.petsSearch, text='Nome:')
        self.labelPetName.pack(side=LEFT, padx=(5, 5), pady=20)
        self.entryPetName = Entry(self.petsSearch, textvariable=petName, width=15)
        self.entryPetName.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelPetType = Label(self.petsSearch, text='Tipo:')
        self.labelPetType.pack(side=LEFT, padx=(5, 5), pady=20)
        self.entryPetType = Combobox(self.petsSearch, textvariable=petType, state="readonly",
                                     values=[''] + typeOfAnimal, width=10)
        self.entryPetType.pack(side=LEFT, padx=(0, 5), pady=20)

        # Creates search filed for clients
        self.labelClientName = Label(self.clientsSearch, text='Nome:')
        self.labelClientName.pack(side=LEFT, padx=(91, 5), pady=20)
        self.entryClientName = Entry(self.clientsSearch, textvariable=clientName, width=15)
        self.entryClientName.pack(side=LEFT, padx=(0, 91), pady=20)

        # Creates tree that will display all the pets information
        self.treePets = Treeview(self.pets, columns=(0, 1, 2), height=17)
        self.treePets.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.treePets.column("#0", stretch=NO, anchor='center', width=0)
        self.treePets.column(0, stretch=NO, anchor='center', width=0)
        self.treePets.column(1, stretch=NO, anchor='center', width=228)
        self.treePets.column(2, stretch=NO, anchor='center', width=130)

        # Define columns heading
        self.treePets.heading('#0', text='', anchor='w')
        self.treePets.heading(0, text='', anchor='w')
        self.treePets.heading(1, text='Nome', anchor='center')
        self.treePets.heading(2, text='Tipo', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarPets = Scrollbar(self.pets, orient="vertical", command=self.treePets.yview)
        self.scrollbarPets.pack(side=RIGHT, fill="y")
        self.treePets.configure(yscrollcommand=self.scrollbarPets.set)

        # Creates tree that will display all the links
        self.treeClients = Treeview(self.clients, columns=(0, 1), height=17)
        self.treeClients.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.treeClients.column("#0", stretch=NO, anchor='center', width=0)
        self.treeClients.column(0, stretch=NO, anchor='center', width=0)
        self.treeClients.column(1, stretch=NO, anchor='center', width=358)

        # Define columns heading
        self.treeClients.heading('#0', text='', anchor='w')
        self.treeClients.heading(0, text='', anchor='w')
        self.treeClients.heading(1, text='Nome', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarClients = Scrollbar(self.clients, orient="vertical", command=self.treeClients.yview)
        self.scrollbarClients.pack(side=RIGHT, fill="y")
        self.treeClients.configure(yscrollcommand=self.scrollbarClients.set)

        # Populates both trees with their default values
        self.refreshTreePets()
        self.refreshTreeClients()

        # Links double click on a row with a window popup
        # self.treePets.bind('<Double 1>', self.displayPetWindow)
        # self.treeClients.bind('<Double 1>', self.displayClientWindow)

    def refreshTreePets(self):
        """
        Description:
        > Gets all the default values for the corresponding tree.
        """

        # Gets default values for animals
        rows = getsPetsForLinksWindow()

        # Displays rows
        self.displayTreePetsRows(rows)

    def displayTreePetsRows(self, rows):
        """
        Description:
        > Sorts rows according to pet's name and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.treePets.delete(*self.treePets.get_children())

        # Sorts rows according to pet's name
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.treePets.insert('', 'end', values=row)

    def refreshTreeClients(self):
        """
        Description:
        > Gets all the default values for the corresponding tree.
        """

        # Gets default values for animals
        rows = getsClientsForLinksWindow()

        # Displays rows
        self.displayTreeClientsRows(rows)

    def displayTreeClientsRows(self, rows):
        """
        Description:
        > Sorts rows according to client's name and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.treeClients.delete(*self.treeClients.get_children())

        # Sorts rows according to pet's name
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.treeClients.insert('', 'end', values=row)

    def getsSelectedIDS(self):
        """
        Description:
        > Gets a tuple of the selected id's of a pet and a client.
        :return tuple of id's -> tuple of integers
        """

        # Gets selected values
        pets = self.treePets.selection()
        clients = self.treeClients.selection()

        # If entries are valid, we return a tuple of them, else, returns an empty tuple
        if pets != () and clients != ():
            return self.treePets.item(pets[0], "values")[0], self.treeClients.item(clients[0], "values")[0]
        else:
            return ()

    def removeEntries(self):
        """
        Description:
        > Checks if the user really wants to delete this link and if so, does it.
        """

        # Gets our tuple of id's. If it got an error, the returned tuple is empty
        tupleOfIDs = self.getsSelectedIDS()

        # Checks if tuple of id's is valid. If not, shows an error and stops execution
        if not self.checksIfTupleOfIdsIsValid():
            messagebox.showerror('ERRO', 'Selecione um animal e um cliente antes de prosseguir!', parent=self.window)
            return

        # Checks if user really wants to delete this link
        message = messagebox.askyesno('Deletar', 'Desejar deletar a ligação entre os elementos?', parent=self.window)

        # If the answer was yes, we can process, else, does nothing
        if message:

            # Inserts values in our database
            deleteRecordPetClientLink(tupleOfIDs)

            # Refreshes main tree
            links.Links.refreshTree(self.master)

    @staticmethod
    def checksIfTupleOfIdsIsValid(Ids):
        """
        Description:
        > Checks if tuple is not empty (invalid).

        :param Ids: tuple of RowIds inside our database -> tuple
        :return: boolean value according to the findings -> boolean
        """
        return Ids != ()
