from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.insertion import insertRecordPetClientLink, insertRecordClient
from database.src.query.databaseNotebookTabs.links import getsPetsForLinksWindow, getsRequestedPets
from database.src.utils.constants import typeOfAnimal
from interface.databaseNotebookTabs.popupWindows.pets.information import WindowPet


class WindowInsertClient(Toplevel):
    """
    Toplevel window used to create a new client.
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
        self.title('Inserir novo cliente')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root

        # Creates two labelFrames to organize our UI
        self.clientWindow = LabelFrame(self.window, text=' Cliente ', height=500, width=625)
        self.petWindow = LabelFrame(self.window, text=' Relacionar com o animal ', height=600, width=625)
        self.clientWindow.grid(column=0, row=0, rowspan=5)
        self.petWindow.grid(column=1, row=0, rowspan=6)

        # Blocks resizing for each labelFrame
        self.clientWindow.grid_propagate(False)
        self.petWindow.grid_propagate(False)

        # Creates a submit button
        self.createClient = Button(self.window, text='Submter', command=self.submit)
        self.createClient.grid(column=0, row=5, padx=5, pady=5, sticky=(W, S, N, E))

        # Creates clients field description labels
        self.descClientName = Label(self.clientWindow, text='Nome:')
        self.descClientName.grid(column=0, row=0, padx=(5, 5), pady=10, sticky=W)
        self.descClientEmail = Label(self.clientWindow, text='Email:')
        self.descClientEmail.grid(column=0, row=2, padx=(5, 5), pady=10, sticky=W)
        self.descClientPhone = Label(self.clientWindow, text='Telemóvel:')
        self.descClientPhone.grid(column=0, row=4, padx=(5, 5), pady=10, sticky=W)
        self.descClientNIF = Label(self.clientWindow, text='NIF:')
        self.descClientNIF.grid(column=0, row=6, padx=(5, 5), pady=10, sticky=W)
        self.descClientAddress = Label(self.clientWindow, text='Morada:')
        self.descClientAddress.grid(column=0, row=8, padx=(5, 5), pady=10, sticky=W)

        # Creates entry variables
        clientName = StringVar()
        clientEmail = StringVar()
        clientPhone = StringVar()
        clientNIF = StringVar()
        clientAddress = StringVar()
        petName = StringVar()
        petType = StringVar()
        petBreed = StringVar()

        # Restriction commands
        validateString = (master.register(self.validateString), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates entry fields
        self.entryClientName = Entry(self.clientWindow, textvariable=clientName, validate="focusout",
                                     validatecommand=validateString, invalidcommand=self.entryError, width=40)
        self.entryClientName.grid(column=1, row=0, padx=(5, 500), pady=36, sticky=W)
        self.entryClientEmail = Entry(self.clientWindow, textvariable=clientEmail, width=40)
        self.entryClientEmail.grid(column=1, row=2, padx=(5, 5), pady=36, sticky=W)
        self.entryClientPhone = Entry(self.clientWindow, textvariable=clientPhone, validate="focusout",
                                      validatecommand=validateNumber, invalidcommand=self.entryError, width=40)
        self.entryClientPhone.grid(column=1, row=4, padx=(5, 5), pady=36, sticky=W)
        self.entryClientNIF = Entry(self.clientWindow, textvariable=clientNIF, validate="focusout",
                                     validatecommand=validateNumber, invalidcommand=self.entryError, width=40)
        self.entryClientNIF.grid(column=1, row=6, padx=(5, 5), pady=36, sticky=W)
        self.entryClientAddress = Entry(self.clientWindow, textvariable=clientAddress, width=40)
        self.entryClientAddress.grid(column=1, row=8, padx=(5, 5), pady=36, sticky=W)

        # Creates separators to better organize our UI
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)

        # Creates search entry for pets
        self.labelPetName = Label(self.petWindow, text='Nome:')
        self.labelPetName.grid(column=0, row=0, pady=(20, 10), sticky=W)
        self.entryPetName = Entry(self.petWindow, textvariable=petName, width=13)
        self.entryPetName.grid(column=1, row=0, pady=(20, 10), sticky=W)
        self.labelPetType = Label(self.petWindow, text='Tipo:')
        self.labelPetType.grid(column=2, row=0, pady=(20, 10), sticky=W)
        self.boxPetType = Combobox(self.petWindow, textvariable=petType, state="readonly",
                                   values=[''] + typeOfAnimal, width=10)
        self.boxPetType.grid(column=3, row=0, pady=(20, 10), sticky=W)
        self.labelPetBreed = Label(self.petWindow, text='Raça:')
        self.labelPetBreed.grid(column=4, row=0, pady=(20, 10), sticky=W)
        self.entryPetBreed = Entry(self.petWindow, textvariable=petBreed, width=13)
        self.entryPetBreed.grid(column=5, row=0, pady=(20, 10), sticky=W)

        # Creates search buttons for the pets tree
        self.petButton = Button(self.petWindow, text='Procurar', width=8, command=self.updatePetTree)
        self.petButton.grid(column=0, row=1, pady=(20, 10), columnspan=3, sticky=(W, E), padx=8)

        # Columns names that are going to be inserted inside the tree
        columns = ('', 'Nome', 'Tipo', 'Raça', 'Cliente')

        # Creates tree that will display all the pets
        self.treePets = Treeview(self.petWindow, columns=columns, height=21, show='headings')
        self.treePets.grid(column=0, row=2, columnspan=6, padx=10, pady=10)

        # Formats columns
        self.treePets.column("#0", stretch=NO, anchor='center', width=0)
        self.treePets.column(0, stretch=NO, anchor='center', width=0)
        self.treePets.column(1, stretch=NO, anchor='center', width=145)
        self.treePets.column(2, stretch=NO, anchor='center', width=145)
        self.treePets.column(3, stretch=NO, anchor='center', width=145)
        self.treePets.column(4, stretch=NO, anchor='center', width=145)

        # Define columns heading and sets their sorting function
        for col in columns:
            self.treePets.heading(col, text=col, command=lambda _col=col:
                                  self.treeSortColumn(self.treePets, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarClients = Scrollbar(self.petWindow, orient="vertical", command=self.treePets.yview)
        self.scrollbarClients.grid(column=7, row=2, sticky=(N, S))
        self.treePets.configure(yscrollcommand=self.scrollbarClients.set)

        # Populates tree
        self.refreshTreePets()

        # Links double click on a row with a window popup
        self.treePets.bind('<Double 1>', self.displayClientWindow)

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

    def submit(self):
        """
        Description:
        > Inserts a client in the database. Gets required info and checks if we want to link it to a pet.
        """

        # Gets tuple with the selected pet
        pet = self.treePets.selection()

        # If the user selected more than one pet. Throws error and interrupts
        if len(pet) != 1:
            messagebox.showerror("Erro", "Selecione um e é só animal antes de continuar!", parent=self.window)
            return

        # Gets confirmation from user
        msg = messagebox.askyesno('Confirmar submissão?', 'Deseja submeter os dados inseridos?', parent=self.window)

        # Checks the answer from the user. If answer was 'no', we stop execution
        if msg:

            # Gets pet info. Can be empty if it has an error
            clientInfo = self.getsClientEntries()

            # If everything is alright
            if clientInfo != ():

                # Inserts values inside our database. Also gets rowid of the newly inserted client
                clientID = insertRecordClient(clientInfo)

                # Checks if insertion went well
                if clientID is not None:

                    # Gets pet's id
                    petID = self.treePets.item(pet[0], "values")[0]

                    # Creates a link between the client and the pet
                    insertRecordPetClientLink((petID, clientID))

                    # Refreshes all trees of our application
                    self.root.refreshApplication()

                    # Eliminates window
                    self.destroy()

                # Since we had an error while inserting the client, we need to prompt the user
                else:
                    messagebox.showerror("Erro", "Aconteceu um erro ao tentar inserir o cliente na base de dados. "
                                                 "Tente de novo!", parent=self.window)

            # Since we had an error while creating the client, we need to prompt the user
            else:
                messagebox.showerror("Erro", "Aconteceu um erro ao obter as informações inseridas. "
                                             "Verifique que inserio toda a informação necessária e tente de novo!",
                                     parent=self.window)

    def getsClientEntries(self):
        """
        Description:
        > Gets values inside each entry to create our pet. Also checks if required values were inserted.

        :return: tuple containing all the inserted info -> tuple of strings
        """

        # Gets entries
        clientName = self.entryClientName.get()
        clientEmail = self.entryClientEmail.get()
        clientPhone = self.entryClientPhone.get()
        clientNIF = self.entryClientNIF.get()
        clientAddress = self.entryClientAddress.get()

        clientPhone = eval(clientPhone) if clientPhone != '' else 0
        clientNIF = eval(clientNIF) if clientNIF != '' else 0

        # Checks if required values were inserted and returns them if so
        if clientName != '' and clientPhone != 0:
            return clientName, clientEmail, clientPhone, clientNIF, clientAddress
        else:
            return ()

    def getsPetEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryPetName.get(), self.boxPetType.get(), self.entryPetBreed.get()]

    def updatePetTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for clients
        [petName, petType, petBreed] = self.getsPetEntries()

        # If no information was typed, just refresh the page
        if petName == '' and petType == '' and petBreed == '':
            self.refreshTreePets()
        else:

            # Gets requested rows
            rows = getsRequestedPets([petName, petType, petBreed])

            # Displays information on our tree
            self.displayTreePetsRows(rows)

    def refreshTreePets(self):
        """
        Description:
        > Gets all the default values for the corresponding tree.
        """

        # Gets default values for pets
        rows = getsPetsForLinksWindow()

        # Displays rows
        self.displayTreePetsRows(rows)

    def displayTreePetsRows(self, rows):
        """
        Description:
        > Sorts rows according to pets's name and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.treePets.delete(*self.treePets.get_children())

        # Sorts rows according to pet's name
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.treePets.insert('', 'end', values=row)

    def displayClientWindow(self, event):
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
            clientName = info[4]

            # Creates toplevel window that will display the information about this pet
            WindowPet(self, petID, clientName)

    @staticmethod
    def validateString(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                float(valueIfAllowed)
                return False
            except ValueError:
                return True
        else:
            return True

    @staticmethod
    def validateNumber(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                float(valueIfAllowed)
                return True
            except ValueError:
                return False
        else:
            return True

    def entryError(self):
        messagebox.showerror('Erro nas entradas', 'Os valores inseridos não são validos!', parent=self.window)
