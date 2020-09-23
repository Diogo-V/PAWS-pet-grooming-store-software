from tkinter import *
from tkinter.ttk import *

from database.src.query.databaseNotebookTabs.history import getsInfoForHistoryWindow


class WindowHistory(Toplevel):
    """
    Toplevel window that holds all the information about a specific appointment.
    """

    def __init__(self, master, historyID):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param historyID: appointment rowid inside the database -> integer
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Informações sobre a marcação passada')
        self.geometry("1250x600")
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a LabelFrame that holds the information about this past appointment
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ')
        self.appointmentWindow.pack(fill='both', expand=True)
        self.appointmentWindow.grid_propagate(False)

        # Gets and filters information about the past appointment from the information list
        [self.appSrv, self.appDate, self.appTime, self.appPrice, self.appObs] = getsInfoForHistoryWindow(historyID)[0]

        # Creates labels that will describe each field in each section and puts the requested information after it
        descAppServices = Label(self.appointmentWindow, text=f'Serviços:  {self.appSrv}', width=400,
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
        textAppObs = Label(self.appointmentWindow, text=f'{self.appObs}', justify=LEFT, wraplength=900)
        textAppObs.grid(column=0, row=9, sticky=W)

        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E))
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E))
