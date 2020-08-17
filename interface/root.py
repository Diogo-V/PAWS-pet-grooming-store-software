from interface.windows.appointments import *
from interface.windows.database import *
from interface.windows.statistics import *


class MainApplication:
    """
    Creates a notebooks that holds our 3 tabs: appointments, database and statistics.
    """

    def __init__(self, title):
        """
        Description:
        > Constructs our main window.

        :param title: title of our application -> string
        """

        self.root = Tk()  # Creates root window
        self.root.title(title)  # Window title
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.root.attributes('-zoomed', True)  # Initializes src as maximized

        # Creates root's notebook
        self.notebook = Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Changes style of notebook windows
        Style().theme_settings(Style().theme_use(), {"TNotebook.Tab": {"configure": {"padding": [185.5, 9]}}})

        # Creates notebook's tabs
        appointments = Appointments(self.notebook)
        database = Database(self.notebook)
        statistics = Statistics(self.notebook)

        # Adds our tabs to the notebook
        self.notebook.add(appointments, text='Marcações')
        self.notebook.add(database, text='Base de dados')
        self.notebook.add(statistics, text='Estatisticas')

        # Puts notebook on the screen
        self.notebook.pack()

    def run(self):
        """Runs our application."""
        self.root.mainloop()
