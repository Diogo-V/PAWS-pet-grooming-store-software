from datetime import date


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


class Appointment(Service):
    """
    Represents an appointment. It's composed of a service and a date of occurrence.
    """

    def __init__(self, description=None, price=None, dateOfAppointment=None):
        """
        Appointment class constructor.
        :param description: type of service provided -> string
        :param price: price of the service -> double
        :param dateOfAppointment: date when the service will be provided -> date
        """
        super().__init__(description, price)
        self.dateOfAppointment = dateOfAppointment if dateOfAppointment is not None else 0

    def __repr__(self):
        """Unambiguous representation of our object. Used mainly for debugging purposes."""
        return f"Service({self.description}, {self.price}, {self.dateOfAppointment})"

    def __str__(self):
        """Readable representation of our object. Used mainly to display our object to the user."""
        return f"Description: {self.description} | Price: {self.price} | Date: {self.dateOfAppointment}"

    def changeDate(self, newDate):
        """
        Updates appointment date.
        :param newDate: new appointment date -> date
        """
        self.dateOfAppointment = newDate
