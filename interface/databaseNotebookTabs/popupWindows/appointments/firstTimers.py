import datetime
from operator import itemgetter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.insertion import *
from database.src.query.databaseNotebookTabs.appointments import getsAppointmentsForDayAppTree
from database.src.utils.constants import typeOfAnimal, services
from database.src.utils.converters import servicesToString, timeToString
from interface.databaseNotebookTabs.popupWindows.appointments.information import WindowAppointment


class WindowFirstTimer(Toplevel):
    """
    Toplevel window that creates a first timer in our database. Creates a pet, client and an appointment.
    """

    def __init__(self, master, root):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param root: Main application frame window -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Primeira vez')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=600, width=1250)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root

        # Creates 3 small LabelFrame for each part of the description
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=500, width=276)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=500, width=276)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=250, width=625)
        self.dayAppWindow = LabelFrame(self.window, text=' Marcações para o dia selecionado ', height=325, width=699)

        # Puts everything on the screen
        self.petWindow.grid(column=1, row=0, rowspan=5)
        self.clientWindow.grid(column=2, row=0, rowspan=5)
        self.appointmentWindow.grid(column=0, row=0, rowspan=3)
        self.dayAppWindow.grid(column=0, row=3, rowspan=3)

        # Blocks resizing of our frames
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)
        self.appointmentWindow.grid_propagate(False)
        self.dayAppWindow.grid_propagate(False)

        # Creates a submit button
        self.auxFrame = Frame(self.window, width=333, height=100)
        self.auxFrame.grid(column=1, row=5, columnspan=2, sticky=(W, S, E, N))
        self.auxFrame.grid_propagate(False)
        self.submitBtt = Button(self.auxFrame, text="Submeter", width=38, command=self.submit)
        self.submitBtt.pack(side=LEFT, fill="both", expand=True, padx=(5, 7), pady=5)

        # Restriction commands
        validateString = (master.register(self.validateString), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateDay = (master.register(self.validateDay), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMonth = (master.register(self.validateMonth), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateYear = (master.register(self.validateYear), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateHours = (master.register(self.validateHours), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMinutes = (master.register(self.validateMinutes), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates labels to describe each entry field of the to be inserted pet
        labelPetName = Label(self.petWindow, text="Nome:")
        labelPetName.grid(row=0, column=0, padx=(5, 0), pady=20, sticky=W)
        labelPetType = Label(self.petWindow, text="Tipo:")
        labelPetType.grid(row=2, column=0, padx=(5, 0), pady=20, sticky=W)
        labelPetType = Label(self.petWindow, text="Raça:")
        labelPetType.grid(row=4, column=0, padx=(5, 0), pady=20, sticky=W)
        labelPetObservations = Label(self.petWindow, text="Observações:")
        labelPetObservations.grid(row=6, column=0, padx=5, pady=20, sticky=W)

        # Creates needed pet variables
        petName = StringVar()
        petType = StringVar()
        petBreed = StringVar()

        # Creates entries for pets
        self.entryPetName = Entry(self.petWindow, textvariable=petName, width=18)
        self.entryPetName.grid(column=1, row=0, padx=(0, 5), pady=10, sticky=W)
        self.entryPetType = Combobox(self.petWindow, textvariable=petType, state="readonly",
                                     values=typeOfAnimal, width=18)
        self.entryPetType.grid(column=1, row=2, padx=(0, 5), pady=10, sticky=W)
        self.entryPetBreed = Entry(self.petWindow, textvariable=petBreed, width=18)
        self.entryPetBreed.grid(column=1, row=4, padx=(0, 5), pady=10, sticky=W)
        self.entryPetObs = Text(self.petWindow, width=32, height=13)
        self.entryPetObs.grid(column=0, row=7, padx=5, pady=0, sticky=W, columnspan=4)

        # Creates separators to better organize our pets frame
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=4)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=4)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=4)

        # Creates labels to describe each entry field of the to be inserted client
        labelClientName = Label(self.clientWindow, text="Nome:")
        labelClientName.grid(row=0, column=0, padx=(5, 0), pady=20, sticky=W)
        labelClientPhone = Label(self.clientWindow, text="Telemóvel:")
        labelClientPhone.grid(row=2, column=0, padx=(5, 0), pady=20, sticky=W)

        # Creates needed client variables
        clientName = StringVar()
        clientPhone = StringVar()

        # Creates entries for client
        self.entryClientName = Entry(self.clientWindow, textvariable=clientName, validate="focusout",
                                     validatecommand=validateString, invalidcommand=self.entryError)
        self.entryClientName.grid(column=1, row=0, padx=(10, 200), pady=10, sticky=W)
        self.entryClientPhone = Entry(self.clientWindow, textvariable=clientPhone, validate="focusout",
                                      validatecommand=validateNumber, invalidcommand=self.entryError)
        self.entryClientPhone.grid(column=1, row=2, padx=(10, 5), pady=10, sticky=W)

        # Creates separators to better organize our clients frame
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)

        # Creates 2 separate frames inside our appointments frames. Used to organize our UI
        self.appInputs = Frame(self.appointmentWindow, height=250, width=350, borderwidth=2, relief=RIDGE)
        self.appServices = Frame(self.appointmentWindow, height=297, width=350, borderwidth=2, relief=RIDGE)
        self.appInputs.pack(side=LEFT, fill='both', expand=True, pady=(0, 8), padx=(8, 0))
        self.appServices.pack(side=LEFT, fill='both', expand=True, pady=(0, 8), padx=(0, 8))

        # Creates labels to describe each of the entries
        self.labelDate = Label(self.appInputs, text='Data:')
        self.labelDate.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        self.labelTime = Label(self.appInputs, text='Hora:')
        self.labelTime.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        self.labelPrice = Label(self.appInputs, text='Preço:')
        self.labelPrice.grid(row=4, column=0, padx=5, pady=10, sticky=W)
        self.labelObservations = Label(self.appInputs, text='Observações:')
        self.labelObservations.grid(row=6, column=0, padx=5, pady=10, sticky=W)
        self.labelServices = Label(self.appServices, text='Serviços:')
        self.labelServices.grid(row=0, column=0, padx=(23, 5), pady=(30, 10), sticky=W)

        # Creates variables that hold the appointments' user input info
        appDateDay = StringVar()
        appDateMonth = StringVar()
        appDateYear = StringVar()
        appTimeHours = StringVar()
        appTimeMinutes = StringVar()
        appPrice = StringVar()

        # Creates entries to get the information from the user
        self.entryDateDay = Entry(self.appInputs, textvariable=appDateDay, validate="focusout",
                                  validatecommand=validateDay, invalidcommand=self.entryError, width=4)
        self.entryDateDay.grid(row=0, column=1, padx=5, pady=10)
        self.entryDateMonth = Entry(self.appInputs, textvariable=appDateMonth, validate="focusout",
                                    validatecommand=validateMonth, invalidcommand=self.entryError, width=4)
        self.entryDateMonth.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.entryDateYear = Entry(self.appInputs, textvariable=appDateYear, validate="focusout",
                                   validatecommand=validateYear, invalidcommand=self.entryError, width=6)
        self.entryDateYear.grid(row=0, column=3, padx=(5, 40), pady=10)
        self.entryTimeHours = Entry(self.appInputs, textvariable=appTimeHours, validate="focusout",
                                    validatecommand=validateHours, invalidcommand=self.entryError, width=4)
        self.entryTimeHours.grid(row=2, column=1, padx=5, pady=10)
        self.entryTimeMinutes = Entry(self.appInputs, textvariable=appTimeMinutes, validate="focusout",
                                      validatecommand=validateMinutes, invalidcommand=self.entryError, width=4)
        self.entryTimeMinutes.grid(row=2, column=2, padx=5, pady=10)
        self.entryPrice = Entry(self.appInputs, textvariable=appPrice, validate="focusout",
                                validatecommand=validateNumber, invalidcommand=self.entryError, width=10)
        self.entryPrice.grid(row=4, column=1, padx=5, pady=10, columnspan=2)
        self.entryObservations = Text(self.appInputs, height=3, width=49)
        self.entryObservations.grid(row=7, column=0, sticky=W, columnspan=5, padx=5, pady=(0, 10))

        # Creates a button that will update all the appointments displayed inside our treeApp
        self.appButton = Button(self.appInputs, text='Ir', width=5, command=self.updateAppTree)
        self.appButton.grid(row=0, column=4, pady=10, padx=(5, 0))

        # Creates a frame to insert our services. Mainly used to organize the UI
        self.services = Frame(self.appServices)
        self.services.grid(row=1, column=0, columnspan=4, padx=(5, 17), sticky=W)

        # Separates entries for the date
        Label(self.appInputs, text='/').grid(column=1, row=0, padx=(57, 0))
        Label(self.appInputs, text='/').grid(column=2, row=0, padx=(47, 0))

        # Separates hours from minutes
        Label(self.appInputs, text='  :').grid(column=1, row=2, padx=(50, 0))

        # Creates variables that hold our provided services. Hold 1 if selected and 0 if not
        self.bath = IntVar()
        self.nails = IntVar()
        self.knot = IntVar()
        self.hygiene = IntVar()
        self.brushing = IntVar()
        self.haircut = IntVar()
        self.misc = IntVar()

        # Creates checkboxes to input our selected services
        self.entryCheckButtonBath = Checkbutton(self.services, text=services[1], variable=self.bath)
        self.entryCheckButtonBath.grid(row=0, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonNails = Checkbutton(self.services, text=services[2], variable=self.nails)
        self.entryCheckButtonNails.grid(row=1, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonKnot = Checkbutton(self.services, text=services[3], variable=self.knot)
        self.entryCheckButtonKnot.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHygiene = Checkbutton(self.services, text=services[4], variable=self.hygiene)
        self.entryCheckButtonHygiene.grid(row=3, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonBrushing = Checkbutton(self.services, text=services[5], variable=self.brushing)
        self.entryCheckButtonBrushing.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHaircut = Checkbutton(self.services, text=services[6], variable=self.haircut)
        self.entryCheckButtonHaircut.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonMisc = Checkbutton(self.services, text=services[7], variable=self.misc)
        self.entryCheckButtonMisc.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # Selects the most provided services for convenience
        self.bath.set(1)
        self.haircut.set(1)
        self.hygiene.set(1)

        # Creates separators to organize our UI
        Separator(self.appInputs, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=5)
        Separator(self.appInputs, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=5)
        Separator(self.appInputs, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=5)

        # Columns names that are going to be inserted inside the tree
        columnsApp = ('', 'Hora', 'Serviços', 'Nome do animal')

        # Creates tree that will display all the pets
        self.treeApp = Treeview(self.dayAppWindow, columns=columnsApp, height=13, show='headings')
        self.treeApp.grid(column=0, row=2, columnspan=5, padx=10, pady=10)

        # Formats columns
        self.treeApp.column("#0", stretch=NO, anchor='center', width=0)
        self.treeApp.column(0, stretch=NO, anchor='center', width=0)
        self.treeApp.column(1, stretch=NO, anchor='center', width=218)
        self.treeApp.column(2, stretch=NO, anchor='center', width=218)
        self.treeApp.column(3, stretch=NO, anchor='center', width=218)

        # Define columns heading and sets their sorting function
        for col in columnsApp:
            self.treeApp.heading(col, text=col, command=lambda _col=col:
                                 self.treeSortColumn(self.treeApp, _col, False), anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarAppointments = Scrollbar(self.dayAppWindow, orient="vertical", command=self.treeApp.yview)
        self.scrollbarAppointments.grid(column=5, row=2, sticky=(N, S))
        self.treeApp.configure(yscrollcommand=self.scrollbarAppointments.set)

        # Links double click on a row with a window popup
        self.treeApp.bind('<Double 1>', self.displayAppointmentWindow)

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

    def submit(self):
        """
        Description:
        > Gets all the values in each entry and creates a pet, a client, a link and an appointment.
        """

        # Gets all entries
        pet = self.getsPetEntries()
        client = self.getsClientEntries()
        appointment = self.getsAppointmentEntries()

        # Checks if all entries are valid. If not, does nothing
        if pet != [] and client != [] and appointment != []:

            # Gets values inside each array
            [petName, petType, petBreed, petObs] = pet
            [clientName, clientPhone] = client
            [appServices, appDate, appTime, appPrice, appObs] = appointment

            # Creates a client in our database and gets his rowid
            clientID = insertRecordClient((clientName, '', clientPhone, '', ''))

            # Validates previous step. Is mainly done just to avoid errors
            if clientID is not None:

                # Creates a pet in our database and gets it's rowid
                petID = insertRecordAnimal((petName, petType, petBreed, '', 0, '', '', 0, petObs))

                # Validates previous step. Is mainly done just to avoid errors
                if petID is not None:

                    # Creates a link between the newly inserted client and pet
                    insertRecordPetClientLink((petID, clientID))

                    # Creates an appointment
                    insertRecordAppointment((appServices, appDate, appTime, appPrice, appObs, petID))

                    # Refreshes all trees of our application
                    self.root.refreshApplication()

                    # Eliminates window
                    self.destroy()

    def updateAppTree(self):
        """
        Description:
        > Gets the requested date and updates the displayed appointments inside the tree.
        """

        # Gets input date
        appDate = self.getsDate()

        # Checks if the user inserted a valid date. If not, does nothing
        if appDate != '':

            # Gets all the appointments for that day
            apps = getsAppointmentsForDayAppTree(appDate)

            # Puts them on the screen
            self.displayTreeAppsRows(apps)

    def displayTreeAppsRows(self, rows):
        """
        Description:
        > Sorts rows according to appointment's hours and displays them on the screen.

        :param rows: list of tuples containing our information -> list
        """

        # Deletes previous rows before inserting the new ones
        self.treeApp.delete(*self.treeApp.get_children())

        # Sorts rows according to appointments' time
        rows.sort(key=itemgetter(1))

        # Displays rows inside our tree
        for row in rows:
            self.treeApp.insert('', 'end', values=row)

    def getsPetEntries(self):
        """
        Description:
        > Gets all the entries to create a pet.
        :return: list of strings
        """

        # Gets values inside each entry
        petName = self.entryPetName.get()
        petType = self.entryPetType.get()
        petBreed = self.entryPetBreed.get()
        petObs = self.entryPetObs.get('1.0', 'end')

        # Checks if required entries were inserted. If an error occurred, returns an empty string
        if petName != '' and petType != '':
            return [petName, petType, petBreed, petObs]
        else:
            messagebox.showerror("Erro", "As entradas do animal não foram inseridas!", parent=self.window)
            return []

    def getsClientEntries(self):
        """
        Description:
        > Gets all the entries to create a client.
        :return: list of strings
        """

        # Gets values inside each entry
        clientName = self.entryClientName.get()
        clientPhone = self.entryClientPhone.get()

        # Checks if required entries were inserted. If an error occurred, returns an empty string
        if clientName != '' and clientPhone != '':
            return [clientName, eval(clientPhone)]
        else:
            messagebox.showerror("Erro", "As entradas do cliente não foram inseridas!", parent=self.window)
            return []

    def getsAppointmentEntries(self):
        """
        Description:
        > Gets all the entries to create an appointment.
        :return: list of strings
        """

        # Gets values inside each entry
        appServices = self.getsServices()
        appPrice = self.getsPrice()
        appTime = self.getsTime()
        appDate = self.getsDate()
        appObs = self.entryObservations.get('1.0', 'end')

        if appDate != '' and appTime != '' and appServices != '':
            return [appServices, appDate, appTime, appPrice, appObs]
        else:
            messagebox.showerror('Erro', 'Insira as entradas necessários na aba das marcações!', parent=self.window)
            return []

    def getsPrice(self):
        """
        Description:
        > Gets appointment price. If no price was put, returns 0.
        :return: float
        """

        # Gets input
        inputPrice = self.entryPrice.get()

        # If the user didn't insert a price, return 0. Else, return value
        if inputPrice != '':
            price = eval(inputPrice)
            return price
        else:
            return 0

    def getsDate(self):
        """
        Description:
        > Gets the appointment date, validates it and returns it in a string.
        :return: Date in a string -> string
        """

        try:

            # Gets entries
            day = eval(self.entryDateDay.get())
            month = eval(self.entryDateMonth.get())
            year = eval(self.entryDateYear.get())

            # Creates a date
            appDate = datetime.date(year, month, day)

            # Checks if date is a today or a day after today. If not, throws an error
            if appDate < datetime.date.today():
                raise ValueError

            # Returns date in a string
            return appDate

        except:
            return ''

    def getsTime(self):
        """
        Description:
        > Gets the appointment time, validates it and returns it in a string.
        :return: time in a string -> string
        """

        try:

            # Gets entries
            hours = eval(self.entryTimeHours.get())
            minutes = eval(self.entryTimeMinutes.get())

            # Creates a time
            appTime = datetime.time(hours, minutes)

            # Returns time in a string
            return timeToString(appTime)

        except:
            return ''

    def getsServices(self):
        """
        Description:
        > Gets all the selected services and converts them in a string.
          If no services were selected, returns an empty string.
        :return: string of services
        """

        # Holds all the services provided
        selectedServices = []

        # Inserted all the selected services into the list
        if self.bath.get() == 1:
            selectedServices.append(services[1])
        if self.nails.get() == 1:
            selectedServices.append(services[2])
        if self.knot.get() == 1:
            selectedServices.append(services[3])
        if self.hygiene.get() == 1:
            selectedServices.append(services[4])
        if self.brushing.get() == 1:
            selectedServices.append(services[5])
        if self.haircut.get() == 1:
            selectedServices.append(services[6])
        if self.misc.get() == 1:
            selectedServices.append(services[7])

        return servicesToString(selectedServices)

    def displayAppointmentWindow(self, event):
        """
        Description:
        > Displays toplevel window with the information about the selected pet.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.treeApp.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:
            # Gets row information
            info = self.treeApp.item(item, 'values')

            # Since we only need the appointment id to query trough the database, we discard the rest
            appointmentID = info[0]

            # Creates toplevel window that will display the information about this appointment
            WindowAppointment(self, appointmentID)

    @staticmethod
    def validateNumber(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                float(valueIfAllowed)
                return True
            except ValueError:
                return False
        else:
            return True

    @staticmethod
    def validateString(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                float(valueIfAllowed)
                return False
            except ValueError:
                return True
        else:
            return True

    @staticmethod
    def validateDay(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                value = float(valueIfAllowed)
                if not 1 <= value <= 31:
                    raise ValueError
                return True
            except ValueError:
                return False
        else:
            return True

    @staticmethod
    def validateMonth(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                value = float(valueIfAllowed)
                if not 1 <= value < 13:
                    raise ValueError
                return True
            except ValueError:
                return False
        else:
            return True

    @staticmethod
    def validateYear(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                value = float(valueIfAllowed)
                if not value >= datetime.datetime.now().year:
                    raise ValueError
                return True
            except ValueError:
                return False
        else:
            return True

    @staticmethod
    def validateHours(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                value = float(valueIfAllowed)
                if not 1 <= value <= 24:
                    raise ValueError
                return True
            except ValueError:
                return False
        else:
            return True

    @staticmethod
    def validateMinutes(self, action, index, valueIfAllowed,
                       priorValue, text, validationType, triggerType):
        if valueIfAllowed != '':
            try:
                value = float(valueIfAllowed)
                if not 0 <= value <= 60:
                    raise ValueError
                return True
            except ValueError:
                return False
        else:
            return True

    def entryError(self):
        messagebox.showerror('Erro nas entradas', 'Os valores inseridos não são validos!', parent=self.window)
