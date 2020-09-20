from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordAppointment
from database.src.functions.insertion import insertRecordHistory
from database.src.query.rootNotebookTabs.appointments import getsInfoForAppointmentsWindow
from interface.rootNotebookTabs.popupWindows.appointments.update import WindowUpdateAppointment


class WindowAppointment(Toplevel):
    """
    Toplevel window that holds all the information about a specific appointment.
    """

    def __init__(self, master, appointmentID, root):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param appointmentID: appointment rowid inside the database -> integer
        :param root: Main application frame window -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Informações sobre a marcação')
        self.geometry("1250x600")
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root
        self.master = master
        self.appointmentID = appointmentID

        # Creates 3 small LabelFrame for each part of the description. Used to organize the information
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=600, width=416)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=600, width=416)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=600, width=417)
        self.petWindow.pack(side=LEFT, fill='both', expand=True)
        self.clientWindow.pack(side=LEFT, fill='both', expand=True)
        self.appointmentWindow.pack(side=LEFT, fill='both', expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)
        self.appointmentWindow.grid_propagate(False)

        # Gets a list containing the information that is going to be displayed
        self.information = getsInfoForAppointmentsWindow(appointmentID)

        # Gets and filters information about the pet, owner and appointment from the information list
        [self.petID, self.petName, self.petType, self.petBreed, self.petGender, self.petWeight, self.petHairType,
         self.petHairColor, self.petAge, self.petObs] = self.getsPetInfo()
        [self.clientID, self.clientName, self.clientEmail,
         self.clientPhone, self.clientNIF, self.clientAdr] = self.getsClientInfo()
        [self.appServices, self.appDate, self.appTime, self.appPrice, self.appObs] = self.getsAppointmentInfo()

        # Creates labels that will describe each field in each section and puts the requested information after it
        descPetName = Label(self.petWindow, text=f'Nome:  {self.petName}', width=100)
        descPetName.grid(column=0, row=0, sticky=W, pady=15)
        descPetType = Label(self.petWindow, text=f'Tipo:  {self.petType}')
        descPetType.grid(column=0, row=2, sticky=W, pady=15)
        descPetBreed = Label(self.petWindow, text=f'Raça:  {self.petBreed}', width=100)
        descPetBreed.grid(column=0, row=4, sticky=W, pady=15)
        descPetGender = Label(self.petWindow, text=f'Sexo:  {self.petGender}', width=100)
        descPetGender.grid(column=0, row=6, sticky=W, pady=15)
        descPetWeight = Label(self.petWindow, text=f'Peso:  {self.petWeight} Kg')
        descPetWeight.grid(column=0, row=8, sticky=W, pady=15)
        descPetHairType = Label(self.petWindow, text=f'Pelo:  {self.petHairType}')
        descPetHairType.grid(column=0, row=10, sticky=W, pady=15)
        descPetHairColor = Label(self.petWindow, text=f'Cor:  {self.petHairColor}', width=100)
        descPetHairColor.grid(column=0, row=12, sticky=W, pady=15)
        descPetAge = Label(self.petWindow, text=f'Idade:  {self.petAge}', width=100)
        descPetAge.grid(column=0, row=14, sticky=W, pady=15)
        descPetObs = Label(self.petWindow, text=f'Observações: ')
        descPetObs.grid(column=0, row=16, sticky=W, pady=15)
        textPetObs = Label(self.petWindow, text=f'{self.petObs}', justify=LEFT, wraplength=415)
        textPetObs.grid(column=0, row=17, sticky=W)

        descClientName = Label(self.clientWindow, text=f'Nome:  {self.clientName}', width=100)
        descClientName.grid(column=0, row=0, sticky=W, pady=15)
        descClientEmail = Label(self.clientWindow, text=f'Email:  {self.clientEmail}', width=100)
        descClientEmail.grid(column=0, row=2, sticky=W, pady=15)
        descClientPhone = Label(self.clientWindow, text=f'Telemóvel:  {self.clientPhone}')
        descClientPhone.grid(column=0, row=4, sticky=W, pady=15)
        descClientNIF = Label(self.clientWindow, text=f'NIF:  {self.clientNIF}')
        descClientNIF.grid(column=0, row=6, sticky=W, pady=15)
        descClientAddress = Label(self.clientWindow, text=f'Morada:  {self.clientAdr}', width=100)
        descClientAddress.grid(column=0, row=8, sticky=W, pady=15)

        descAppServices = Label(self.appointmentWindow, text=f'Serviços:  {self.appServices}', width=100,
                                justify=LEFT, wraplength=415)
        descAppServices.grid(column=0, row=0, sticky=W, pady=15)
        descAppDate = Label(self.appointmentWindow, text=f'Dia:  {self.appDate}')
        descAppDate.grid(column=0, row=2, sticky=W, pady=15)
        descAppTime = Label(self.appointmentWindow, text=f'Hora:  {self.appTime}')
        descAppTime.grid(column=0, row=4, sticky=W, pady=15)
        descAppPrice = Label(self.appointmentWindow, text=f'Preço:  {self.appPrice} €')
        descAppPrice.grid(column=0, row=6, sticky=W, pady=15)
        descAppObs = Label(self.appointmentWindow, text=f'Observações: ')
        descAppObs.grid(column=0, row=8, sticky=W, pady=15)
        textAppObs = Label(self.appointmentWindow, text=f'{self.appObs}', justify=LEFT, wraplength=415)
        textAppObs.grid(column=0, row=9, sticky=W)

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

        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))

        # Create a button that finalizes appointment by sending it to te history table
        butFinalize = Button(self.clientWindow, text='Finalizar', command=self.finalizeAppointment)
        butFinalize.grid(column=0, row=10, pady=150, padx=(30, 0), sticky=W)

        # Create a button that destroys appointment
        butDestroy = Button(self.clientWindow, text='Remover', command=self.destroyAppointment)
        butDestroy.grid(column=0, row=10, pady=150, padx=(160, 0), sticky=W)

        # Creates a button that allows the user to change all the entries about the pet, the client and the appointment
        butChange = Button(self.clientWindow, text='Alterar', command=self.changeInfo)
        butChange.grid(column=0, row=10, pady=150, padx=(290, 0), sticky=W)

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][0:10]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][10:16]

    def getsAppointmentInfo(self):
        """Gets and filters information about the appointments from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][16:21]

    def destroyAppointment(self):
        """Checks if user wants to destroy appointment and if so, deletes it from the database."""

        # Shows a popup to confirm destruction of appointments
        message = messagebox.askquestion('Eliminar', 'Deseja eliminar a marcação?', parent=self.window)

        # If we want to eliminate our appointment, we change our database, else, does nothing
        if message == 'yes':

            # Changes database entries
            deleteRecordAppointment(self.appointmentID)

            # Refreshes all trees of our application
            self.root.refreshApplication()

            # Eliminates window
            self.destroy()

    def finalizeAppointment(self):
        """Checks if user wants to finalize appointment and if so, sends it to the history table and refreshes tree."""

        # Shows a popup to confirm finalization
        message = messagebox.askquestion('Finalizar', 'Deseja finalizar a marcação?', parent=self.window)

        # If we want to finalize our appointment, we change our database, else, does nothing
        if message == 'yes':

            # Changes database entries
            insertRecordHistory((self.appServices, self.appDate, self.appTime, self.appPrice, self.appObs, self.petID))
            deleteRecordAppointment(self.appointmentID)

            # Refreshes all trees of our application
            self.root.refreshApplication()

            # Eliminates window
            self.destroy()

    def changeInfo(self):
        """
        Description:
        > Changes previous entries to the newly provided ones from the user.
        """
        WindowUpdateAppointment(self, self.appointmentID, self.root)
