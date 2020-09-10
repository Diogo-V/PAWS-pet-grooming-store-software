from operator import itemgetter

from database.src.functions.deletion import deleteRecordClient, deleteClientsLinks, deleteClientsPets
from database.src.query.databaseNotebookTabs.clients import getsRequestedClients, getsAllClients
from interface.databaseNotebookTabs import clients
from interface.databaseNotebookTabs.popupWindows.clients.information import WindowClient
from interface.rootNotebookTabs.popupWindows.appointments.information import *


class WindowDeleteClient(Toplevel):
    """
    Toplevel window used to delete existing clients.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> notebook
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Apagar cliente')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a search frame and a display frame and puts them on the screen
        self.search = LabelFrame(self.window, text=' Pesquisar ', width=1000, height=100)
        self.display = LabelFrame(self.window, text=' Clientes ', width=1000, height=300)
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
        clientName = StringVar()
        clientPhone = StringVar()
        petName = StringVar()

        # Creates labels and entry fields and puts them on the screen
        self.labelClientName = Label(self.search, text='Nome:')
        self.labelClientName.pack(side=LEFT, padx=(25, 5), pady=10)
        self.entryClientName = Entry(self.search, textvariable=clientName)
        self.entryClientName.pack(side=LEFT, padx=(0, 5), pady=10)
        self.labelClientPhone = Label(self.search, text='Telemóvel:')
        self.labelClientPhone.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryClientPhone = Entry(self.search, textvariable=clientPhone)
        self.entryClientPhone.pack(side=LEFT, padx=(0, 5), pady=10)
        self.labelPetName = Label(self.search, text='Animal:')
        self.labelPetName.pack(side=LEFT, padx=(10, 5), pady=10)
        self.entryPetName = Entry(self.search, textvariable=petName)
        self.entryPetName.pack(side=LEFT, padx=(0, 15), pady=10)

        # Creates search button and puts it on the screen
        self.button = Button(self.search, text='Procurar', command=self.updateTree)
        self.button.pack(side=LEFT, padx=(100, 50), pady=10)

        # Columns names that are going to be inserted inside the tree
        columns = ('', 'Nome do cliente', 'Telemóvel', 'Nome do animal', 'Tipo de animal')

        # Creates tree that will display all the links
        self.tree = Treeview(self.display, columns=columns, height=13, show='headings')
        self.tree.pack(side=LEFT, padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=235)
        self.tree.column(2, stretch=NO, anchor='center', width=235)
        self.tree.column(3, stretch=NO, anchor='center', width=235)
        self.tree.column(4, stretch=NO, anchor='center', width=235)

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
        self.tree.bind('<Double 1>', self.displayClientWindow)

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

        # Sorts
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

        # Gets tuple with the selected client. If none were selected, gets an empty tuple
        client = self.tree.selection()

        # If the user selected more than one client. Throws error and interrupts
        if len(client) != 1:
            messagebox.showerror("Erro", "Selecione apenas uma cliente antes de continuar!", parent=self.window)
            return

        # Gets if an entry was selected
        if client != ():

            # Confirms if the user wants to eliminate this entry
            msg = messagebox.askyesno('Confirmar remoção', 'Deseja remover a entrada selecionada?', parent=self.window)

            # If the user agreed, deletes it
            if msg:

                # Gets client row id
                clientID = self.tree.item(client[0], "values")[0]

                # Removes clients from database
                deleteRecordClient(clientID)

                # Asks if the user wants to eliminate all the associated pets. if so, does it
                if messagebox.askyesno('Remover animais', 'Deseja remover os animais associados?', parent=self.window):
                    deleteClientsPets(clientID)

                # Removes associated links
                deleteClientsLinks(clientID)

                # Refreshes main tree
                clients.Clients.refreshTree(self.master)

                # Eliminates window
                self.destroy()

        # If a client was not selected and the button was still pressed, we throw an error
        else:
            messagebox.showerror('Erro', 'Selecione um cliente antes de tentar remover!', parent=self.window)

    def getsEntries(self):
        """
        Description:
        > Gets values inside each entry box and creates a list with those values.
        """
        return [self.entryClientName.get(), self.entryClientPhone.get(), self.entryPetName.get()]

    def updateTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets information in entries
        [clientName, clientPhone, petName] = self.getsEntries()

        # If no information was typed, just refresh page
        if clientName == '' and clientPhone == '' and petName == '':
            self.refreshTree()
        else:

            # Gets rows that are going to be displayed
            rows = getsRequestedClients([clientName, clientPhone, petName])

            # Displays our queried rows
            self.displayTreeRows(rows)

    def refreshTree(self):
        """Refreshes all the entries inside the tree. Show default entries."""

        # Gets default rows
        rows = getsAllClients()

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

    def displayClientWindow(self, event):
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

            # Since we only need the client id to query trough the database, we discard the rest
            clientID = info[0]

            # Creates toplevel window that will display the information about this client
            WindowClient(self, clientID)
