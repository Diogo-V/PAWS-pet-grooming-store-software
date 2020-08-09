class Animal:
    """
    Represents an animal. It is going to be owned by one or more clients.
    """

    numberOfAnimals = 0  # Amount of animals within our program

    def __init__(self, name=None, owners=None, typeOfAnimal=None, weight=None, birthDate=None, history=None,
                 observations=None, appointment=None):
        """
        Animal class constructor.
        :param name: animal nickname -> string
        :param owners: clients which own the pet -> list of clients (owners)
        :param typeOfAnimal: type of animal -> string
        :param weight: animal's weight -> double
        :param birthDate: animal's birth date -> datetime
        :param history: record of all of the services (with dates) provided to the pet -> list of appointments
        :param observations: notes about the pet -> string
        :param appointment: set of services appointed to the pet -> list of appointments
        """
        self.name = name if name is not None else ''
        self.owners = owners if owners is not None else []
        self.typeOfAnimal = typeOfAnimal if typeOfAnimal is not None else ''
        self.weight = weight if weight is not None else 0
        self.birthDate = birthDate
        self.history = history if history is not None else 0  # Change this one
        self.observations = observations if observations is not None else ''
        self.appointment = appointment if history is not None else []
        Animal.numberOfAnimals += 1  # Since we created one more animal, we have to increment it

    def __repr__(self):
        """Unambiguous representation of our object. Used mainly for debugging purposes."""
        return f"Animal({self.name}, {self.owners}, {self.typeOfAnimal}, " \
               f"{self.weight}, {self.birthDate}, {self.history}, {self.observations})"

    def __str__(self):
        """Readable representation of our object. Used mainly to display our object to the user."""
        return f"Name: {self.name} | Owners: {self.owners} | History: {self.appointment}"

    def __len__(self):
        """Returns the amount of owners the pet has."""
        return len(self.owners)

    @classmethod
    def setNumberOfAnimals(cls, amount):
        """Updates numberOfAnimals class variable."""
        cls.numberOfAnimals = amount

    def addOwner(self, owner):
        """
        Associates a pet with a client.
        :param owner: client that hasn't been added to the owners list -> client
        """
        if owner not in self.owners:
            self.owners.append(owner)

    def removeOwner(self, owner):
        """
        Removes association between a pet and an owner.
        :param owner: client belonging to the owners list -> client
        """
        if owner in self.owners:
            self.owners.remove(owner)

    def addHistory(self, record):
        """
        Adds a record of the service provided to the pet.
        :param record: service provided to the pet -> service
        """
        self.history.append(record)

    def removeHistory(self, record):
        """
        Removes a record of a service provided to the pet.
        :param record: service provided to the pet -> service
        """
        self.history.remove(record)

    def changeHistory(self, oldRecord, newRecord):
        """
        Changes the record of a previously provided service.
        :param oldRecord: record that is going to be substituted -> appointment
        :param newRecord: record that is going to substitute -> appointment
        """
        self.removeAppointment(oldRecord)
        self.addAppointment(newRecord)

    def addAppointment(self, appointment):
        """
        Adds a future appointment for the pet.
        :param appointment: combo of service + date that is going to be provided to the pet -> appointment
        """
        self.appointment.append(appointment)

    def removeAppointment(self, appointment):
        """
        Removes a future appointment for the pet.
        :param appointment: combo of service + date that is going to be provided to the pet -> appointment
        """
        self.appointment.remove(appointment)

    def changeAppointment(self, oldAppointment, newAppointment):
        """
        Changes an appointment to a different one.
        :param oldAppointment: appointment that is going to be substituted -> appointment
        :param newAppointment: appointment that is going to substitute -> appointment
        """
        self.removeAppointment(oldAppointment)
        self.addAppointment(newAppointment)

    def changeName(self, newName):
        """
        Changes the name of a pet.
        :param newName: new name of the pet -> string
        """
        self.name = newName

    def changeTypeOfAnimal(self, newType):
        """
        Changes the description of the type of pet.
        :param newType: description of the new type of animal -> string
        """
        self.typeOfAnimal = newType

    def changeWeight(self, newWeight):
        """
        Changes weight of the pet.
        :param newWeight: updated weight of the pet -> double
        """
        self.weight = newWeight

    def changeBirthDate(self, newDate):
        """
        Changes the birth date of the pet.
        :param newDate: updated birth date of the pet -> date
        """
        self.birthDate = newDate

    def changeObservations(self, newObservation=''):
        """
        Changes recorded observations of the pet.
        :param newObservation: updated observation of the pet -> string
        """
        self.observations = newObservation
