from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.deletion import deleteRecordAppointment
from database.src.functions.insertion import insertRecordHistory
from database.src.query.rootNotebookTabs.appointments import getsInfoForAppointmentsWindow
from interface.rootNotebookTabs import appointments


class WindowAppointment(Toplevel):
    """
    Toplevel window that holds all the information about a specific appointment.
    """

    def __init__(self, master, appointmentID):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param appointmentID: appointment rowid inside the database -> integer
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Informações sobre a marcação')
        self.geometry("1000x500")
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates class variable so that it can be used as a property
        self.master = master
        self.appointmentID = appointmentID

        # Creates 3 small LabelFrame for each part of the description. Used to organize the information
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=500, width=333)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=500, width=333)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=500, width=334)
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
        [self.petID, self.petName, self.petType, self.petWeight, self.petHair, self.petObs] = self.getsPetInfo()
        [self.clientName, self.clientNIF, self.clientPhone] = self.getsClientInfo()
        [self.appServices, self.appDate, self.appTime, self.appPrice] = self.getsAppointmentInfo()

        # Formats some fields so that they don't show 'None'
        if self.petObs is None:
            self.petObs = ''
        if self.clientPhone is None:
            self.clientPhone = ''
        if self.clientNIF is None:
            self.clientNIF = ''
        if self.petWeight is None or self.petWeight is 0:
            self.petWeight = ''

        # Creates labels that will describe each field in each section and puts the requested information after it
        descPetName = Label(self.petWindow, text=f'Nome:  {self.petName}', width=100)
        descPetName.grid(column=0, row=0, sticky=W, pady=15)
        descPetType = Label(self.petWindow, text=f'Tipo de animal:  {self.petType}')
        descPetType.grid(column=0, row=2, sticky=W, pady=15)
        descPetWeight = Label(self.petWindow, text=f'Peso:  {self.petWeight}Kg')
        descPetWeight.grid(column=0, row=4, sticky=W, pady=15)
        descPetHair = Label(self.petWindow, text=f'Tipo de pelo:  {self.petHair}')
        descPetHair.grid(column=0, row=6, sticky=W, pady=15)
        descPetObs = Label(self.petWindow, text=f'Observações: ')
        descPetObs.grid(column=0, row=8, sticky=W, pady=15)
        textPetObs = Label(self.petWindow, text=f'{self.petObs}', justify=LEFT, wraplength=333)
        textPetObs.grid(column=0, row=9, sticky=W)

        descClientName = Label(self.clientWindow, text=f'Nome:  {self.clientName}', width=100)
        descClientName.grid(column=0, row=0, sticky=W, pady=15)
        descClientNIF = Label(self.clientWindow, text=f'NIF:  {self.clientNIF}')
        descClientNIF.grid(column=0, row=2, sticky=W, pady=15)
        descClientPhone = Label(self.clientWindow, text=f'Telemóvel:  {self.clientPhone}')
        descClientPhone.grid(column=0, row=4, sticky=W, pady=15)

        descAppServices = Label(self.appointmentWindow, text=f'Serviços:  {self.appServices}', width=100)
        descAppServices.grid(column=0, row=0, sticky=W, pady=15)
        descAppDate = Label(self.appointmentWindow, text=f'Dia:  {self.appDate}')
        descAppDate.grid(column=0, row=2, sticky=W, pady=15)
        descAppTime = Label(self.appointmentWindow, text=f'Hora:  {self.appTime}')
        descAppTime.grid(column=0, row=4, sticky=W, pady=15)
        descAppPrice = Label(self.appointmentWindow, text=f'Preço do servico:  {self.appPrice}€')
        descAppPrice.grid(column=0, row=6, sticky=W, pady=15)

        # Creates separators so that we can organize the window more efficiently
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))

        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))

        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))

        # Used to get some space between the appointments information and the buttons
        Label(self.appointmentWindow, text='').grid(column=0, row=7, pady=10)
        Label(self.appointmentWindow, text='').grid(column=0, row=8, pady=10)

        # Create a button that finalizes appointment by sending it to te history table
        butFinalize = Button(self.appointmentWindow, text='Finalizar', command=self.finalizeAppointment)
        butFinalize.grid(column=0, row=9, pady=20, padx=(60, 50), sticky=W)

        # Create a button that destroys appointment
        butDestroy = Button(self.appointmentWindow, text='Remover', command=self.destroyAppointment)
        butDestroy.grid(column=0, row=9, pady=20, padx=(180, 0), sticky=W)

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list."""
        return self.information[0][0:6]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list."""
        return self.information[0][6:9]

    def getsAppointmentInfo(self):
        """Gets and filters information about the appointments from the information list."""
        return self.information[0][9:13]

    def destroyAppointment(self):
        """Checks if user wants to destroy appointment and if so, deletes it from the database."""

        # Shows a popup to confirm destruction of appointments
        message = messagebox.askquestion('Eliminar', 'Deseja eliminar a marcação?')

        # If we want to eliminate our appointment, we change our database, else, does nothing
        if message == 'yes':

            # Changes database entries
            deleteRecordAppointment(self.appointmentID)

            # Refresh tree because we now have a different display
            appointments.DayAppointments.refreshTree(self.master)

    def finalizeAppointment(self):
        """Checks if user wants to finalize appointment and if so, sends it to the history table and refreshes tree."""

        # Shows a popup to confirm finalization
        message = messagebox.askquestion('Finalizar', 'Deseja finalizar a marcação?')

        # If we want to finalize our appointment, we change our database, else, does nothing
        if message == 'yes':

            # Changes database entries
            insertRecordHistory((self.appServices, self.appDate, self.appTime, self.appPrice, self.petID))
            deleteRecordAppointment(self.appointmentID)

            # Refresh tree because we now have a different display
            appointments.DayAppointments.refreshTree(self.master)
