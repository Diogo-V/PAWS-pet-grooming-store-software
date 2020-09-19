from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordAnimal
from database.src.functions.insertion import insertRecordAnimal, insertRecordPetClientLink, insertRecordClient
from database.src.utils.constants import *


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
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates two labelFrames to organize our UI
        self.petWindow = LabelFrame(self.window, text=' Animal ', height=600, width=625)
        self.clientWindow = LabelFrame(self.window, text=' Cliente ', height=500, width=625)
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
        descPetBreed = Label(self.petWindow, text='Raça:')
        descPetBreed.grid(column=0, row=4, padx=(5, 5), pady=10, sticky=W)
        descPetGender = Label(self.petWindow, text='Sexo:')
        descPetGender.grid(column=0, row=6, padx=(5, 5), pady=10, sticky=W)
        descPetWeight = Label(self.petWindow, text='Peso:')
        descPetWeight.grid(column=0, row=8, padx=(5, 5), pady=10, sticky=W)
        descPetHairType = Label(self.petWindow, text='Tipo de pelo:')
        descPetHairType.grid(column=0, row=10, padx=(5, 5), pady=10, sticky=W)
        descPetHairColor = Label(self.petWindow, text='Cor do pelo:')
        descPetHairColor.grid(column=0, row=12, padx=(5, 5), pady=10, sticky=W)
        descPetAge = Label(self.petWindow, text='Idade:')
        descPetAge.grid(column=0, row=14, padx=(5, 5), pady=10, sticky=W)
        descPetObservations = Label(self.petWindow, text='Observações:')
        descPetObservations.grid(column=0, row=16, padx=(5, 5), pady=10, sticky=W)

        # Creates entry variables
        petName = StringVar()
        petType = StringVar()
        petBreed = StringVar()
        petGender = StringVar()
        petWeight = StringVar()
        petHairType = StringVar()
        petHairColor = StringVar()
        petAge = StringVar()

        # Creates entry fields
        self.entryPetName = Entry(self.petWindow, textvariable=petName, width=25)
        self.entryPetName.grid(column=1, row=0, padx=(5, 5), pady=10, sticky=W)
        self.entryPetType = Combobox(self.petWindow, textvariable=petType, state="readonly",
                                     values=typeOfAnimal, width=24)
        self.entryPetType.grid(column=1, row=2, padx=(5, 5), pady=10, sticky=W)
        self.entryPetBreed = Entry(self.petWindow, textvariable=petBreed, width=25)
        self.entryPetBreed.grid(column=1, row=4, padx=(5, 5), pady=10, sticky=W)
        self.entryPetGender = Combobox(self.petWindow, textvariable=petGender, state="readonly",
                                       values=gender, width=24)
        self.entryPetGender.grid(column=1, row=6, padx=(5, 5), pady=10, sticky=W)
        self.entryPetWeight = Entry(self.petWindow, textvariable=petWeight, validate="focusout",
                                    validatecommand=validateNumber, invalidcommand=self.entryError, width=25)
        self.entryPetWeight.grid(column=1, row=8, padx=(5, 5), pady=10, sticky=W)
        self.entryPetHairType = Combobox(self.petWindow, textvariable=petHairType, state="readonly",
                                         values=typeOfHair, width=24)
        self.entryPetHairType.grid(column=1, row=10, padx=(5, 5), pady=10, sticky=W)
        self.entryPetHairColor = Entry(self.petWindow, textvariable=petHairColor, width=25)
        self.entryPetHairColor.grid(column=1, row=12, padx=(5, 5), pady=10, sticky=W)
        self.entryPetAge = Entry(self.petWindow, textvariable=petAge, width=25)
        self.entryPetAge.grid(column=1, row=14, padx=(5, 5), pady=10, sticky=W)
        self.entryPetObs = Text(self.petWindow, width=75, height=10)
        self.entryPetObs.grid(column=0, row=17, padx=(5, 30), pady=0, sticky=W, columnspan=6)

        # Creates separators to better organize our UI
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=11, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=13, sticky=(W, E), columnspan=6)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=15, sticky=(W, E), columnspan=6)

        # Creates animals field description labels
        descClientName = Label(self.clientWindow, text='Nome:')
        descClientName.grid(column=0, row=0, padx=(5, 5), pady=40, sticky=W)
        descClientEmail = Label(self.clientWindow, text='Email:')
        descClientEmail.grid(column=0, row=2, padx=(5, 5), pady=40, sticky=W)
        descClientPhone = Label(self.clientWindow, text='Telemóvel:')
        descClientPhone.grid(column=0, row=4, padx=(5, 5), pady=40, sticky=W)
        descClientNIF = Label(self.clientWindow, text='NIF:')
        descClientNIF.grid(column=0, row=6, padx=(5, 5), pady=40, sticky=W)
        descClientAddress = Label(self.clientWindow, text='Morada:')
        descClientAddress.grid(column=0, row=8, padx=(5, 5), pady=40, sticky=W)

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
            messagebox.showerror("Erro", "Falha ao criar o animal! Reveja se inseriu toda a informação necessária e se "
                                         "está correta depois, tente de novo!", parent=self.window)
            return

        # Validates if everything is alright. If not, interrupts
        if client == ():
            messagebox.showerror("Erro", "Falha ao criar o cliente! Reveja se inseriu toda a informação necessária e se "
                                         "está correta depois, tente de novo!", parent=self.window)

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
                    messagebox.showerror("Erro", "Ocurreu um erro e não foi possivel inserir o cliente!",
                                         parent=self.window)

            # Something went wrong so, we need to prompt the user about such error
            else:
                messagebox.showerror("Erro", "Ocurreu um erro e não foi possivel inserir o animal!", parent=self.window)

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

        # Formats values
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
        > Gets information inserted our client entries.

        :return: tuple containing such info -> list of strings
        """

        # Gets values inside each entry
        clientName = self.entryClientName.get()
        clientEmail = self.entryClientEmail.get()
        clientPhone = self.entryClientPhone.get()
        clientNIF = self.entryClientNIF.get()
        clientAddress = self.entryClientAddress.get()

        # Formats values
        clientPhone = eval(clientPhone) if clientPhone != '' else 0
        clientNIF = eval(clientNIF) if clientNIF != '' else 0

        # Checks if required values were inserted and returns them if so
        if clientName != '' or clientPhone != '':
            return clientName, clientEmail, clientPhone, clientNIF, clientAddress
        else:
            return ()

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
