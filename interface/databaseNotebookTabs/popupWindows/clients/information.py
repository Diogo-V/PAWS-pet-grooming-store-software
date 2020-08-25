from tkinter import *
from tkinter.ttk import *
from database.src.query.databaseNotebookTabs.clients import getsInfoForClientWindow


class WindowClient(Toplevel):
    """
    Toplevel window used to show information about this client.
    """

    def __init__(self, master, linkID):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param linkID: link rowid inside the database -> integer
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Informações sobre esta este animal<->cliente')
        self.geometry("1000x500")
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
        self.information = getsInfoForClientWindow(linkID)

        # Gets and filters information about the pet and owner from the information list
        [self.petName, self.petType, self.petWeight, self.petHair, self.petBirth, self.petObs] = self.getsPetInfo()
        [self.clientName, self.clientNIF, self.clientPhone, self.clientEmail, self.clientAdr] = self.getsClientInfo()

        # Formats some fields so that they don't show 'None'
        if self.petObs is None:
            self.petObs = ''
        if self.clientPhone is None:
            self.clientPhone = ''
        if self.clientNIF is None:
            self.clientNIF = ''
        if self.petWeight is None or self.petWeight is 0:
            self.petWeight = ''
        if self.petBirth is None:
            self.petBirth = ''
        if self.clientEmail is None:
            self.clientEmail = ''
        if self.clientAdr is None:
            self.clientAdr = ''

        # Creates labels that will describe each field in each section and puts the requested information after it
        descPetName = Label(self.petWindow, text=f'Nome:  {self.petName}', width=100)
        descPetName.grid(column=0, row=0, sticky=W, pady=15)
        descPetType = Label(self.petWindow, text=f'Tipo de animal:  {self.petType}')
        descPetType.grid(column=0, row=2, sticky=W, pady=15)
        descPetWeight = Label(self.petWindow, text=f'Peso:  {self.petWeight}Kg')
        descPetWeight.grid(column=0, row=4, sticky=W, pady=15)
        descPetHair = Label(self.petWindow, text=f'Tipo de pelo:  {self.petHair}')
        descPetHair.grid(column=0, row=6, sticky=W, pady=15)
        descPetBirthDate = Label(self.petWindow, text=f'Aniversário:  {self.petBirth}')
        descPetBirthDate.grid(column=0, row=8, sticky=W, pady=15)
        descPetObs = Label(self.petWindow, text=f'Observações: ')
        descPetObs.grid(column=0, row=10, sticky=W, pady=20)
        textPetObs = Label(self.petWindow, text=f'{self.petObs}', justify=LEFT, wraplength=500)
        textPetObs.grid(column=0, row=11, sticky=W)

        descClientName = Label(self.clientWindow, text=f'Nome:  {self.clientName}', width=100)
        descClientName.grid(column=0, row=0, sticky=W, pady=15)
        descClientNIF = Label(self.clientWindow, text=f'NIF:  {self.clientNIF}')
        descClientNIF.grid(column=0, row=2, sticky=W, pady=15)
        descClientPhone = Label(self.clientWindow, text=f'Telemóvel:  {self.clientPhone}')
        descClientPhone.grid(column=0, row=4, sticky=W, pady=15)
        descClientEmail = Label(self.clientWindow, text=f'Email:  {self.clientEmail}', justify=LEFT, wraplength=500)
        descClientEmail.grid(column=0, row=6, sticky=W, pady=15)
        descClientAddress = Label(self.clientWindow, text=f'Morada:  {self.clientAdr}', justify=LEFT, wraplength=500)
        descClientAddress.grid(column=0, row=8, sticky=W, pady=15)

        # Creates separators so that we can organize the window more efficiently
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E))

        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list."""
        return self.information[0][0:6]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list."""
        return self.information[0][6:11]
