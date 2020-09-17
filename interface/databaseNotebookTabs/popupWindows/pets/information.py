from tkinter import *
from tkinter.ttk import *

from database.src.query.databaseNotebookTabs.pets import getsInfoForPetWindow


class WindowPet(Toplevel):
    """
    Toplevel window used to show information about this pet.
    """

    def __init__(self, master, animalID):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param animalID: animal rowid inside the database -> integer
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Informações sobre este animal')
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates 2 small rootNotebookTabs for each part of the description. Used to organize the information
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=500, width=500)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=500, width=500)
        self.petWindow.pack(side=LEFT, fill='both', expand=True)
        self.clientWindow.pack(side=LEFT, fill='both', expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)

        # Gets a list containing the information that is going to be displayed
        self.information = getsInfoForPetWindow(animalID)

        # Gets and filters information about the pet and owner from the information list
        [petName, petType, petBreed, petGender, petWeight, petHairType,
         petHairColor, petAge, petObs] = self.getsPetInfo()
        [clientName, clientNIF, clientPhone, clientEmail, clientAdr] = self.getsClientInfo()

        # Creates labels that will describe each field in each section and puts the requested information after it
        descPetName = Label(self.petWindow, text=f'Nome:  {petName}', width=100)
        descPetName.grid(column=0, row=0, sticky=W, pady=15)
        descPetType = Label(self.petWindow, text=f'Tipo:  {petType}')
        descPetType.grid(column=0, row=2, sticky=W, pady=15)
        descPetBreed = Label(self.petWindow, text=f'Raça:  {petBreed}')
        descPetBreed.grid(column=0, row=4, sticky=W, pady=15)
        descPetGender = Label(self.petWindow, text=f'Sexo:  {petGender}')
        descPetGender.grid(column=0, row=6, sticky=W, pady=15)
        descPetWeight = Label(self.petWindow, text=f'Peso:  {petWeight}Kg')
        descPetWeight.grid(column=0, row=8, sticky=W, pady=15)
        descPetHair = Label(self.petWindow, text=f'Tipo de pelo:  {petHairType}')
        descPetHair.grid(column=0, row=10, sticky=W, pady=15)
        descPetName = Label(self.petWindow, text=f'Cor do pelo:  {petHairColor}')
        descPetName.grid(column=0, row=12, sticky=W, pady=15)
        descPetBirthDate = Label(self.petWindow, text=f'Aniversário:  {petAge}')
        descPetBirthDate.grid(column=0, row=14, sticky=W, pady=15)
        descPetObs = Label(self.petWindow, text=f'Observações: ')
        descPetObs.grid(column=0, row=16, sticky=W, pady=20)
        textPetObs = Label(self.petWindow, text=f'{petObs}', justify=LEFT, wraplength=500)
        textPetObs.grid(column=0, row=17, sticky=W)

        descClientName = Label(self.clientWindow, text=f'Nome:  {clientName}', width=100)
        descClientName.grid(column=0, row=0, sticky=W, pady=15)
        descClientNIF = Label(self.clientWindow, text=f'NIF:  {clientNIF}')
        descClientNIF.grid(column=0, row=2, sticky=W, pady=15)
        descClientPhone = Label(self.clientWindow, text=f'Telemóvel:  {clientPhone}')
        descClientPhone.grid(column=0, row=4, sticky=W, pady=15)
        descClientEmail = Label(self.clientWindow, text=f'Email:  {clientEmail}', justify=LEFT, wraplength=500)
        descClientEmail.grid(column=0, row=6, sticky=W, pady=15)
        descClientAddress = Label(self.clientWindow, text=f'Morada:  {clientAdr}', justify=LEFT, wraplength=500)
        descClientAddress.grid(column=0, row=8, sticky=W, pady=15)

        # Creates separators so that we can organize the window more efficiently
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=11, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=13, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=15, sticky=(W, E))

        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list."""
        return self.information[0][0:9]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list."""
        return self.information[0][9:14]
