from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordPetClientLink
from database.src.query.databaseNotebookTabs.links import *
from database.src.utils.constants import typeOfAnimal
from interface.databaseNotebookTabs import links
from interface.databaseNotebookTabs.popupWindows.clients.information import WindowClient
from interface.databaseNotebookTabs.popupWindows.pets.information import WindowPet


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
        self.title('Apagar relação entre animal e dono')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates instance variable so that it can be used later on
        self.master = master

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates 2 LabelFrames that will hold our search buttons for each section
        self.petsSearch = LabelFrame(self.window, text=' Procurar animais ', width=400, height=120)
        self.clientsSearch = LabelFrame(self.window, text=' Procurar clientes ', width=400, height=120)

        # Creates 2 LabelFrames that will hold our pets and clients' trees, respectively
        self.pets = LabelFrame(self.window, text=' Animais ', width=400, height=370)
        self.clients = LabelFrame(self.window, text=' Clientes ', width=400, height=370)

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
        self.labelPetName.grid(column=0, row=0, padx=(5, 5), pady=(20, 10), sticky=W)
        self.entryPetName = Entry(self.petsSearch, textvariable=petName, width=15)
        self.entryPetName.grid(column=1, row=0, padx=(0, 5), pady=(20, 10), sticky=W)
        self.labelPetType = Label(self.petsSearch, text='Tipo:')
        self.labelPetType.grid(column=2, row=0, padx=(5, 5), pady=(20, 10))
        self.entryPetType = Combobox(self.petsSearch, textvariable=petType, state="readonly",
                                     values=[''] + typeOfAnimal, width=10)
        self.entryPetType.grid(column=4, row=0, padx=(0, 5), pady=(20, 10))

        # Creates search filed for clients
        self.labelClientName = Label(self.clientsSearch, text='Nome:')
        self.labelClientName.grid(column=0, row=0, padx=(5, 5), pady=(20, 10), sticky=W)
        self.entryClientName = Entry(self.clientsSearch, textvariable=clientName, width=15)
        self.entryClientName.grid(column=1, row=0, padx=(0, 5), pady=(20, 10), sticky=W)

        # Creates search buttons for each section
        self.petsButton = Button(self.petsSearch, text='Procurar', width=20, command=self.updatePetTree)
        self.clientsButton = Button(self.clientsSearch, text='Procurar', width=20, command=self.updateClientTree)
        self.petsButton.grid(column=0, row=1, padx=5, columnspan=2)
        self.clientsButton.grid(column=0, row=1, padx=5, columnspan=2)

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

        # Creates a Label that tells the user if link already exists or not
        self.statusVar = StringVar(value="Entradas invalidas")
        self.status = Label(self.window, textvariable=self.statusVar)
        self.status.grid(column=1, row=0)

        # Links double click on a row with a window popup
        self.treePets.bind('<Double 1>', self.displayPetWindow)
        self.treeClients.bind('<Double 1>', self.displayClientWindow)

        # Updates every 0.2 seconds the status our Label. Used to tell the user if entries are valid
        self.master.after(200, self.updateLinkLabel)

    def getsPetEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryPetName.get(), self.entryPetType.get()]

    def getsClientEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryClientName.get()]

    def updatePetTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for pets
        [petName, petType] = self.getsPetEntries()

        # If no information was typed, just refresh the page
        if petName == '' and petType == '':
            self.refreshTreePets()
        else:

            # Gets requested rows
            rows = getsRequestedPets([petName, petType])

            # Displays information on our tree
            self.displayTreePetsRows(rows)

    def updateClientTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for clients
        [clientName] = self.getsClientEntries()

        # If no information was typed, just refresh the page
        if clientName == '':
            self.refreshTreeClients()
        else:

            # Gets requested rows
            rows = getsRequestedClients([clientName])

            # Displays information on our tree
            self.displayTreeClientsRows(rows)

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

        # Checks if one row from each tree has been selected. If not, sends an error
        if self.status.cget("text") == "Entradas invalidas":
            messagebox.showerror('ERRO', 'Selecione um animal e um cliente antes de prosseguir!', parent=self.window)
            return

        # Checks if combo of entries is valid. If not, interrupts
        if self.status.cget("text") == "Entrada não existente":
            messagebox.showerror('ERRO', 'Selecione um animal e um cliente que já tenham sido relacionados!',
                                 parent=self.window)
            return

        # Checks if user really wants to delete this link
        message = messagebox.askyesno('Deletar', 'Desejar deletar a ligação entre os elementos?', parent=self.window)

        # If the answer was yes, we can process, else, does nothing
        if message:

            # Gets our tuple of id's. If it got an error, the returned tuple is empty
            tupleOfIDs = self.getsSelectedIDS()

            # Inserts values in our database
            deleteRecordPetClientLink(tupleOfIDs)

            # Refreshes main tree
            links.Links.refreshTree(self.master)

    def updateLinkLabel(self):
        """
        Description:
        > Checks if we have one row from each tree selected. If so, checks if it already exists and displays a message.
        """

        # Gets links of ids
        tupleOfIds = self.getsSelectedIDS()

        # If we don't have a valid entry, then we can't check if link already exists
        if self.checksIfTupleOfIdsIsValid(tupleOfIds):

            # Checks if link is already in the database and tells the user if so
            if checksIfLinkIsAlreadyInDatabase(tupleOfIds):
                self.statusVar.set("Entrada possivel")
            else:
                self.statusVar.set("Entrada não existente")

        self.master.after(200, self.updateLinkLabel)

    def displayPetWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected pet.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.treePets.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:
            # Gets row information
            info = self.treePets.item(item, 'values')

            # Since we only need the pet id to query trough the database, we discard the rest
            petID = info[0]

            # Creates toplevel window that will display the information about this pet
            WindowPet(self, petID)

    def displayClientWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected client.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.treeClients.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:
            # Gets row information
            info = self.treeClients.item(item, 'values')

            # Since we only need the client id to query trough the database, we discard the rest
            clientID = info[0]

            # Creates toplevel window that will display the information about this client
            WindowClient(self, clientID)

    @staticmethod
    def checksIfTupleOfIdsIsValid(Ids):
        """
        Description:
        > Checks if tuple is not empty (invalid).

        :param Ids: tuple of RowIds inside our database -> tuple
        :return: boolean value according to the findings -> boolean
        """
        return Ids != ()
