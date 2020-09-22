from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.insertion import insertRecordAnimal, insertRecordPetClientLink
from database.src.query.databaseNotebookTabs.links import getsRequestedClients, getsClientsForLinksWindow
from database.src.utils.constants import *
from interface.databaseNotebookTabs.popupWindows.clients.information import WindowClient


class WindowInsertPet(Toplevel):
    """
    Toplevel window used to create a new pet.
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
        self.title('Inserir novo animal')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root
        self.master = master

        # Creates two labelFrames to organize our UI
        self.petWindow = LabelFrame(self.window, text=' Animais ', height=750, width=600)
        self.clientWindow = LabelFrame(self.window, text=' Relacionar com o cliente ', height=500, width=600)
        self.petWindow.pack(side=LEFT, fill="both", expand=True)
        self.clientWindow.pack(side=TOP, fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)

        # Creates a submit button
        self.submit = Button(self.window, text='Submter', command=self.submit)
        self.submit.pack(side=BOTTOM, padx=5, pady=5, expand=True, fill="both")

        # Creates animals field description labels
        descPetName = Label(self.petWindow, text='Nome:')
        descPetName.grid(column=0, row=0, padx=(5, 5), pady=10, sticky=W)
        descPetType = Label(self.petWindow, text='Tipo:')
        descPetType.grid(column=0, row=2, padx=(5, 5), pady=10, sticky=W)
        descPetBreed = Label(self.petWindow, text='Raça:')
        descPetBreed.grid(column=0, row=4, padx=(5, 5), pady=10, sticky=W)
        descPetGender = Label(self.petWindow, text='Sexo:')
        descPetGender.grid(column=0, row=6, padx=(5, 5), pady=10, sticky=W)
        descPetWeight = Label(self.petWindow, text='Peso:')
        descPetWeight.grid(column=0, row=8, padx=(5, 5), pady=10, sticky=W)
        descPetHairType = Label(self.petWindow, text='Pelo:')
        descPetHairType.grid(column=0, row=10, padx=(5, 5), pady=10, sticky=W)
        descPetHairColor = Label(self.petWindow, text='Cor:')
        descPetHairColor.grid(column=0, row=12, padx=(5, 5), pady=10, sticky=W)
        descPetAge = Label(self.petWindow, text='Idade:')
        descPetAge.grid(column=0, row=14, padx=(5, 5), pady=10, sticky=W)
        descPetObservations = Label(self.petWindow, text='Observações:')
        descPetObservations.grid(column=0, row=16, padx=(5, 5), pady=10, sticky=W)

        # Creates entry variables
        petName = StringVar()
        petBreed = StringVar()
        petGender = StringVar()
        petType = StringVar()
        petWeight = StringVar()
        petHairType = StringVar()
        petHairColor = StringVar()
        petAge = StringVar()
        clientName = StringVar()
        clientPhone = StringVar()

        # Restriction commands
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateString = (master.register(self.validateString), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates entry fields
        self.entryPetName = Entry(self.petWindow, textvariable=petName, width=30)
        self.entryPetName.grid(column=1, row=0, padx=(5, 5), pady=10, sticky=W)
        self.entryPetType = Combobox(self.petWindow, textvariable=petType, state="readonly",
                                     values=typeOfAnimal, width=28)
        self.entryPetType.grid(column=1, row=2, padx=(5, 5), pady=10, sticky=W)
        self.entryPetBreed = Entry(self.petWindow, textvariable=petBreed, validate="focusout",
                                    validatecommand=validateString, invalidcommand=self.entryError, width=30)
        self.entryPetBreed.grid(column=1, row=4, padx=(5, 5), pady=10, sticky=W)
        self.entryPetGender = Combobox(self.petWindow, textvariable=petGender, state="readonly",
                                       values=gender, width=28)
        self.entryPetGender.grid(column=1, row=6, padx=(5, 5), pady=10, sticky=W)
        self.entryPetWeight = Entry(self.petWindow, textvariable=petWeight, validate="focusout",
                                    validatecommand=validateNumber, invalidcommand=self.entryError, width=30)
        self.entryPetWeight.grid(column=1, row=8, padx=(5, 5), pady=10, sticky=W)
        self.entryPetHairType = Combobox(self.petWindow, textvariable=petHairType, state="readonly",
                                         values=typeOfHair, width=28)
        self.entryPetHairType.grid(column=1, row=10, padx=(5, 5), pady=10, sticky=W)
        self.entryPetHairColor = Entry(self.petWindow, textvariable=petHairColor, validate="focusout",
                                       validatecommand=validateString, invalidcommand=self.entryError, width=30)
        self.entryPetHairColor.grid(column=1, row=12, padx=(5, 5), pady=10, sticky=W)
        self.entryPetAge = Entry(self.petWindow, textvariable=petAge, validate="focusout",
                                 validatecommand=validateNumber, invalidcommand=self.entryError, width=30)
        self.entryPetAge.grid(column=1, row=14, padx=(5, 5), pady=10, sticky=W)
        self.entryPetObs = Text(self.petWindow, width=78, height=10)
        self.entryPetObs.grid(column=0, row=17, padx=(5, 20), pady=0, sticky=W, columnspan=6)

        # Creates separators to better organize our UI
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=11, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=13, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=15, sticky=(W, E), columnspan=6)

        # Creates search entry for clients
        self.labelClientName = Label(self.clientWindow, text='Nome:')
        self.labelClientName.grid(column=0, row=0, padx=(5, 0), pady=(20, 10), sticky=W)
        self.entryClientName = Entry(self.clientWindow, textvariable=clientName, width=20)
        self.entryClientName.grid(column=1, row=0, pady=(20, 10), sticky=W)
        self.labelClientPhone = Label(self.clientWindow, text='Telemóvel:')
        self.labelClientPhone.grid(column=0, row=1, padx=(5, 0), pady=(0, 10), sticky=W)
        self.entryClientPhone = Entry(self.clientWindow, textvariable=clientPhone, width=20)
        self.entryClientPhone.grid(column=1, row=1, pady=(0, 10), sticky=W)

        # Creates search buttons for the clients tree
        self.clientsButton = Button(self.clientWindow, text='Procurar', width=20, command=self.updateClientTree)
        self.clientsButton.grid(column=2, row=0, pady=(20, 10), rowspan=2)

        # Columns names that are going to be inserted inside the tree
        columns = ('', 'Nome', 'Telemóvel', 'Animal')

        # Creates tree that will display all the clients
        self.treeClients = Treeview(self.clientWindow, columns=columns, height=19, show='headings')
        self.treeClients.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

        # Formats columns
        self.treeClients.column("#0", stretch=NO, anchor='center', width=0)
        self.treeClients.column(0, stretch=NO, anchor='center', width=0)
        self.treeClients.column(1, stretch=NO, anchor='center', width=185)
        self.treeClients.column(2, stretch=NO, anchor='center', width=185)
        self.treeClients.column(3, stretch=NO, anchor='center', width=185)

        # Define columns heading and sets their sorting function
        for col in columns:
            self.treeClients.heading(col, text=col, command=lambda _col=col:
                                     self.treeSortColumn(self.treeClients, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarClients = Scrollbar(self.clientWindow, orient="vertical", command=self.treeClients.yview)
        self.scrollbarClients.grid(column=3, row=2, sticky=(N, S))
        self.treeClients.configure(yscrollcommand=self.scrollbarClients.set)

        # Populates tree
        self.refreshTreeClients()

        # Links double click on a row with a window popup
        self.treeClients.bind('<Double 1>', self.displayPetWindow)

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
        > Inserts an animal in the database. Gets required info and links it to an owner.
        """

        # Gets tuple with the selected owner
        owner = self.treeClients.selection()

        # Checks if the user selected an owner and if it was only one. If not, prompts the user and interrupts execution
        if len(owner) != 1:
            messagebox.showerror("Erro", "Selecione um e um só cliente antes de continuar!", parent=self.window)
            return

        # Gets confirmation from user
        msg = messagebox.askyesno('Confirmar submissão?', 'Deseja submeter os dados inseridos?', parent=self.window)

        # If user agreed, continues
        if msg:

            # Gets pet info. Can be empty if it has an error
            petInfo = self.getsPetEntries()

            # If everything is alright
            if petInfo != ():

                # Inserts values inside our database. Also gets rowid of the animal
                animalID = insertRecordAnimal(petInfo)

                # Checks if insertion went well
                if animalID is not None:
                    # Gets owner's id
                    ownerId = self.treeClients.item(owner[0], "values")[0]

                    # Creates a link between the client and the pet
                    insertRecordPetClientLink((animalID, ownerId))

                    # Refreshes all trees of our application
                    self.root.refreshApplication()

                    # Eliminates window
                    self.destroy()

                # Since an error occurred, we need to warn the user
                else:
                    messagebox.showerror("Erro", "Aconteceu um erro ao inserir o animal na base de dados! "
                                                 "Tente de novo", parent=self.window)
            # Since an error occurred, we need to warn the user
            else:
                messagebox.showerror("Erro", "Aconteceu com as entradas digitadas do animal! "
                                             "Reveja se inserio todas as informações necessárias e tente de novo.",
                                     parent=self.window)

    def getsPetEntries(self):
        """
        Description:
        > Gets values inside each entry to create our pet. Also checks if required values were inserted.

        :return: tuple containing all the inserted info -> tuple of strings
        """

        # Gets entries
        petName = self.entryPetName.get()
        petType = self.entryPetType.get()
        petBreed = self.entryPetBreed.get()
        petGender = self.entryPetGender.get()
        petWeight = self.entryPetWeight.get()
        petHairType = self.entryPetHairType.get()
        petHairColor = self.entryPetHairColor.get()
        petAge = self.entryPetAge.get()
        petObs = self.entryPetObs.get('1.0', 'end')

        petWeight = eval(petWeight) if petWeight != '' else 0
        petAge = eval(petAge) if petAge != '' else 0

        # Checks if required values were inserted and returns them if so
        if petName != '' or petType != '':
            return petName, petType, petBreed, petGender, petWeight, petHairType, petHairColor, petAge, petObs
        else:
            return ()

    def getsClientEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryClientName.get(), self.entryClientPhone.get()]

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

    def refreshTreeClients(self):
        """
        Description:
        > Gets all the default values for the corresponding tree.
        """

        # Gets default values for clients
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

    def displayPetWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected pet.

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
            petName = info[3]

            # Creates toplevel window that will display the information about this client
            WindowClient(self, clientID, petName)

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
