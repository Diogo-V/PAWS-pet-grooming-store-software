from operator import itemgetter
from database.src.query.rootNotebookTabs.appointments import getsDayAppointments
from interface.rootNotebookTabs.popupWindows.appointments.information import *
from datetime import date


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

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=self.winfo_screenheight(), width=self.winfo_screenwidth())
        self.window.pack(fill='both', expand=True)

        # Creates a search frame and a display frame and puts them on the screen
        self.search = LabelFrame(self.window, text=' Pesquisar dia ', width=1500, height=100)
        self.display = LabelFrame(self.window, text=' Marcações ')
        self.search.pack(padx=20, pady=20, fill="both", expand=True)
        self.display.pack(padx=20, pady=(0, 20), fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.search.grid_propagate(False)
        self.display.grid_propagate(False)

        # Creates tree that will display all the appointments for the day
        self.tree = Treeview(self.display, columns=(0, 1, 2, 3, 4, 5, 6), height=900)
        self.tree.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=214)
        self.tree.column(2, stretch=NO, anchor='center', width=214)
        self.tree.column(3, stretch=NO, anchor='center', width=214)
        self.tree.column(4, stretch=NO, anchor='center', width=214)
        self.tree.column(5, stretch=NO, anchor='center', width=214)
        self.tree.column(6, stretch=NO, anchor='center', width=214)

        # Define columns heading
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading(0, text='', anchor='w')  # Used to store appointments' id
        self.tree.heading(1, text='Nome do animal', anchor='center')
        self.tree.heading(2, text='Nome do cliente', anchor='center')
        self.tree.heading(3, text='Serviços', anchor='center')
        self.tree.heading(4, text='Hora', anchor='center')
        self.tree.heading(5, text='Número de telemóvel', anchor='center')
        self.tree.heading(6, text='Observações', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbar = Scrollbar(self.display, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Allocates memory for the entry values and puts today's date in there
        day = StringVar(self.search, value=str(date.today().day))
        month = StringVar(self.search, value=str(date.today().month))
        year = StringVar(self.search, value=str(date.today().year))

        # Creates labels and entry fields and puts them on the screen
        self.labelDay = Label(self.search, text='Dia:')
        self.labelDay.pack(side=LEFT, padx=(50, 5), pady=20)
        self.entryDay = Entry(self.search, textvariable=day)
        self.entryDay.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelMonth = Label(self.search, text='Mês:')
        self.labelMonth.pack(side=LEFT, padx=(10, 5), pady=20)
        self.entryMonth = Entry(self.search, textvariable=month)
        self.entryMonth.pack(side=LEFT, padx=(0, 5), pady=20)
        self.labelYear = Label(self.search, text='Ano:')
        self.labelYear.pack(side=LEFT, padx=(10, 5), pady=20)
        self.entryYear = Entry(self.search, textvariable=year)
        self.entryYear.pack(side=LEFT, padx=(0, 15), pady=20)

        # Creates refresh button and puts it on the screen
        self.refresh = Button(self.search, text='Hoje', command=lambda: self.refreshTree(self))
        self.refresh.pack(side=LEFT, padx=(250, 10), pady=20)

        # Creates search button and puts it on the screen
        self.button = Button(self.search, text='Procurar', command=self.updateTreeDate)
        self.button.pack(side=LEFT, padx=(10, 50), pady=20)

        # Initializes appointments tree view with today's appointments
        self.updateTreeDate()

        # Links double click on a row with a window popup
        self.tree.bind('<Double 1>', self.displayAppointmentsWindow)

    def getsEntriesDate(self):
        """
        Description:
        > Gets values inside each entry box and creates a date
        """

        # Gets information (strings) from each entry
        year = self.entryYear.get()
        month = self.entryMonth.get()
        day = self.entryDay.get()

        # If one of the entries is empty, returns today's date. If not, returns requested date
        if year == '' or month == '' or day == '':
            return date.today()
        else:
            return date(eval(year), eval(month), eval(day))

    def updateTreeDate(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets values of each entry
        dateAppointment = self.getsEntriesDate()

        # Gets rows to be displayed
        rows = getsDayAppointments(dateAppointment)

        # Puts and displays rows in tree
        self.displayTreeRows(rows)

    def displayAppointmentsWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected appointment.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.tree.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:

            # Gets row information
            info = self.tree.item(item, 'values')

            # Since we only need the appointment id to query trough the database, we discard the rest
            appointmentID = info[0]

            # Creates toplevel window that will display the information about this appointment
            WindowAppointment(self, appointmentID)

    def displayTreeRows(self, rows):
        """
        Description:
        > Sorts rows according to the time of arrival and displays them on our tree.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.tree.delete(*self.tree.get_children())

        # Sorts rows according to it's time of arrival at the store
        rows.sort(key=itemgetter(4))

        # Displays rows inside our tree
        for row in rows:
            self.tree.insert('', 'end', values=row)

    @staticmethod
    def refreshTree(treeFrame):
        """Refreshes all the entries inside the tree. Show entries for today's date."""

        # Gets rows to be displayed for today
        rows = getsDayAppointments(date.today())

        # Puts and displays rows in tree
        treeFrame.displayTreeRows(rows)
