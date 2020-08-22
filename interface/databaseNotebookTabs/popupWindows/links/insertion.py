from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class WindowInsertLink(Toplevel):
    """
    Toplevel window used to create a new relationship between an animal and an owner.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Inserir nova relação entre animal e dono')
        self.geometry("1000x500")
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)
