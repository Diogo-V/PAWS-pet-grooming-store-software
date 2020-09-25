from database.src.utils.maintenance import clearsElementsWithNoLinks
from interface.rootNotebookTabs.appointments import *
from interface.rootNotebookTabs.database import *
from interface.rootNotebookTabs.statistics import *


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
        self.appointmentsFrame = DayAppointments(self.notebook, self)
        self.databaseFrame = Database(self.notebook, self)
        self.statisticsFrame = Statistics(self.notebook)

        # Adds our rootNotebookTabs to the notebook. The spaces fill the rest of the tab's space
        self.notebook.add(self.appointmentsFrame, text='                    Marcações                    ')
        self.notebook.add(self.databaseFrame, text='                    Base de dados                    ')
        self.notebook.add(self.statisticsFrame, text='                    Estatísticas                    ')

        # Puts notebook on the screen
        self.notebook.pack()

    def run(self):
        """Runs our application."""
        self.root.mainloop()

    def refreshApplication(self):
        """Refreshes all the trees inside all tabs of our application. Also clears all free entries."""
        clearsElementsWithNoLinks()
        self.databaseFrame.refreshAllTabs()
        self.appointmentsFrame.updateTreeDate()
