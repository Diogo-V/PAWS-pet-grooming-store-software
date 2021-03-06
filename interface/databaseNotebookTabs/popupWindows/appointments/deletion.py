from math import floor
from operator import itemgetter

from database.src.query.databaseNotebookTabs.appointments import *
from database.src.utils.constants import typeOfAnimal
from database.src.utils.converters import stringToDate
from interface.rootNotebookTabs.popupWindows.appointments.information import *


class WindowDeleteAppointment(Toplevel):
    """
    Toplevel window used to delete existing appointments.
    """

    def __init__(self, master, root):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> notebook
        :param root: Main application frame window -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Remover marcação')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)
        self.transient(master)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root

        # Creates a search frame and a display frame and puts them on the screen
        self.search = LabelFrame(self.window, text=' Pesquisar ', width=1000, height=100)
        self.display = LabelFrame(self.window, text=' Marcações ', width=1000, height=300)
        self.search.pack(padx=10, pady=10, fill="both", expand=True)
        self.display.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        # Creates a delete button
        self.delete = Button(self.window, text='Deletar entrada selecionada', command=self.deleteEntry)
        self.delete.pack(side=BOTTOM, fill="both", expand=True, padx=50, pady=(0, 10))

        # Blocks resizing for each labelFrame and the button
        self.search.grid_propagate(False)
        self.display.grid_propagate(False)
        self.delete.grid_propagate(False)

        # Allocates memory for the entry values
        petName = StringVar()
        petType = StringVar()
        petBreed = StringVar()
        clientName = StringVar()
        clientPhone = StringVar()

        # Creates labels and entry fields and puts them on the screen
        self.labelPetName = Label(self.search, text='Animal:')
        self.labelPetName.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryPetName = Entry(self.search, textvariable=petName, width=16)
        self.entryPetName.pack(side=LEFT, padx=(0, 15), pady=10)
        self.labelPetType = Label(self.search, text='Tipo:')
        self.labelPetType.pack(side=LEFT, padx=(10, 5), pady=10)
        self.boxPetType = Combobox(self.search, textvariable=petType,
                                   state="readonly", values=[''] + typeOfAnimal, width=11)
        self.boxPetType.pack(side=LEFT, padx=(0, 15), pady=10)
        self.labelPetBreed = Label(self.search, text='Raça:')
        self.labelPetBreed.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryPetBreed = Entry(self.search, textvariable=petBreed, width=16)
        self.entryPetBreed.pack(side=LEFT, padx=(0, 15), pady=10)
        self.labelClientName = Label(self.search, text='Cliente:')
        self.labelClientName.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryClientName = Entry(self.search, textvariable=clientName, width=16)
        self.entryClientName.pack(side=LEFT, padx=(0, 15), pady=10)
        self.labelClientPhone = Label(self.search, text='Telemóvel:')
        self.labelClientPhone.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryClientPhone = Entry(self.search, textvariable=clientPhone, width=16)
        self.entryClientPhone.pack(side=LEFT, padx=(0, 15), pady=10)

        # Creates search button and puts it on the screen
        self.button = Button(self.search, text='Procurar', command=self.updateTree)
        self.button.pack(side=LEFT, padx=(25, 50), pady=10)

        # Columns names that are going to be inserted inside the tree
        columns = ('', 'Nome do animal', 'Tipo de animal', 'Raça', 'Nome do cliente', 'Telemóvel', 'Dia', 'Hora')

        # Creates tree that will display all the links
        self.tree = Treeview(self.display, columns=columns, height=18, show='headings')
        self.tree.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(2, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(3, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(4, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(5, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(6, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))
        self.tree.column(7, stretch=NO, anchor='center', width=floor(self.tree.winfo_screenwidth()/7 - 25))

        # Define columns heading and sets their sorting function
        for col in columns:
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.treeSortColumn(self.tree, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbar = Scrollbar(self.display, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Populates tree
        self.refreshTree()

        # Links double click on a row with a window popup
        self.tree.bind('<Double 1>', self.displayAppointmentWindow)

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

    def deleteEntry(self):
        """
        Description:
        > Gets the id of the selected row and, if the user confirms, deletes it.
        """

        # Gets tuple with the selected appointment. If none were selected, gets an empty tuple
        appointment = self.tree.selection()

        # If the user selected more than one appointment. Throws error and interrupts
        if len(appointment) != 1:
            messagebox.showerror("Erro", "Selecione apenas uma marcação antes de continuar!", parent=self.window)
            return

        # Gets if an entry was selected
        if appointment != ():

            # Confirms if the user wants to eliminate this entry
            msg = messagebox.askyesno('Confirmar remoção', 'Deseja remover a entrada selecionada?', parent=self.window)

            # If the user agreed, deletes it
            if msg:

                # Gets appointment row id
                appointmentID = self.tree.item(appointment[0], "values")[0]

                # Removes appointment from database
                deleteRecordAppointment(appointmentID)

                # Refreshes all trees of our application
                self.root.refreshApplication()

                # Eliminates window
                self.destroy()

        # If a appointment was not selected and the button was still pressed, we throw an error
        else:
            messagebox.showerror('Erro', 'Selecione uma marcação antes de tentar remover!', parent=self.window)

    def getsEntries(self):
        """
        Description:
        > Gets values inside each entry box and creates a list with those values.
        """
        return [self.entryPetName.get(), self.boxPetType.get(), self.entryPetBreed.get(),
                self.entryClientName.get(), self.entryClientPhone.get()]

    def updateTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets information in entries
        [petName, petType, petBreed, clientName, clientPhone] = self.getsEntries()

        # If no information was typed, just refresh page
        if petName == '' and petType == '' and clientName == '' and clientPhone == '' and petBreed == '':
            self.refreshTree()
        else:

            # Gets rows that are going to be displayed
            rows = getsRequestedAppointments([petName, petType, petBreed, clientName, clientPhone])

            # Displays our queried rows
            self.displayTreeRows(rows)

    def refreshTree(self):
        """Refreshes all the entries inside the tree. Show default entries."""

        # Gets default rows
        rows = getsAllAppointments()

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

        # Sorts rows according to pet's name
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def displayAppointmentWindow(self, event):
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

            # Since we need the appointment id and the owner's name to query trough the database, we discard the rest
            appointmentID = info[0]
            clientName = info[4]

            # Creates toplevel window that will display the information about this appointment
            WindowDayAppointment(self, appointmentID, clientName, self.root)

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
