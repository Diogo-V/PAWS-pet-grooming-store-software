from tkinter import *
from tkinter.ttk import *
from database.src.utils.querying import *
from datetime import date


# Criar a parte de quando clico numa das entradas da arvore e aparece uma descrição sobre o appointment + 2 butões
# para o cancelar e para o concluir

# Criar a parte de dar refresh cada vez que entro na aba dos appointments

# Criar a parte de criar, deletar e dar update nos appointments

# Criar a parte em que os resultados aparecem todos sorted pela hora de entrada


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
        self.search.pack(padx=20, pady=20)
        self.display.pack(padx=20, pady=(0, 20))

        # Creates tree that will display all the appointments for the day
        self.tree = Treeview(self.display, columns=(1, 2, 3, 4, 5, 6), height=900)
        self.tree.pack(padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=216)
        self.tree.column(2, stretch=NO, anchor='center', width=216)
        self.tree.column(3, stretch=NO, anchor='center', width=216)
        self.tree.column(4, stretch=NO, anchor='center', width=216)
        self.tree.column(5, stretch=NO, anchor='center', width=216)
        self.tree.column(6, stretch=NO, anchor='center', width=216)

        # Define columns heading
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading(1, text='Nome do animal', anchor='center')
        self.tree.heading(2, text='Nome do cliente', anchor='center')
        self.tree.heading(3, text='Serviços', anchor='center')
        self.tree.heading(4, text='Hora', anchor='center')
        self.tree.heading(5, text='Número de telemóvel', anchor='center')
        self.tree.heading(6, text='Observações', anchor='center')

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

        # Creates search button and puts it on the screen
        self.button = Button(self.search, text='Procurar', command=self.updateTree)
        self.button.pack(side=LEFT, padx=(515, 30), pady=20)

        # Initializes appointments tree view with today's appointments
        self.updateTree()

    def getsEntriesDate(self):
        """
        Description:
        > Gets values inside each entry box and creates a date
        """
        return date(self.entryYear.get(), self.entryMonth.get(), self.entryDay.get())

    def updateTree(self):
        """
        Description:
        > Gets values inside our search entries and updates rows inside our tree view.
        """

        # Gets values of each entry
        dateAppointment = date(eval(self.entryYear.get()), eval(self.entryMonth.get()), eval(self.entryDay.get()))

        # Deletes previous rows before inserting the new ones

        # Gets rows to be displayed
        rows = getsDayAppointments(dateAppointment)

        # Sorts rows according to it's time of arrival at the store
        sorted(rows)

        # Gets rows to be displayed and does so
        for row in rows:
            self.tree.insert('', 'end', values=row)
