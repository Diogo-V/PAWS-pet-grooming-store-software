from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordAnimal
from database.src.functions.insertion import insertRecordAnimal, insertRecordPetClientLink, insertRecordClient
from database.src.utils.constants import typeOfAnimal, typeOfHair


class WindowInsertMix(Toplevel):
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
        self.title('Inserir animal + cliente')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates variable so that it can be used as control
        self.master = master

        # Creates two labelFrames to organize our UI
        self.petWindow = LabelFrame(self.window, text=' Animal ', height=500, width=500)
        self.clientWindow = LabelFrame(self.window, text=' Cliente ', height=400, width=500)
        self.petWindow.pack(side=LEFT, fill="both", expand=True)
        self.clientWindow.pack(side=TOP, fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)

        # Creates a submit button
        self.submitButton = Button(self.window, text='Submter', command=self.submit)
        self.submitButton.pack(side=BOTTOM, padx=5, pady=5, expand=True, fill="both")

        # Restriction commands
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateString = (master.register(self.validateString), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates animals field description labels
        descPetName = Label(self.petWindow, text='Nome:')
        descPetName.grid(column=0, row=0, padx=(5, 5), pady=10, sticky=W)
        descPetType = Label(self.petWindow, text='Tipo:')
        descPetType.grid(column=0, row=2, padx=(5, 5), pady=10, sticky=W)
        descPetWeight = Label(self.petWindow, text='Peso:')
        descPetWeight.grid(column=0, row=4, padx=(5, 5), pady=10, sticky=W)
        descPetHair = Label(self.petWindow, text='Pelo:')
        descPetHair.grid(column=0, row=6, padx=(5, 5), pady=10, sticky=W)
        descPetBirthDate = Label(self.petWindow, text='Aniversário:')
        descPetBirthDate.grid(column=0, row=8, padx=(5, 5), pady=10, sticky=W)
        descPetObservations = Label(self.petWindow, text='Observações:')
        descPetObservations.grid(column=0, row=10, padx=(5, 5), pady=10, sticky=W)

        # Creates entry variables
        petName = StringVar()
        petType = StringVar()
        petWeight = StringVar()
        petHair = StringVar()
        petBirth = StringVar()

        # Creates entry fields
        self.entryPetName = Entry(self.petWindow, textvariable=petName)
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
        self.entryPetObs = Text(self.petWindow, width=60, height=10)
        self.entryPetObs.grid(column=0, row=11, padx=(5, 5), pady=0, sticky=W, columnspan=2)

        # Creates separators to better organize our UI
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E), columnspan=2)

        # Creates animals field description labels
        descClientName = Label(self.clientWindow, text='Nome:')
        descClientName.grid(column=0, row=0, padx=(5, 5), pady=30, sticky=W)
        descClientEmail = Label(self.clientWindow, text='Email:')
        descClientEmail.grid(column=0, row=2, padx=(5, 5), pady=30, sticky=W)
        descClientPhone = Label(self.clientWindow, text='Telemóvel:')
        descClientPhone.grid(column=0, row=4, padx=(5, 5), pady=30, sticky=W)
        descClientNIF = Label(self.clientWindow, text='NIF:')
        descClientNIF.grid(column=0, row=6, padx=(5, 5), pady=30, sticky=W)
        descClientAddress = Label(self.clientWindow, text='Morada:')
        descClientAddress.grid(column=0, row=8, padx=(5, 5), pady=30, sticky=W)

        # Creates entry variables
        clientName = StringVar()
        clientEmail = StringVar()
        clientPhone = StringVar()
        clientNIF = StringVar()
        clientAddress = StringVar()

        # Creates entry fields
        self.entryClientName = Entry(self.clientWindow, textvariable=clientName, validate="focusout", width=35,
                                      validatecommand=validateString, invalidcommand=self.entryError)
        self.entryClientName.grid(column=1, row=0, padx=(5, 500), pady=10, sticky=W)
        self.entryClientEmail = Entry(self.clientWindow, textvariable=clientEmail, width=35)
        self.entryClientEmail.grid(column=1, row=2, padx=(5, 5), pady=10, sticky=W)
        self.entryClientPhone = Entry(self.clientWindow, textvariable=clientPhone, validate="focusout", width=35,
                                      validatecommand=validateNumber, invalidcommand=self.entryError)
        self.entryClientPhone.grid(column=1, row=4, padx=(5, 5), pady=10, sticky=W)
        self.entryClientNIF = Entry(self.clientWindow, textvariable=clientNIF, validate="focusout", width=35,
                                    validatecommand=validateNumber, invalidcommand=self.entryError)
        self.entryClientNIF.grid(column=1, row=6, padx=(5, 5), pady=10, sticky=W)
        self.entryClientAddress = Entry(self.clientWindow, textvariable=clientAddress, width=35)
        self.entryClientAddress.grid(column=1, row=8, padx=(5, 5), pady=10, sticky=W)

        # Creates separators to better organize our UI
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)

    def submit(self):
        """
        Description:
        > Gets the inserted info and creates a pet, a client and a link between them in our database.
        """

        # Gets all the info about the pet and the client
        pet = self.getsPetEntries()
        client = self.getsClientEntries()

        # Validates if everything is alright. If not, interrupts
        if pet == ():
            messagebox.showerror("Erro", "Falha ao criar o animal! Reveja a informação digitada e tente de novo!",
                                 parent=self.window)
            return

        # Validates if everything is alright. If not, interrupts
        if client == ():
            messagebox.showerror("Erro", "Falha ao criar o cliente! Reveja a informação digitada e tente de novo!",
                                 parent=self.window)

        # Prompts the user and asks for his confirmation
        msg = messagebox.askyesno("Confirmar", "Deseja inserir este animal + cliente?", parent=self.window)
        if msg:

            # Inserts a pet and gets his rowid
            petID = insertRecordAnimal(pet)

            if petID is not None:

                # Insert client and gets his rowid
                clientID = insertRecordClient(client)

                if clientID is not None:

                    # Insert link between them
                    insertRecordPetClientLink((petID, clientID))

                    # Eliminates window
                    self.destroy()

                # Something went wrong when inserting our client so, we nee to rollback any changes and warn the user
                else:
                    deleteRecordAnimal(petID)
                    messagebox.showerror("Erro", "Ocurreu um erro e não possivel inserir o cliente!",
                                         parent=self.window)

            # Something went wrong so, we need to prompt the user about such error
            else:
                messagebox.showerror("Erro", "Ocurreu um erro e não possivel inserir o animal!", parent=self.window)

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
        if self.checkPetRequiredValues((petName, petType)):
            return petName, petType, eval(petWeight), petHair, petBirth, petObs
        else:
            return ()

    def getsClientEntries(self):
        """
        Description:
        > Gets information inserted our client entries.

        :return: tuple containing such info -> list of strings
        """

        # Gets values inside each entry
        clientName = self.entryClientName.get()
        clientEmail = self.entryClientEmail.get()
        clientPhone = self.entryClientPhone.get()
        clientNIF = self.entryClientNIF.get()
        clientAddress = self.entryClientAddress.get()

        if self.checkClientRequiredValues((clientName, clientPhone)):
            return clientName, clientEmail, clientPhone, clientNIF, clientAddress
        else:
            return ()

    def checkPetRequiredValues(self, info):
        """
        Description:
        > Checks if all of the required values were inserted. If not, pops an error and stops creation process.

        :param info: tuple containing all the inserted info -> tuple of strings
        :return: boolean value
        """
        if info[0] != '' and info[1] != '':
            return True
        else:
            messagebox.showerror('Erro nas entradas',
                                 'Não digitou toda a informação necessária para criar um animal!', parent=self.window)
            return False

    def checkClientRequiredValues(self, info):
        """
        Description:
        > Checks if all of the required values were inserted. If not, pops an error and stops creation process.

        :param info: tuple containing all the inserted info -> tuple of strings
        :return: boolean value
        """
        if info[0] != '' and info[1]:
            return True
        else:
            messagebox.showerror('Erro nas entradas',
                                 'Não digitou toda a informação necessária para criar um cliente!', parent=self.window)
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
