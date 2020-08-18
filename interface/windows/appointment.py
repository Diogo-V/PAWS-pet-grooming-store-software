from tkinter import *
from tkinter.ttk import *


class WindowAppointment(Toplevel):
    """
    Toplevel window that holds all the information about a specific appointment
    """

    def __init__(self, master, info):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param info: tuple that contains information about the appointment -> tuple
        """

        # Creates toplevel window that will be displayed
        Toplevel.__init__(self, master)
        self.title('Informações sobre a marcação')

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=500, width=500)
        self.window.pack(fill='both', expand=True)

