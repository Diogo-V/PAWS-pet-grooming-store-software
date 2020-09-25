from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordPetClientLink, deleteRecordAnimal, deleteRecordClient
from database.src.query.databaseNotebookTabs.links import *
from database.src.utils.constants import typeOfAnimal
from interface.databaseNotebookTabs.popupWindows.clients.information import WindowClient
from interface.databaseNotebookTabs.popupWindows.pets.information import WindowPet


class WindowDeleteLink(Toplevel):
    """
    Toplevel window used to delete a relationship between an animal and an owner.
    """

    def __init__(self, master, root):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param root: Main application frame window -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Selecionar a relação entre animal e dono que deseja eliminar')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates a root variable so that we can access the main application window
        self.root = root
        self.master = master

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=600, width=1250)
        self.window.pack(fill='both', expand=True)

        # Creates 2 LabelFrames that will hold our search buttons for each section
        self.petsSearch = LabelFrame(self.window, text=' Procurar animais ', width=500, height=120)
        self.clientsSearch = LabelFrame(self.window, text=' Procurar clientes ', width=500, height=120)

        # Creates 2 LabelFrames that will hold our pets and clients' trees, respectively
        self.pets = LabelFrame(self.window, text=' Animais ', width=500, height=370)
        self.clients = LabelFrame(self.window, text=' Clientes ', width=500, height=370)

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
        auxFrame = Frame(self.window)
        auxFrame.grid(column=1, row=2, sticky=(W, S, N, E))
        auxFrame.grid_propagate(False)
        self.link = Button(auxFrame, text='Remover', command=self.removeEntries, width=27)
        self.link.pack(side=LEFT, fill="both", expand=True, padx=10)

        # Creates needed entry variables
        petName = StringVar(self.petsSearch)
        petType = StringVar(self.petsSearch)
        petBreed = StringVar(self.petsSearch)
        clientName = StringVar(self.clientsSearch)
        clientPhone = StringVar(self.clientsSearch)

        # Creates search fields for pets
        self.labelPetName = Label(self.petsSearch, text='Nome:')
        self.labelPetName.grid(column=0, row=0, padx=(5, 5), pady=(20, 10), sticky=W)
        self.entryPetName = Entry(self.petsSearch, textvariable=petName, width=13)
        self.entryPetName.grid(column=1, row=0, padx=(0, 5), pady=(20, 10), sticky=W)
        self.labelPetType = Label(self.petsSearch, text='Tipo:')
        self.labelPetType.grid(column=2, row=0, padx=(5, 5), pady=(20, 10))
        self.entryPetType = Combobox(self.petsSearch, textvariable=petType, state="readonly",
                                     values=[''] + typeOfAnimal, width=10)
        self.entryPetType.grid(column=4, row=0, padx=(0, 5), pady=(20, 10), sticky=W)
        self.labelPetBreed = Label(self.petsSearch, text='Raça:')
        self.labelPetBreed.grid(column=5, row=0, padx=(5, 5), pady=(20, 10), sticky=W)
        self.entryPetBreed = Entry(self.petsSearch, textvariable=petBreed, width=13)
        self.entryPetBreed.grid(column=6, row=0, padx=(0, 5), pady=(20, 10), sticky=W)

        # Creates search filed for clients
        self.labelClientName = Label(self.clientsSearch, text='Nome:')
        self.labelClientName.grid(column=0, row=0, padx=(5, 5), pady=(20, 10), sticky=W)
        self.entryClientName = Entry(self.clientsSearch, textvariable=clientName, width=15)
        self.entryClientName.grid(column=1, row=0, padx=(0, 5), pady=(20, 10), sticky=W)
        self.labelClientPhone = Label(self.clientsSearch, text='Telemóvel:')
        self.labelClientPhone.grid(column=2, row=0, padx=(30, 5), pady=(20, 10), sticky=W)
        self.entryClientPhone = Entry(self.clientsSearch, textvariable=clientPhone, width=15)
        self.entryClientPhone.grid(column=3, row=0, padx=(0, 5), pady=(20, 10), sticky=W)

        # Creates search buttons for each section
        self.petsButton = Button(self.petsSearch, text='Procurar', width=20, command=self.updatePetTree)
        self.clientsButton = Button(self.clientsSearch, text='Procurar', width=20, command=self.updateClientTree)
        self.petsButton.grid(column=0, row=1, padx=5, columnspan=3)
        self.clientsButton.grid(column=0, row=1, padx=5, columnspan=2)

        # Columns names that are going to be inserted inside the tree
        columnsPets = ('', 'Nome', 'Tipo', 'Raça', 'Cliente')

        # Creates tree that will display all the pets information
        self.treePets = Treeview(self.pets, columns=columnsPets, height=21, show='headings')
        self.treePets.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.treePets.column("#0", stretch=NO, anchor='center', width=0)
        self.treePets.column(0, stretch=NO, anchor='center', width=0)
        self.treePets.column(1, stretch=NO, anchor='center', width=115)
        self.treePets.column(2, stretch=NO, anchor='center', width=115)
        self.treePets.column(3, stretch=NO, anchor='center', width=115)
        self.treePets.column(4, stretch=NO, anchor='center', width=115)

        # Define columns heading and sets their sorting function
        for col in columnsPets:
            self.treePets.heading(col, text=col, command=lambda _col=col:
                                     self.treeSortColumn(self.treePets, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarPets = Scrollbar(self.pets, orient="vertical", command=self.treePets.yview)
        self.scrollbarPets.pack(side=RIGHT, fill="y")
        self.treePets.configure(yscrollcommand=self.scrollbarPets.set)

        # Columns names that are going to be inserted inside the tree
        columnsClients = ('', 'Nome', 'Telemóvel', 'Animal')

        # Creates tree that will display all the links
        self.treeClients = Treeview(self.clients, columns=columnsClients, height=21, show='headings')
        self.treeClients.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.treeClients.column("#0", stretch=NO, anchor='center', width=0)
        self.treeClients.column(0, stretch=NO, anchor='center', width=0)
        self.treeClients.column(1, stretch=NO, anchor='center', width=153)
        self.treeClients.column(2, stretch=NO, anchor='center', width=153)
        self.treeClients.column(3, stretch=NO, anchor='center', width=153)

        # Define columns heading and sets their sorting function
        for col in columnsClients:
            self.treeClients.heading(col, text=col, command=lambda _col=col:
                                     self.treeSortColumn(self.treeClients, _col, False), anchor='center')

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
        self.status.grid(column=1, row=0, padx=50)

        # Links double click on a row with a window popup
        self.treePets.bind('<Double 1>', self.displayPetWindow)
        self.treeClients.bind('<Double 1>', self.displayClientWindow)

        # Updates every 0.2 seconds the status our Label. Used to tell the user if entries are valid
        self.master.after(200, self.updateLinkLabel)

    def treeSortColumn(self, tv, col, reverse):
        """
        Description:
        > Sorts the clicked column of the tree.
        :param tv: tree -> TreeView
        :param col: selected column name -> string
        :param reverse: checks if we need to reverse it -> boolean
        """

        # Gets lines from the selected column
        lines = [(tv.set(k, col), k) for k in tv.get_children('')]

        # Sorts
        lines.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(lines):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, text=col, command=lambda _col=col: self.treeSortColumn(tv, _col, not reverse))

    def getsPetEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryPetName.get(), self.entryPetType.get(), self.entryPetBreed.get()]

    def getsClientEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryClientName.get(), self.entryClientPhone.get()]

    def updatePetTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for pets
        [petName, petType, petBreed] = self.getsPetEntries()

        # If no information was typed, just refresh the page
        if petName == '' and petType == '' and petBreed == '':
            self.refreshTreePets()
        else:

            # Gets requested rows
            rows = getsRequestedPets([petName, petType, petBreed])

            # Displays information on our tree
            self.displayTreePetsRows(rows)

    def updateClientTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for clients
        [clientName, clientPhone] = self.getsClientEntries()

        # If no information was typed, just refresh the page
        if clientName == '' and clientPhone == '':
            self.refreshTreeClients()
        else:

            # Gets requested rows
            rows = getsRequestedClients([clientName, clientPhone])

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
        if len(pets) == 1 and len(clients) == 1:
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
        message = messagebox.askyesno('Deletar', 'Desejar deletar a ligação entre os elementos? '
                                                 'Se não tiverem mais ligações, os elementos seram eliminados!',
                                      parent=self.window)

        # If the answer was yes, we can process, else, does nothing
        if message:

            # Gets our tuple of id's. If it got an error, the returned tuple is empty
            tupleOfIDs = self.getsSelectedIDS()

            # If we didn't have any errors, we can continue
            if tupleOfIDs != ():

                # Checks if our elements have any more owners/pets, if not, we eliminate them
                if not checksIfPetHasMoreThanOneOwner(tupleOfIDs[0]):
                    deleteRecordAnimal(tupleOfIDs[0])
                if not checksIfClientHasMoreThanOnePet(tupleOfIDs[1]):
                    deleteRecordClient(tupleOfIDs[1])

                # Removes values in our database
                deleteRecordPetClientLink(tupleOfIDs)

                # Refreshes all trees of our application
                self.root.refreshApplication()

                # Destroys current window
                self.destroy()

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

            # Since we need the pet id and the owner's name to query trough the database, we discard the rest
            petID = info[0]
            clientName = info[4]

            # Creates toplevel window that will display the information about this pet
            WindowPet(self, petID, clientName)

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

            # Since we need the client id and the pet's name to query trough the database, we discard the rest
            clientID = info[0]
            petName = info[3]

            # Creates toplevel window that will display the information about this client
            WindowClient(self, clientID, petName)

    @staticmethod
    def checksIfTupleOfIdsIsValid(tupleOfIds):
        """
        Description:
        > Checks if tuple is not empty (invalid).

        :param tupleOfIds: tuple of RowIds inside our database -> tuple
        :return: boolean value according to the findings -> boolean
        """
        return tupleOfIds != ()
