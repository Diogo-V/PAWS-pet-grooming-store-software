from tkinter import *
from tkinter.ttk import *


class Statistics(Frame):
    """
    Frame that holds statistics about everything.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        """
        # Creates statistics tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)







