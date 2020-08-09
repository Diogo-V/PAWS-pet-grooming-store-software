# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------- SERVICES ------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


class Service:
    """
    Represents a service provided by the store.
    """

    def __init__(self, description=None, price=None):
        """
        Service class constructor.
        :param description: type of service provided -> string
        :param price: price of the service -> double
        """
        self.description = description if description is not None else ''
        self.price = price if price is not None else 0

    def __repr__(self):
        """Unambiguous representation of our object. Used mainly for debugging purposes."""
        return f"Service({self.description}, {self.price})"

    def __str__(self):
        """Readable representation of our object. Used mainly to display our object to the user."""
        return f"Description: {self.description} | Price: {self.price}"

    def changeDescription(self, description):
        """
        Changes current service's description.
        :param description: new name for the service provided
        """
        self.description = description

    def changePrice(self, price):
        """
        Changes current service's price.
        :param price: new price for the service provided
        """
        self.price = price


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------- APPOINTMENTS ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


class Appointment:
    """
    Represents an appointment. It's composed of a list of services and a date of occurrence.
    """

    def __init__(self, services=None, dateOfAppointment=None, animal=None):
        """
        Appointment class constructor.
        :param services: services provided to the pet -> list of services
        :param dateOfAppointment: date when the service will be provided -> date
        :param animal: animal object that holds this appointment -> animal
        """
        self.services = services
        self.dateOfAppointment = dateOfAppointment
        self.animal = animal

    def __repr__(self):
        """Unambiguous representation of our object. Used mainly for debugging purposes."""
        return f"Service({self.services}, {self.dateOfAppointment})"

    def __str__(self):
        """Readable representation of our object. Used mainly to display our object to the user."""
        return f"List of services: {self.services} | Date: {self.dateOfAppointment} | Animal: {self.animal}"

    def changeDate(self, newDate):
        """
        Updates appointment date.
        :param newDate: new appointment date -> date
        """
        self.dateOfAppointment = newDate

    def changeAnimal(self, newAnimal):
        """
        Changes scheduled animal for this appointment.
        :param newAnimal: pets that now owns this appointment -> animal
        """
        self.animal = newAnimal
