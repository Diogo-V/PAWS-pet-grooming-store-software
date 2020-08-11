from tkinter import *
from tkinter.ttk import *


class Appointments(Frame):
    """
    Frame that holds appointments for the day.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        """
        # Creates appointments tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)





