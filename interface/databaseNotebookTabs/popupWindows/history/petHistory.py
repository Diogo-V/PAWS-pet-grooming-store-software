import datetime

from database.src.query.databaseNotebookTabs.history import getsPetHistory
from database.src.utils.converters import dateToString, stringToDate
from interface.databaseNotebookTabs.popupWindows.history.information import WindowHistory
from interface.rootNotebookTabs.popupWindows.appointments.information import *


class WindowPetHistory(Toplevel):
    """
    Toplevel window used to search and delete pets.
    """

    def __init__(self, master, animalID):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> notebook
        :param animalID: animal rowid inside the database -> integer
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Ver histórico do animal')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=600, width=1250)
        self.window.pack(fill='both', expand=True)

        # Creates a display frame and put it on the screen
        self.display = LabelFrame(self.window, text=' Histórico ', width=1250, height=600)
        self.display.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        self.display.grid_propagate(False)

        # Columns names that are going to be inserted inside the tree
        columns = ('', 'Dia', 'Hora', 'Serviços', 'Observações')

        # Creates tree that will display all the links
        self.tree = Treeview(self.display, columns=columns, height=30, show='headings')
        self.tree.pack(side=LEFT, padx=10, pady=5)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=297)
        self.tree.column(2, stretch=NO, anchor='center', width=297)
        self.tree.column(3, stretch=NO, anchor='center', width=297)
        self.tree.column(4, stretch=NO, anchor='center', width=297)

        # Define columns heading and sets their sorting function
        for col in columns:
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.treeSortColumn(self.tree, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbar = Scrollbar(self.display, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Populates tree
        self.refreshTree(animalID)

        # Links double click on a row with a window popup
        self.tree.bind('<Double 1>', self.displayHistoryWindow)

    def treeSortColumn(self, tv, col, reverse):
        """
        Description:
        > Sorts the clicked column of the tree.
        :param tv: tree -> TreeView
        :param col: selected column name -> string
        :param reverse: checks if we need to reverse it -> boolean
        """

        # Gets lines from the selected column
        lines = [(tv.set(k, col), k) for k in tv.get_children('')]

        # Checks if the selected column is the day one. If so, we need to convert each date to an ordinal number and
        # then, reverse the process again
        if col == 'Dia':

            # Passes string to an integer
            if type(lines) is list and lines != []:
                lines = list(map(lambda app: self.transformsStringAppointmentToInteger(app, 0), lines))
            elif type(lines) is tuple:
                lines = self.transformsStringAppointmentToInteger(lines, 0)

            # Sorts
            lines.sort(reverse=reverse)

            # Passes integer to string
            if type(lines) is list and lines != []:
                lines = list(map(lambda app: self.transformsIntegerAppointmentDateToString(app, 0), lines))
            elif type(lines) is tuple:
                lines = self.transformsIntegerAppointmentDateToString(lines, 0)

        else:

            # Only need to sort
            lines.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(lines):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, text=col, command=lambda _col=col: self.treeSortColumn(tv, _col, not reverse))

    def refreshTree(self, animalID):
        """
        Description:
        > Refreshes all the entries inside the tree. Show default entries.

        :param animalID: animal rowid inside the database -> integer
        """

        # Gets default rows
        rows = getsPetHistory(animalID)

        # Puts and displays rows in tree
        self.displayTreeRows(rows)

    def displayTreeRows(self, rows):
        """
        Description:
        > Sorts rows according to pet's name and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.tree.delete(*self.tree.get_children())

        # Sorts rows according to date
        self.treeSortColumn(self.tree, 'Dia', False)

        # Displays rows inside our tree
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def displayHistoryWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected pet.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.tree.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:

            # Gets row information
            info = self.tree.item(item, 'values')

            # Since we only need the history id to query trough the database, we discard the rest
            historyID = info[0]

            WindowHistory(self, historyID)

    @staticmethod
    def transformsIntegerAppointmentDateToString(app, idxOfDate):
        """
        Description:
        > Changes date inside app from integer to a printable string.
        :param app: tuple with the information about an appointment inside our database -> tuple
        :param idxOfDate: tuple index where date is located -> integer
        :return: tuple with our formatted information -> tuple
        """
        app = list(app)
        app[idxOfDate] = dateToString(datetime.date.fromordinal(app[idxOfDate]))
        return tuple(app)

    @staticmethod
    def transformsStringAppointmentToInteger(app, idxOfDate):
        """
        Description:
        > Changes input date into an integer so that we can insert it inside our database.
        :param app: tuple with the information about an appointment inside our database -> tuple
        :param idxOfDate: tuple index where date is located -> integer
        :return: tuple with our formatted information -> tuple
        """
        app = list(app)
        app[idxOfDate] = stringToDate(app[idxOfDate]).toordinal()
        return tuple(app)
