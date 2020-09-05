from datetime import date, time, datetime
from operator import itemgetter

import interface
from database.src.functions.insertion import insertRecordAppointment
from database.src.query.databaseNotebookTabs.appointments import getsRequestedPets, getsPetsForAppointmentsWindow
from database.src.utils.constants import *
from database.src.utils.converters import dateToString, timeToString, servicesToString
from interface.databaseNotebookTabs.popupWindows.pets.information import WindowPet
from interface.rootNotebookTabs.popupWindows.appointments.information import *


class WindowInsertAppointment(Toplevel):
    """
    Toplevel window used to insert a new appointment in the database.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: root window where is going to be inserted -> notebook
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Inserir marcação')
        self.geometry("1000x500")
        self.resizable(False, False)
        self.transient(master)

        # Creates tab main window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates two labelFrames to organize our UI
        self.appointmentWindow = LabelFrame(self.window, text=' Marcação ', height=500, width=500)
        self.petWindow = LabelFrame(self.window, text=' Animal associado á marcação ', height=400, width=500)
        self.appointmentWindow.pack(side=LEFT, fill="both", expand=True)
        self.petWindow.pack(side=TOP, fill="both", expand=True)

        # Blocks resizing for each labelFrame
        self.appointmentWindow.grid_propagate(False)
        self.petWindow.grid_propagate(False)

        # Creates a submit button
        self.createAppointment = Button(self.window, text='Submter', command=self.submit)
        self.createAppointment.pack(side=BOTTOM, padx=5, pady=5, expand=True, fill="both")

        # Creates labels to describe each of the entries
        self.labelDate = Label(self.appointmentWindow, text='Data:')
        self.labelDate.grid(row=0, column=0, padx=5, pady=30, sticky=W)
        self.labelTime = Label(self.appointmentWindow, text='Hora:')
        self.labelTime.grid(row=2, column=0, padx=5, pady=30, sticky=W)
        self.labelPrice = Label(self.appointmentWindow, text='Preço:')
        self.labelPrice.grid(row=4, column=0, padx=5, pady=30, sticky=W)
        self.labelServices = Label(self.appointmentWindow, text='Serviços:')
        self.labelServices.grid(row=6, column=0, padx=5, pady=30, sticky=W)

        # Creates variables that hold the appointments' user input info
        appDateDay = StringVar()
        appDateMonth = StringVar()
        appDateYear = StringVar()
        appTimeHours = StringVar()
        appTimeMinutes = StringVar()
        appPrice = StringVar()

        # Restriction commands
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateDay = (master.register(self.validateDay), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMonth = (master.register(self.validateMonth), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateYear = (master.register(self.validateYear), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateHours = (master.register(self.validateHours), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMinutes = (master.register(self.validateMinutes), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Creates entries to get the information from the user
        self.entryDateDay = Entry(self.appointmentWindow, textvariable=appDateDay, validate="focusout",
                                  validatecommand=validateDay, invalidcommand=self.entryError, width=4)
        self.entryDateDay.grid(row=0, column=1, padx=5, pady=10)
        self.entryDateMonth = Entry(self.appointmentWindow, textvariable=appDateMonth, validate="focusout",
                                    validatecommand=validateMonth, invalidcommand=self.entryError, width=4)
        self.entryDateMonth.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.entryDateYear = Entry(self.appointmentWindow, textvariable=appDateYear, validate="focusout",
                                   validatecommand=validateYear, invalidcommand=self.entryError, width=6)
        self.entryDateYear.grid(row=0, column=3, padx=(5, 300), pady=10)
        self.entryTimeHours = Entry(self.appointmentWindow, textvariable=appTimeHours, validate="focusout",
                                    validatecommand=validateHours, invalidcommand=self.entryError, width=4)
        self.entryTimeHours.grid(row=2, column=1, padx=5, pady=10)
        self.entryTimeMinutes = Entry(self.appointmentWindow, textvariable=appTimeMinutes, validate="focusout",
                                      validatecommand=validateMinutes, invalidcommand=self.entryError, width=4)
        self.entryTimeMinutes.grid(row=2, column=2, padx=5, pady=10)
        self.entryPrice = Entry(self.appointmentWindow, textvariable=appPrice, validate="focusout",
                                validatecommand=validateNumber, invalidcommand=self.entryError, width=10)
        self.entryPrice.grid(row=4, column=1, padx=5, pady=10, columnspan=2)

        # Creates a frame to insert our services. Mainly used to organize the UI
        self.services = Frame(self.appointmentWindow)
        self.services.grid(row=7, column=0, columnspan=4, padx=(5, 100), pady=5, sticky=W)

        # Separates entries for the date
        Label(self.appointmentWindow, text='/').grid(column=1, row=0, padx=(57, 0))
        Label(self.appointmentWindow, text='/').grid(column=2, row=0, padx=(47, 0))

        # Separates hours from minutes
        Label(self.appointmentWindow, text='  :').grid(column=1, row=2, padx=(50, 0))

        # Creates variables that hold our provided services. Hold 1 if selected and 0 if not
        self.bath = IntVar()
        self.nails = IntVar()
        self.knot = IntVar()
        self.hygiene = IntVar()
        self.brushing = IntVar()
        self.haircut = IntVar()
        self.misc = IntVar()

        # Creates checkboxes to input our selected services
        self.entryCheckButtonBath = Checkbutton(self.services, text=services[0], variable=self.bath)
        self.entryCheckButtonBath.grid(row=0, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonNails = Checkbutton(self.services, text=services[1], variable=self.nails)
        self.entryCheckButtonNails.grid(row=1, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonKnot = Checkbutton(self.services, text=services[2], variable=self.knot)
        self.entryCheckButtonKnot.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHygiene = Checkbutton(self.services, text=services[3], variable=self.hygiene)
        self.entryCheckButtonHygiene.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonBrushing = Checkbutton(self.services, text=services[4], variable=self.brushing)
        self.entryCheckButtonBrushing.grid(row=0, column=2, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHaircut = Checkbutton(self.services, text=services[5], variable=self.haircut)
        self.entryCheckButtonHaircut.grid(row=1, column=2, padx=20, pady=10, sticky=W)
        self.entryCheckButtonMisc = Checkbutton(self.services, text=services[6], variable=self.misc)
        self.entryCheckButtonMisc.grid(row=0, column=3, padx=20, pady=10, sticky=W)

        # Selects the most provided services for convenience
        self.bath.set(1)
        self.haircut.set(1)

        # Creates separators to organize our UI
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=4)
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=4)
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=4)

        # Creates variables so that we have a place to store our input information
        petName = StringVar()
        petType = StringVar()

        # Creates search entry for pets
        self.labelPetName = Label(self.petWindow, text='Nome:')
        self.labelPetName.grid(column=0, row=0, padx=(5, 0), pady=(20, 10), sticky=W)
        self.entryPetName = Entry(self.petWindow, textvariable=petName, width=20)
        self.entryPetName.grid(column=1, row=0, pady=(20, 10), sticky=W)
        self.labelPetType = Label(self.petWindow, text='Tipo:')
        self.labelPetType.grid(column=2, row=0, padx=(5, 0), pady=(20, 10), sticky=W)
        self.boxPetType = Combobox(self.petWindow, textvariable=petType, state="readonly",
                                   values=[''] + typeOfAnimal, width=10)
        self.boxPetType.grid(column=3, row=0, padx=(5, 0), pady=(20, 10), sticky=W)

        # Creates search buttons for the pets tree
        self.petButton = Button(self.petWindow, text='Procurar', width=8, command=self.updatePetTree)
        self.petButton.grid(column=4, row=0, pady=(20, 10), sticky=E)

        # Creates tree that will display all the pets
        self.tree = Treeview(self.petWindow, columns=(0, 1, 2), height=15)
        self.tree.grid(column=0, row=1, columnspan=5, padx=10, pady=10)

        # Formats columns
        self.tree.column("#0", stretch=NO, anchor='center', width=0)
        self.tree.column(0, stretch=NO, anchor='center', width=0)
        self.tree.column(1, stretch=NO, anchor='center', width=225)
        self.tree.column(2, stretch=NO, anchor='center', width=225)

        # Define columns heading
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading(0, text='', anchor='w')
        self.tree.heading(1, text='Nome', anchor='center')
        self.tree.heading(2, text='Tipo', anchor='center')

        # Creates a scrollbar for the tree view and then puts it on the screen
        self.scrollbarClients = Scrollbar(self.petWindow, orient="vertical", command=self.tree.yview)
        self.scrollbarClients.grid(column=6, row=1, sticky=(N, S))
        self.tree.configure(yscrollcommand=self.scrollbarClients.set)

        # Populates tree
        self.refreshTreePets()

        # Links double click on a row with a window popup
        self.tree.bind('<Double 1>', self.displayAppointmentWindow)

    def submit(self):
        """
        Description:
        > Inserts an appointment in the database. Gets required info and links it to a pet.
        """

        # Gets tuple with the selected pet
        appSelectedPet = self.tree.selection()

        # If the user selected more than one pet. Throws error and interrupts
        if len(appSelectedPet) != 1:
            messagebox.showerror("Erro", "Selecione apenas uma animal antes de continuar!", parent=self.window)
            return

        # Gets selected services
        appServices = self.getsServices()

        # Checks if the user selected a pet and a set of services. If not, throws an error
        if appSelectedPet != () and appServices != []:

            # Gets confirmation from user
            msg = messagebox.askyesno('Confirmar submissão', 'Deseja inserir a marcação?', parent=self.window)

            # If the user said yes, proceed
            if msg:

                # Gets needed values
                appDate = self.getsDate()
                appTime = self.getsTime()
                appPrice = self.getsPrice()
                appPetID = self.tree.item(appSelectedPet[0], "values")[0]

                # Validates date
                if appDate == '' or appTime == '':
                    messagebox.showerror('Erro', 'Insira uma data valida antes de prosseguir!', parent=self.window)
                    return

                # Validates time
                if appTime == '':
                    messagebox.showerror('Erro', 'Hora invalida! Insira uma nova hora', parent=self.window)
                    return

                # Creates info that is going to be inserted
                info = (appServices, appDate, appTime, appPrice, appPetID)

                # Creates appointment with the provided info
                insertRecordAppointment(info)

                # Refreshes main tree
                interface.databaseNotebookTabs.appointments.Appointments.refreshTree(self.master)

                # Eliminates window
                self.destroy()

        else:
            messagebox.showerror('Erro', 'Selecione um animal e/ou serviços antes de prosseguir!', parent=self.window)

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
            return eval(inputPrice)
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
            appDate = date(year, month, day)

            # Checks if date is a today or a day after today. If not, throws an error
            if appDate < date.today():
                raise ValueError

            # Returns date in a string
            return dateToString(appDate)

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
            appTime = time(hours, minutes)

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
            selectedServices.append(services[0])
        if self.nails.get() == 1:
            selectedServices.append(services[1])
        if self.knot.get() == 1:
            selectedServices.append(services[2])
        if self.hygiene.get() == 1:
            selectedServices.append(services[3])
        if self.brushing.get() == 1:
            selectedServices.append(services[4])
        if self.haircut.get() == 1:
            selectedServices.append(services[5])
        if self.misc.get() == 1:
            selectedServices.append(services[6])

        return servicesToString(selectedServices)

    def getsPetEntries(self):
        """
        Description:
        > Gets information inserted inside our entries.

        :return: list containing such info -> list of strings
        """
        return [self.entryPetName.get(), self.boxPetType.get()]

    def refreshTreePets(self):
        """
        Description:
        > Gets all the default values for the corresponding tree.
        """

        # Gets default values for pets
        rows = getsPetsForAppointmentsWindow()

        # Displays rows
        self.displayTreePetsRows(rows)

    def displayTreePetsRows(self, rows):
        """
        Description:
        > Sorts rows according to pets's name and displays them on the screen.

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
        > Displays toplevel window with the information about the selected pet.

        :param event: event of clicking a button -> event
        """

        # Gets row that was clicked
        item = self.tree.identify_row(event.y)

        # If the user didn't click on a blank space, shows the toplevel window else, does nothing
        if item:
            # Gets row information
            info = self.tree.item(item, 'values')

            # Since we only need the pet id to query trough the database, we discard the rest
            petID = info[0]

            # Creates toplevel window that will display the information about this pet
            WindowPet(self, petID)

    def updatePetTree(self):
        """
        Description:
        > Gets values inside our search entries and gets rows that are going to be displayed.
        """

        # Gets entries for clients
        [petName, petType] = self.getsPetEntries()

        # If no information was typed, just refresh the page
        if petName == '' and petType == '':
            self.refreshTreePets()
        else:

            # Gets requested rows
            rows = getsRequestedPets([petName, petType])

            # Displays information on our tree
            self.displayTreePetsRows(rows)

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
                if not value >= datetime.now().year:
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
