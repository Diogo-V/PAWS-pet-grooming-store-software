from interface.rootNotebookTabs.appointments import *
from interface.rootNotebookTabs.database import *
from interface.rootNotebookTabs.statistics import *
from tkinter.font import *


class MainApplication:
    """
    Creates a notebooks that holds our 3 rootNotebookTabs: appointments, database and statistics.
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

        # Creates style for root notebook rootNotebookTabs
        Style().theme_settings(Style().theme_use(), {"TNotebook.Tab": {"configure": {"padding": [105.5, 9]}}})

        # Creates root's notebook
        self.notebook = Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Creates notebook's rootNotebookTabs
        appointmentsFrame = Appointments(self.notebook)
        databaseFrame = Database(self.notebook)
        statisticsFrame = Statistics(self.notebook)

        # Adds our rootNotebookTabs to the notebook. The spaces fill the rest of the tab's space
        self.notebook.add(appointmentsFrame, text='                    Marcações                    ')
        self.notebook.add(databaseFrame, text='                    Base de dados                    ')
        self.notebook.add(statisticsFrame, text='                    Estatisticas                    ')

        # Puts notebook on the screen
        self.notebook.pack()

    def run(self):
        """Runs our application."""
        self.root.mainloop()
