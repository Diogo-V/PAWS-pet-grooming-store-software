from tkinter import *
from tkinter.ttk import *


class WindowLink(Toplevel):
    """
    Toplevel window used to create a new relationship between an animal and an owner.
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
        self.title('Informações sobre esta relação')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates instance variable so that it can be used later on
        self.master = master

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)
