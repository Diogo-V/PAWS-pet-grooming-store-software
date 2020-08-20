from tkinter import *
from tkinter.ttk import *
from database.src.utils.querying import *


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

        # Creates 3 small frames for each part of the description. Used to organize the information
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=500, width=333)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=500, width=333)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=500, width=334)
        self.petWindow.pack(side=LEFT, fill='both', expand=True)
        self.clientWindow.pack(side=LEFT, fill='both', expand=True)
        self.appointmentWindow.pack(side=LEFT, fill='both', expand=True)

        # Gets a list containing the information that is going to be displayed
        self.information = getsInfoForAppointmentsWindow(appointmentID)

        # Gets and filters information about the pet from the information list
        [petName, petType, petWeight, petHair, petObservations] = self.getsPetInfo()
        [clientName, clientNIF, clientPhone] = self.getsClientInfo()
        [appServices, appDate, appTime, appPrice] = self.getsAppointmentInfo()

        # Creates labels that will describe each field in each section
        Label(self.petWindow, text='Nome: ').grid(column=0, row=0, sticky='e', pady=35)
        Label(self.petWindow, text='Tipo de animal: ').grid(column=0, row=1, sticky='e', pady=35)
        Label(self.petWindow, text='Peso: ').grid(column=0, row=2, sticky='e', pady=35)
        Label(self.petWindow, text='Tipo de pelo: ').grid(column=0, row=3, sticky='e', pady=35)
        Label(self.petWindow, text='Observações: ').grid(column=0, row=4, sticky='e', pady=35)

        Label(self.clientWindow, text='Nome: ').grid(column=0, row=0, sticky='e', pady=35)
        Label(self.clientWindow, text='NIF: ').grid(column=0, row=1, sticky='e', pady=35)
        Label(self.clientWindow, text='Número de telemóvel: ').grid(column=0, row=2, sticky='e', pady=35)

        Label(self.appointmentWindow, text='Serviços: ').grid(column=0, row=0, sticky='e', pady=35)
        Label(self.appointmentWindow, text='Dia: ').grid(column=0, row=1, sticky='e', pady=35)
        Label(self.appointmentWindow, text='Hora: ').grid(column=0, row=2, sticky='e', pady=35)
        Label(self.appointmentWindow, text='Preço do servico: ').grid(column=0, row=3, sticky='e', pady=35)

        # Inserts information about each field for each section after each label
        Label(self.petWindow, text=petName).grid(column=1, row=0, sticky='w', pady=35)
        Label(self.petWindow, text=petType).grid(column=1, row=1, sticky='w', pady=35)
        Label(self.petWindow, text=f"{petWeight}Kg").grid(column=1, row=2, sticky='w', pady=35)
        Label(self.petWindow, text=petHair).grid(column=1, row=3, sticky='w', pady=35)
        Label(self.petWindow, text=petObservations).grid(column=1, row=4, sticky='w', pady=35)

        Label(self.clientWindow, text=clientName).grid(column=1, row=0, sticky='w', pady=35)
        Label(self.clientWindow, text=clientNIF).grid(column=1, row=1, sticky='w', pady=35)
        Label(self.clientWindow, text=clientPhone).grid(column=1, row=2, sticky='w', pady=35)

        Label(self.appointmentWindow, text=appServices).grid(column=1, row=0, sticky='w', pady=35)
        Label(self.appointmentWindow, text=appDate).grid(column=1, row=1, sticky='w', pady=35)
        Label(self.appointmentWindow, text=appTime).grid(column=1, row=2, sticky='w', pady=35)
        Label(self.appointmentWindow, text=f"{appPrice}€").grid(column=1, row=3, sticky='w', pady=35)

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list."""
        return self.information[0][0:5]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list."""
        return self.information[0][5:8]

    def getsAppointmentInfo(self):
        """Gets and filters information about the appointments from the information list."""
        return self.information[0][8:12]
