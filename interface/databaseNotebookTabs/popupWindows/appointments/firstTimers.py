import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import interface
from database.src.functions.insertion import *
from database.src.utils.constants import typeOfAnimal, services
from database.src.utils.converters import servicesToString, timeToString, dateToString


class WindowFirstTimer(Toplevel):
    """
    Toplevel window that creates a first timer in our database. Creates a pet, client and an appointment.
    """

    def __init__(self, master):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Primeira vez')
        self.geometry("1000x500")
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates 3 small LabelFrame for each part of the description
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=500, width=333)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=500, width=333)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=500, width=334)

        # Puts everything on the screen
        self.petWindow.pack(side=LEFT, fill='both', expand=True)
        self.clientWindow.pack(side=LEFT, fill='both', expand=True)
        self.appointmentWindow.pack(side=LEFT, fill='both', expand=True)

        # Blocks resizing of our frames
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)
        self.appointmentWindow.grid_propagate(False)

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
        labelPetName.grid(row=0, column=0, padx=(5, 0), pady=30, sticky=W)
        labelPetType = Label(self.petWindow, text="Tipo:")
        labelPetType.grid(row=2, column=0, padx=(5, 0), pady=30, sticky=W)
        labelPetObservations = Label(self.petWindow, text="Observações:")
        labelPetObservations.grid(row=4, column=0, padx=5, pady=30, sticky=W)

        # Creates needed pet variables
        petName = StringVar()
        petType = StringVar()

        # Creates entries for pets
        self.entryPetName = Entry(self.petWindow, textvariable=petName)
        self.entryPetName.grid(column=1, row=0, padx=(0, 5), pady=10, sticky=W)
        self.entryPetType = Combobox(self.petWindow, textvariable=petType, state="readonly", values=typeOfAnimal)
        self.entryPetType.grid(column=1, row=2, padx=(0, 5), pady=10, sticky=W)
        self.entryPetObs = Text(self.petWindow, width=39, height=13)
        self.entryPetObs.grid(column=0, row=5, padx=5, pady=0, sticky=W, columnspan=2)

        # Creates separators to better organize our pets frame
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)

        # Creates labels to describe each entry field of the to be inserted client
        labelClientName = Label(self.clientWindow, text="Nome:")
        labelClientName.grid(row=0, column=0, padx=(5, 0), pady=30, sticky=W)
        labelClientPhone = Label(self.clientWindow, text="Telemóvel:")
        labelClientPhone.grid(row=2, column=0, padx=(5, 0), pady=30, sticky=W)

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

        # Creates labels to describe each entry field of the to be inserted appointment
        self.labelDate = Label(self.appointmentWindow, text='Data:')
        self.labelDate.grid(row=0, column=0, padx=5, pady=30, sticky=W)
        self.labelTime = Label(self.appointmentWindow, text='Hora:')
        self.labelTime.grid(row=2, column=0, padx=5, pady=30, sticky=W)
        self.labelPrice = Label(self.appointmentWindow, text='Preço:')
        self.labelPrice.grid(row=4, column=0, padx=5, pady=30, sticky=W)
        self.labelServices = Label(self.appointmentWindow, text='Serviços:')
        self.labelServices.grid(row=6, column=0, padx=5, pady=(30, 10), sticky=W)

        # Creates variables that hold the appointments' user input info
        appDateDay = StringVar()
        appDateMonth = StringVar()
        appDateYear = StringVar()
        appTimeHours = StringVar()
        appTimeMinutes = StringVar()
        appPrice = StringVar()

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
        self.entryCheckButtonBath.grid(row=0, column=0, padx=20, pady=5, sticky=W)
        self.entryCheckButtonNails = Checkbutton(self.services, text=services[1], variable=self.nails)
        self.entryCheckButtonNails.grid(row=1, column=0, padx=20, pady=5, sticky=W)
        self.entryCheckButtonKnot = Checkbutton(self.services, text=services[2], variable=self.knot)
        self.entryCheckButtonKnot.grid(row=2, column=0, padx=20, pady=5, sticky=W)
        self.entryCheckButtonHygiene = Checkbutton(self.services, text=services[3], variable=self.hygiene)
        self.entryCheckButtonHygiene.grid(row=3, column=0, padx=20, pady=5, sticky=W)
        self.entryCheckButtonBrushing = Checkbutton(self.services, text=services[4], variable=self.brushing)
        self.entryCheckButtonBrushing.grid(row=0, column=1, padx=20, pady=5, sticky=W)
        self.entryCheckButtonHaircut = Checkbutton(self.services, text=services[5], variable=self.haircut)
        self.entryCheckButtonHaircut.grid(row=1, column=1, padx=20, pady=5, sticky=W)
        self.entryCheckButtonMisc = Checkbutton(self.services, text=services[6], variable=self.misc)
        self.entryCheckButtonMisc.grid(row=2, column=1, padx=20, pady=5, sticky=W)

        # Selects the most provided services for convenience
        self.bath.set(1)
        self.haircut.set(1)

        # Creates separators to organize our UI
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=4)
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=4)
        Separator(self.appointmentWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=4)

        # Creates a submit button
        self.auxFrame = Frame(self.clientWindow, width=333, height=100)
        self.auxFrame.grid(column=0, row=4, padx=(7, 5), pady=212, columnspan=2, sticky=W)
        self.auxFrame.grid_propagate(False)
        self.submitBtt = Button(self.auxFrame, text="Submeter", width=38, command=self.submit)
        self.submitBtt.pack(side=LEFT, fill="both", expand=True, ipady=35)

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
            [petName, petType, petObs] = pet
            [clientName, clientPhone] = client
            [appServices, appDate, appTime, appPrice] = appointment

            # Creates a client in our database and gets his rowid
            clientID = insertRecordClient((clientName, '', clientPhone, '', ''))

            # Validates previous step. Is mainly done just to avoid errors
            if clientID is not None:

                # Creates a pet in our database and gets it's rowid
                petID = insertRecordAnimal((petName, petType, 0, '', '', petObs))

                # Validates previous step. Is mainly done just to avoid errors
                if petID is not None:

                    # Creates a link between the newly inserted client and pet
                    insertRecordPetClientLink((petID, clientID))

                    # Creates an appointment
                    insertRecordAppointment((appServices, appDate, appTime, appPrice, petID))

                    # Refreshes main tree
                    interface.databaseNotebookTabs.appointments.Appointments.refreshTree(self.master)

                    # Eliminates window
                    self.destroy()

    def getsPetEntries(self):
        """
        Description:
        > Gets all the entries to create a pet.
        :return: list of strings
        """

        # Gets values inside each entry
        petName = self.entryPetName.get()
        petType = self.entryPetType.get()
        petObs = self.entryPetObs.get('1.0', 'end')

        # Checks if required entries were inserted. If an error occurred, returns an empty string
        if petName != '' and petType != '':
            return [petName, petType, petObs]
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

        if appDate != '' and appTime != '' and appServices != '':
            return [appServices, appDate, appTime, appPrice]
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