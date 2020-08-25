from operator import itemgetter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from database.src.functions.insertion import insertRecordAnimal, insertRecordPetClientLink
from database.src.query.databaseNotebookTabs.links import getsRequestedClients, getsClientsForLinksWindow
from database.src.utils.constants import typeOfAnimal, typeOfHair
from interface.databaseNotebookTabs import pets


class WindowInsertPet(Toplevel):
    """
    Toplevel window used to create a new pet.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Inserir novo animal')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates variable so that it can be used as control
        self.master = master

        # Creates two labelFrames to organize our UI
        self.petWindow = LabelFrame(self.window, text=' Animais ', height=500, width=500)
        self.clientWindow = LabelFrame(self.window, text=' Relacionar com o cliente ', height=400, width=500)
        self.petWindow.pack(side=LEFT, fill="both", expand=True)
        self.clientWindow.pack(side=TOP, fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)

        # Creates a submit button
        self.submit = Button(self.window, text='Submter', command=self.submit)
        self.submit.pack(side=BOTTOM, padx=5, pady=5, expand=True, fill="both")

        # Creates animals field description labels
        self.descPetName = Label(self.petWindow, text='Nome:')
        self.descPetName.grid(column=0, row=0, padx=(5, 5), pady=10, sticky=W)
        self.descPetType = Label(self.petWindow, text='Tipo:')
        self.descPetType.grid(column=0, row=2, padx=(5, 5), pady=10, sticky=W)
        self.descPetWeight = Label(self.petWindow, text='Peso:')
        self.descPetWeight.grid(column=0, row=4, padx=(5, 5), pady=10, sticky=W)
        self.descPetHair = Label(self.petWindow, text='Pelo:')
        self.descPetHair.grid(column=0, row=6, padx=(5, 5), pady=10, sticky=W)
        self.descPetBirthDate = Label(self.petWindow, text='Aniversário:')
        self.descPetBirthDate.grid(column=0, row=8, padx=(5, 5), pady=10, sticky=W)
        self.descPetObservations = Label(self.petWindow, text='Observações:')
        self.descPetObservations.grid(column=0, row=10, padx=(5, 5), pady=10, sticky=W)

        # Creates entry variables
        petName = StringVar()
        petType = StringVar()
        petWeight = StringVar()
        petHair = StringVar()
        petBirth = StringVar()
        clientName = StringVar()

        # Restriction commands
        validateString = (master.register(self.validateString), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates entry fields
        self.entryPetName = Entry(self.petWindow, textvariable=petName, validate="focusout",
                                  validatecommand=validateString, invalidcommand=self.entryError)
        self.entryPetName.grid(column=1, row=0, padx=(5, 5), pady=10, sticky=W)
        self.entryPetType = Combobox(self.petWindow, textvariable=petType, state="readonly", values=typeOfAnimal)
        self.entryPetType.grid(column=1, row=2, padx=(5, 5), pady=10, sticky=W)
        self.entryPetWeight = Entry(self.petWindow, textvariable=petWeight, validate="focusout",
                                    validatecommand=validateNumber, invalidcommand=self.entryError)
        self.entryPetWeight.grid(column=1, row=4, padx=(5, 5), pady=10, sticky=W)
        self.entryPetHair = Combobox(self.petWindow, textvariable=petHair, state="readonly", values=typeOfHair)
        self.entryPetHair.grid(column=1, row=6, padx=(5, 5), pady=10, sticky=W)
        self.entryPetBirth = Entry(self.petWindow, textvariable=petBirth)
        self.entryPetBirth.grid(column=1, row=8, padx=(5, 5), pady=10, sticky=W)
        self.entryPetObs = Text(self.petWindow, width=48, height=10)
        self.entryPetObs.grid(column=0, row=11, padx=(5, 5), pady=0, sticky=W, columnspan=2)

        # Creates separators to better organize our UI
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E), columnspan=2)

        # Creates search entry for clients
        self.labelClientName = Label(self.clientWindow, text='Nome:')
        self.labelClientName.grid(column=0, row=0, padx=(5, 0), pady=(20, 10), sticky=W)
        self.entryClientName = Entry(self.clientWindow, textvariable=clientName, width=20)
        self.entryClientName.grid(column=1, row=0, pady=(20, 10), sticky=W)

        # Creates search buttons for the clients tree
        self.clientsButton = Button(self.clientWindow, text='Procurar', width=20, command=self.updateClientTree)
        self.clientsButton.grid(column=2, row=0, pady=(20, 10), sticky=E)

        # Creates tree that will display all the links
        self.treeClients = Treeview(self.clientWindow, columns=(0, 1), height=15)
        self.treeClients.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

        # Formats columns
        self.treeClients.column("#0", stretch=NO, anchor='center', width=0)
        self.treeClients.column(0, stretch=NO, anchor='center', width=0)
        self.treeClients.column(1, stretch=NO, anchor='center', width=450)

        # Define columns heading
        self.treeClients.heading('#0', text='', anchor='w')
        self.treeClients.heading(0, text='', anchor='w')
        self.treeClients.heading(1, text='Nome', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarClients = Scrollbar(self.clientWindow, orient="vertical", command=self.treeClients.yview)
        self.scrollbarClients.grid(column=3, row=1, sticky=(N, S))
        self.treeClients.configure(yscrollcommand=self.scrollbarClients.set)

        # Populates tree
        self.refreshTreeClients()

    def submit(self):
        """
        Description:
        > Inserts an animal in the database. Gets required info and checks if we want to link it to an owner.
        """

        # Gets tuple with the selected owner
        owner = self.treeClients.selection()

        # If no owner was selected, we ask if the user still wants to submit
        if owner == ():

            # Gets confirmation from user
            msg = messagebox.askyesno('Confirmar submissão', 'Deseja inserir o animal sem dono?', parent=self.window)

            # Checks the answer from the user. If answer was 'no', we stop execution
            if msg:

                # Gets pet info. Can be empty if it has an error
                petInfo = self.getsPetEntries()

                # If everything is alright
                if petInfo != ():

                    # Inserts values inside our database
                    insertRecordAnimal(petInfo)

                    # Refreshes main tree
                    pets.Pets.refreshTree(self.master)

                    # Eliminates window
                    self.destroy()

        else:

            # Gets confirmation from user
            msg = messagebox.askyesno('Confirmar submissão?', 'Deseja submeter os dados inseridos?', parent=self.window)

            # Checks the answer from the user. If answer was 'no', we stop execution
            if msg:

                # Gets pet info. Can be empty if it has an error
                petInfo = self.getsPetEntries()

                # If everything is alright
                if petInfo != ():

                    # Inserts values inside our database. Also gets rowid of the animal
                    animalID = insertRecordAnimal(petInfo)

                    # Gets owner's id
                    ownerId = self.treeClients.item(owner[0], "values")[0]

                    # Creates a link between the client and the pet
                    insertRecordPetClientLink((animalID, ownerId))

                    # Refreshes main tree
                    pets.Pets.refreshTree(self.master)

                    # Eliminates window
                    self.destroy()

    def getsPetEntries(self):
        """
        Description:
        > Gets values inside each entry to create our pet. Also checks if required values were inserted.

        :return: tuple containing all the inserted info -> tuple of strings
        """

        # Gets entries
        petName = self.entryPetName.get()
        petType = self.entryPetType.get()
        petWeight = self.entryPetWeight.get()
        petHair = self.entryPetHair.get()
        petBirth = self.entryPetBirth.get()
        petObs = self.entryPetObs.get('1.0', 'end')

        # Checks if required values were inserted and returns them if so
        if self.checkRequiredValues((petName, petType, petWeight, petHair)):
            return petName, petType, eval(petWeight), petHair, petBirth, petObs
        else:
            return ()

    def getsClientEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryClientName.get()]

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

    def checkRequiredValues(self, info):
        """
        Description:
        > Checks if all of the required values were inserted. If not, pops an error and stops creation process.

        :param info: tuple containing all the inserted info -> tuple of strings
        :return: boolean value
        """
        if info[0] != '' and info[1] != '' and info[2] != '' and info[3] != '':
            return True
        else:
            messagebox.showerror('Erro nas entradas',
                                 'Não digitou toda a informação necessária para criar uma entrada!', parent=self.window)
            return False

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
