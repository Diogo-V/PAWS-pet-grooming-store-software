import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from database.src.functions.update import updateRecordAnimal, updateRecordClient, updateRecordAppointment
from database.src.query.rootNotebookTabs.appointments import getsInfoForAppointmentsWindow
from database.src.utils.constants import *
from database.src.utils.converters import *


class WindowUpdateAppointment(Toplevel):
    """
    Toplevel window that allows the refactoring of all the information about this appointment.
    """

    def __init__(self, master, appointmentID, root):
        """
        Description:
        > Creates our window.

        :param master: Frame window where is going to be inserted -> Frame
        :param appointmentID: appointment rowid inside the database -> integer
        :param root: Main application frame window -> Frame
        """

        # Creates toplevel window that will be displayed. Sets size and blocks resize
        Toplevel.__init__(self, master)
        self.title('Alterar informações sobre a marcação')
        self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='images/paw.ico'))  # Puts icon
        self.geometry("1250x600")
        self.resizable(False, False)

        # Creates frame (used to put widgets in it) for our toplevel window and puts it on the screen
        self.window = Frame(self, height=500, width=1000)
        self.window.pack(fill='both', expand=True)

        # Creates a root variable so that we can access the main application window
        self.root = root
        self.master = master
        self.appointmentID = appointmentID

        # Creates 3 small LabelFrame for each part of the description. Used to organize the information
        self.petWindow = LabelFrame(self.window, text=' Sobre o animal ', height=600, width=416)
        self.clientWindow = LabelFrame(self.window, text=' Sobre o cliente ', height=600, width=416)
        self.appointmentWindow = LabelFrame(self.window, text=' Sobre a marcação ', height=600, width=417)
        self.petWindow.pack(side=LEFT, fill='both', expand=True)
        self.clientWindow.pack(side=LEFT, fill='both', expand=True)
        self.appointmentWindow.pack(side=LEFT, fill='both', expand=True)

        # Blocks resizing for each labelFrame
        self.petWindow.grid_propagate(False)
        self.clientWindow.grid_propagate(False)
        self.appointmentWindow.grid_propagate(False)

        # Restriction commands
        validateNumber = (master.register(self.validateNumber), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateDay = (master.register(self.validateDay), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMonth = (master.register(self.validateMonth), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateYear = (master.register(self.validateYear), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateHours = (master.register(self.validateHours), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        validateMinutes = (master.register(self.validateMinutes), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Gets a list containing the information that is going to be displayed
        self.information = getsInfoForAppointmentsWindow(appointmentID)

        # Gets and filters information about the pet, owner and appointment from the information list
        [self.petID, self.petName, self.petType, self.petBreed, self.petGender, self.petWeight, self.petHairType,
         self.petHairColor, self.petAge, self.petObs] = self.getsPetInfo()
        [self.clientID, self.clientName, self.clientEmail,
         self.clientPhone, self.clientNIF, self.clientAdr] = self.getsClientInfo()
        [self.appServices, self.appDate, self.appTime, self.appPrice, self.appObs] = self.getsAppointmentInfo()

        # Formats input into something that can be put inside each entry
        self.appDate = stringToDate(self.appDate)
        self.appTime = stringToTime(self.appTime)
        self.appServices = stringToServices(self.appServices)

        # Creates 2 separate frames inside our appointments frames. Used to organize our UI
        self.frmAppInputs = Frame(self.appointmentWindow, height=600, width=412, borderwidth=2, relief=RIDGE)
        self.frmAppServices = Frame(self.appointmentWindow, height=600, width=412, borderwidth=2, relief=RIDGE)
        self.frmAppInputs.pack(side=TOP, fill='both', expand=True, pady=(0, 5), padx=5)
        self.frmAppServices.pack(side=BOTTOM, fill='both', expand=True, pady=(0, 5), padx=5)

        # Creates a frame to insert our services. Mainly used to organize the UI
        self.services = Frame(self.frmAppServices)
        self.services.grid(row=1, column=0, columnspan=4, padx=(5, 100), sticky=W)

        # Creates labels that will describe each field in each section and puts the requested information after it
        descPetName = Label(self.petWindow, text=f'Nome:')
        descPetName.grid(column=0, row=0, sticky=W, pady=15)
        descPetType = Label(self.petWindow, text=f'Tipo:')
        descPetType.grid(column=0, row=2, sticky=W, pady=15)
        descPetBreed = Label(self.petWindow, text=f'Raça:')
        descPetBreed.grid(column=0, row=4, sticky=W, pady=15)
        descPetGender = Label(self.petWindow, text=f'Sexo:')
        descPetGender.grid(column=0, row=6, sticky=W, pady=15)
        descPetWeight = Label(self.petWindow, text=f'Peso:')
        descPetWeight.grid(column=0, row=8, sticky=W, pady=15)
        descPetHairType = Label(self.petWindow, text=f'Pelo:')
        descPetHairType.grid(column=0, row=10, sticky=W, pady=15)
        descPetHairColor = Label(self.petWindow, text=f'Cor:')
        descPetHairColor.grid(column=0, row=12, sticky=W, pady=15)
        descPetAge = Label(self.petWindow, text=f'Idade:')
        descPetAge.grid(column=0, row=14, sticky=W, pady=15)
        descPetObs = Label(self.petWindow, text=f'Observações:')
        descPetObs.grid(column=0, row=16, sticky=W, pady=15)

        descClientName = Label(self.clientWindow, text=f'Nome:')
        descClientName.grid(column=0, row=0, sticky=W, pady=15)
        descClientEmail = Label(self.clientWindow, text=f'Email:')
        descClientEmail.grid(column=0, row=2, sticky=W, pady=15)
        descClientPhone = Label(self.clientWindow, text=f'Telemóvel:')
        descClientPhone.grid(column=0, row=4, sticky=W, pady=15)
        descClientNIF = Label(self.clientWindow, text=f'NIF:')
        descClientNIF.grid(column=0, row=6, sticky=W, pady=15)
        descClientAddress = Label(self.clientWindow, text=f'Morada:')
        descClientAddress.grid(column=0, row=8, sticky=W, pady=15)

        # Creates labels to describe each of the entries
        descAppDate = Label(self.frmAppInputs, text='Data:')
        descAppDate.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        descAppTime = Label(self.frmAppInputs, text='Hora:')
        descAppTime.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        descAppPrice = Label(self.frmAppInputs, text='Preço:')
        descAppPrice.grid(row=4, column=0, padx=5, pady=10, sticky=W)
        descAppObservations = Label(self.frmAppInputs, text='Observações:')
        descAppObservations.grid(row=6, column=0, padx=5, pady=10, sticky=W)
        descAppServices = Label(self.frmAppServices, text='Serviços:')
        descAppServices.grid(row=0, column=0, padx=(23, 5), pady=10, sticky=W)

        # Creates all the needed text variables for the entries
        self.varPetName = StringVar()
        self.varPetType = StringVar()
        self.varPetBreed = StringVar()
        self.varPetGender = StringVar()
        self.varPetWeight = StringVar()
        self.varPetHairType = StringVar()
        self.varPetHairColor = StringVar()
        self.varPetAge = StringVar()

        self.varClientName = StringVar()
        self.varClientEmail = StringVar()
        self.varClientPhone = StringVar()
        self.varClientNif = StringVar()
        self.varClientAddress = StringVar()

        self.varAppDateDay = StringVar()
        self.varAppDateMonth = StringVar()
        self.varAppDateYear = StringVar()
        self.varAppTimeHours = StringVar()
        self.varAppTimeMinutes = StringVar()
        self.varAppPrice = StringVar()

        # Creates all the needed entries
        self.entryPetName = Entry(self.petWindow, width=20, textvariable=self.varPetName)
        self.entryPetName.grid(column=1, row=0, sticky=W, pady=15, padx=(0, 100))
        self.entryPetType = Combobox(self.petWindow, textvariable=self.varPetType,
                                     state="readonly", values=typeOfAnimal, width=19)
        self.entryPetType.grid(column=1, row=2, sticky=W, pady=15, padx=(0, 100))
        self.entryPetBreed = Entry(self.petWindow, width=20, textvariable=self.varPetBreed)
        self.entryPetBreed.grid(column=1, row=4, sticky=W, pady=15, padx=(0, 100))
        self.entryPetGender = Combobox(self.petWindow, textvariable=self.varPetGender,
                                       state="readonly", values=gender, width=19)
        self.entryPetGender.grid(column=1, row=6, sticky=W, pady=15, padx=(0, 100))
        self.entryPetWeight = Entry(self.petWindow, width=20, textvariable=self.varPetWeight)
        self.entryPetWeight.grid(column=1, row=8, sticky=W, pady=15, padx=(0, 100))
        self.entryPetHairType = Combobox(self.petWindow, textvariable=self.varPetHairType,
                                         state="readonly", values=typeOfHair, width=19)
        self.entryPetHairType.grid(column=1, row=10, sticky=W, pady=15, padx=(0, 100))
        self.entryPetHairColor = Entry(self.petWindow, width=20, textvariable=self.varPetHairColor)
        self.entryPetHairColor.grid(column=1, row=12, sticky=W, pady=15, padx=(0, 100))
        self.entryPetAge = Entry(self.petWindow, width=20, textvariable=self.varPetAge)
        self.entryPetAge.grid(column=1, row=14, sticky=W, pady=15, padx=(0, 100))
        self.entryPetObs = Text(self.petWindow, width=49, height=5)
        self.entryPetObs.grid(column=0, row=17, padx=(5, 50), pady=0, sticky=W, columnspan=2)

        self.entryClientName = Entry(self.clientWindow, width=20, textvariable=self.varClientName)
        self.entryClientName.grid(column=1, row=0, sticky=W, pady=15, padx=(35, 50))
        self.entryClientEmail = Entry(self.clientWindow, width=20, textvariable=self.varClientEmail)
        self.entryClientEmail.grid(column=1, row=2, sticky=W, pady=15, padx=(35, 50))
        self.entryClientPhone = Entry(self.clientWindow, width=20, textvariable=self.varClientPhone)
        self.entryClientPhone.grid(column=1, row=4, sticky=W, pady=15, padx=(35, 50))
        self.entryClientNIF = Entry(self.clientWindow, width=20, textvariable=self.varClientNif)
        self.entryClientNIF.grid(column=1, row=6, sticky=W, pady=15, padx=(35, 50))
        self.entryClientAddress = Entry(self.clientWindow, width=20, textvariable=self.varClientAddress)
        self.entryClientAddress.grid(column=1, row=8, sticky=W, pady=15, padx=(35, 50))

        self.entryAppDateDay = Entry(self.frmAppInputs, textvariable=self.varAppDateDay, validate="focusout",
                                     validatecommand=validateDay, invalidcommand=self.entryError, width=4)
        self.entryAppDateDay.grid(row=0, column=1, padx=5, pady=10)
        self.entryAppDateMonth = Entry(self.frmAppInputs, textvariable=self.varAppDateMonth, validate="focusout",
                                       validatecommand=validateMonth, invalidcommand=self.entryError, width=4)
        self.entryAppDateMonth.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.entryAppDateYear = Entry(self.frmAppInputs, textvariable=self.varAppDateYear, validate="focusout",
                                      validatecommand=validateYear, invalidcommand=self.entryError, width=6)
        self.entryAppDateYear.grid(row=0, column=3, padx=(5, 200), pady=10)
        self.entryAppTimeHours = Entry(self.frmAppInputs, textvariable=self.varAppTimeHours, validate="focusout",
                                       validatecommand=validateHours, invalidcommand=self.entryError, width=4)
        self.entryAppTimeHours.grid(row=2, column=1, padx=5, pady=10)
        self.entryAppTimeMinutes = Entry(self.frmAppInputs, textvariable=self.varAppTimeMinutes, validate="focusout",
                                         validatecommand=validateMinutes, invalidcommand=self.entryError, width=4)
        self.entryAppTimeMinutes.grid(row=2, column=2, padx=5, pady=10)
        self.entryAppPrice = Entry(self.frmAppInputs, textvariable=self.varAppPrice, validate="focusout",
                                   validatecommand=validateNumber, invalidcommand=self.entryError, width=10)
        self.entryAppPrice.grid(row=4, column=1, padx=5, pady=10, columnspan=2)
        self.entryAppObs = Text(self.frmAppInputs, width=48, height=10)
        self.entryAppObs.grid(column=0, row=7, sticky=W, columnspan=4, padx=5)

        # Separates entries for the date
        Label(self.frmAppInputs, text='/').grid(column=1, row=0, padx=(57, 0))
        Label(self.frmAppInputs, text='/').grid(column=2, row=0, padx=(47, 0))

        # Separates hours from minutes
        Label(self.frmAppInputs, text='  :').grid(column=1, row=2, padx=(50, 0))

        # Inserts the current values inside each entry
        self.entryPetName.insert(END, self.petName)
        self.entryPetType.current(typeOfAnimal.index(self.petType))
        self.entryPetBreed.insert(END, self.petBreed)
        self.entryPetGender.current(gender.index(self.petGender))
        self.entryPetWeight.insert(END, self.petWeight)
        self.entryPetHairType.current(typeOfHair.index(self.petHairType))
        self.entryPetHairColor.insert(END, self.petHairColor)
        self.entryPetAge.insert(END, self.petAge)
        self.entryPetObs.insert(END, self.petObs)

        self.entryClientName.insert(END, self.clientName)
        self.entryClientEmail.insert(END, self.clientEmail)
        self.entryClientPhone.insert(END, self.clientPhone)
        self.entryClientNIF.insert(END, self.clientNIF)
        self.entryClientAddress.insert(END, self.clientAdr)

        self.entryAppDateDay.insert(END, str(self.appDate.day))
        self.entryAppDateMonth.insert(END, str(self.appDate.month))
        self.entryAppDateYear.insert(END, str(self.appDate.year))
        self.entryAppTimeHours.insert(END, str(self.appTime.hour))
        self.entryAppTimeMinutes.insert(END, str(self.appTime.minute))
        self.entryAppPrice.insert(END, str(self.appPrice))
        self.entryAppObs.insert(END, str(self.appObs))

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
        self.entryCheckButtonKnot.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHygiene = Checkbutton(self.services, text=services[3], variable=self.hygiene)
        self.entryCheckButtonHygiene.grid(row=3, column=0, padx=20, pady=10, sticky=W)
        self.entryCheckButtonBrushing = Checkbutton(self.services, text=services[4], variable=self.brushing)
        self.entryCheckButtonBrushing.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonHaircut = Checkbutton(self.services, text=services[5], variable=self.haircut)
        self.entryCheckButtonHaircut.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        self.entryCheckButtonMisc = Checkbutton(self.services, text=services[6], variable=self.misc)
        self.entryCheckButtonMisc.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # Sets all the checkButtons that are currently inside our provided services
        self.setsServices()

        # Creates separators so that we can organize the window more efficiently
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=9, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=11, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=13, sticky=(W, E), columnspan=2)
        Separator(self.petWindow, orient=HORIZONTAL).grid(column=0, row=15, sticky=(W, E), columnspan=2)

        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=2)
        Separator(self.clientWindow, orient=HORIZONTAL).grid(column=0, row=7, sticky=(W, E), columnspan=2)

        Separator(self.frmAppInputs, orient=HORIZONTAL).grid(column=0, row=1, sticky=(W, E), columnspan=5)
        Separator(self.frmAppInputs, orient=HORIZONTAL).grid(column=0, row=3, sticky=(W, E), columnspan=5)
        Separator(self.frmAppInputs, orient=HORIZONTAL).grid(column=0, row=5, sticky=(W, E), columnspan=5)

        # Creates a button to update all the information. Also creates a frame to help expand it
        auxFrame = Frame(self.clientWindow, borderwidth=2, relief=SUNKEN, width=300, height=200)
        auxFrame.grid(row=9, column=0, sticky=(W, S, E, N), columnspan=4, padx=(6, 200), pady=(120, 0))
        auxFrame.grid_propagate(False)
        self.bttUpdate = Button(auxFrame, text='Atualizar', width=48, command=self.updateEntries)
        self.bttUpdate.pack(side=BOTTOM, fill='both', expand=True, ipady=40)

    def updateEntries(self):
        """
        Description:
        > Gets all the values inside each entry and updates their values.
        """

        # Ask confirmation from the user
        msg = messagebox.askyesno("Confirmar", "Deseja atualizar a informação?", parent=self.window)

        if msg:

            # Gets pet values
            pet = self.getsPetEntries()

            # Checks if an error occurred while creating a pet
            if pet != ():

                # Gets client values
                client = self.getsClientEntries()

                if client != ():

                    # Gets appointment values
                    appointment = self.getsAppointmentEntries()

                    if appointment != ():

                        # Updates all the information
                        updateRecordAnimal(pet, self.petID)
                        updateRecordClient(client, self.clientID)
                        updateRecordAppointment(appointment, self.appointmentID)

                        # Refreshes all trees of our application
                        self.root.refreshApplication()

                        # Destroys this window and the one behind
                        self.master.destroy()

                    else:
                        messagebox.showerror("Erro", "Aconteceu um erro na atualização da marcação! "
                                                     "Pode ter surgido porque não tem as entradas necessárias!",
                                             parent=self.window)

                else:
                    messagebox.showerror("Erro", "Aconteceu um erro na atualização do cliente! "
                                                 "Pode ter surgido porque não tem as entradas necessárias!",
                                         parent=self.window)

            else:
                messagebox.showerror("Erro", "Aconteceu um erro na atualização do animal! "
                                             "Pode ter surgido porque não tem as entradas necessárias!",
                                     parent=self.window)

    def getsPetInfo(self):
        """Gets and filters information about the pet from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][0:10]

    def getsClientInfo(self):
        """Gets and filters information about the client from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][10:16]

    def getsAppointmentInfo(self):
        """Gets and filters information about the appointments from the information list.
           We use a zero to only get the first owner of the pet."""
        return self.information[0][16:21]

    def getsPetEntries(self):
        """
        Description:
        > Gets values inside each entry to update our pet. Also checks if required values were inserted.

        :return: tuple containing all the inserted info -> tuple of strings
        """

        # Gets entries
        petName = self.entryPetName.get()
        petType = self.entryPetType.get()
        petBreed = self.entryPetBreed.get()
        petGender = self.entryPetGender.get()
        petWeight = self.entryPetWeight.get()
        petHairType = self.entryPetHairType.get()
        petHairColor = self.entryPetHairColor.get()
        petAge = self.entryPetAge.get()
        petObs = self.entryPetObs.get('1.0', 'end')

        # Formats values
        petWeight = eval(petWeight) if petWeight != '' else 0
        petAge = eval(petAge) if petAge != '' else 0

        # Checks if required values were inserted and returns them if so
        if petName != '' and petType != '':
            return petName, petType, petBreed, petGender, petWeight, petHairType, petHairColor, petAge, petObs
        else:
            return ()

    def getsClientEntries(self):
        """
        Description:
        > Gets values inside each entry to update our client. Also checks if required values were inserted.

        :return: tuple containing all the inserted info -> tuple of strings
        """

        # Gets entries
        clientName = self.entryClientName.get()
        clientEmail = self.entryClientEmail.get()
        clientPhone = self.entryClientPhone.get()
        clientNIF = self.entryClientNIF.get()
        clientAddress = self.entryClientAddress.get()

        # Formats values before going to the database
        clientNIF = eval(clientNIF) if clientNIF != '' else 0
        clientPhone = eval(clientPhone) if clientPhone != '' else 0

        # Checks if required values were inserted and returns them if so
        if clientName != '' and clientPhone != 0:
            return clientName, clientEmail, clientPhone, clientNIF, clientAddress
        else:
            return ()

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
        appObs = self.entryAppObs.get('1.0', 'end')

        if appDate != '' and appTime != '' and appServices != '':
            return appServices, appDate, appTime, appPrice, appObs, self.petID
        else:
            return ()

    def getsPrice(self):
        """
        Description:
        > Gets appointment price. If no price was put, returns 0.
        :return: float
        """

        # Gets input
        inputPrice = self.entryAppPrice.get()

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
            day = eval(self.entryAppDateDay.get())
            month = eval(self.entryAppDateMonth.get())
            year = eval(self.entryAppDateYear.get())

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
            hours = eval(self.entryAppTimeHours.get())
            minutes = eval(self.entryAppTimeMinutes.get())

            # Creates a time
            appTime = datetime.time(hours, minutes)

            # Returns time in a string
            return timeToString(appTime)

        except:
            return ''

    def setsServices(self):
        """
        Description:
        > Turns on all the currently provided services.
        """

        # Inserted all the selected services into the list
        if self.entryCheckButtonBath.cget("text") in self.appServices:
            self.bath.set(1)
        if self.entryCheckButtonNails.cget("text") in self.appServices:
            self.nails.set(1)
        if self.entryCheckButtonKnot.cget("text") in self.appServices:
            self.knot.set(1)
        if self.entryCheckButtonHygiene.cget("text") in self.appServices:
            self.hygiene.set(1)
        if self.entryCheckButtonBrushing.cget("text") in self.appServices:
            self.brushing.set(1)
        if self.entryCheckButtonHaircut.cget("text") in self.appServices:
            self.haircut.set(1)
        if self.entryCheckButtonMisc.cget("text") in self.appServices:
            self.misc.set(1)

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
                if not datetime.datetime.now().year <= value <= 9999:
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
