from tkinter import *
from tkinter.ttk import *


class Database(Frame):
    """
    Frame that holds buttons and options to access, modify and update our database.
    """

    def __init__(self, master, **kwargs):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> Tk
        """
        # Creates database tab for the notebook
        Frame.__init__(self, master)
        super().__init__(master, **kwargs)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=self.winfo_screenheight(), width=self.winfo_screenmmwidth())
        self.window.pack(fill='both', expand=True)
