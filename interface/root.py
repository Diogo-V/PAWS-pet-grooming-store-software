from interface.frames.appointments import *
from interface.frames.database import *
from interface.frames.statistics import *
from tkinter.font import *


class MainApplication:
    """
    Creates a notebooks that holds our 3 frames: appointments, database and statistics.
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

        # Changes default font of the entire file
        myFont = Font(font=("Varela", 12))
        self.root.option_add("*Font", myFont)

        # Creates root's notebook
        self.notebook = Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Changes style of notebook frames
        Style().theme_settings(Style().theme_use(), {"TNotebook.Tab": {"configure": {"padding": [185.5, 9]}}})

        # Creates notebook's frames
        appointmentsFrame = Appointments(self.notebook)
        databaseFrame = Database(self.notebook)
        statisticsFrame = Statistics(self.notebook)

        # Adds our frames to the notebook
        self.notebook.add(appointmentsFrame, text='Marcações')
        self.notebook.add(databaseFrame, text='Base de dados')
        self.notebook.add(statisticsFrame, text='Estatisticas')

        # Puts notebook on the screen
        self.notebook.pack()

    def run(self):
        """Runs our application."""
        self.root.mainloop()
