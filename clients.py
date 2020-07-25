class Client:
    """
    Represents a client. Each client has one or more animals
    """

    numberOfClients = 0  # Amount of clients within our program

    def __init__(self, first=None, last=None, email=None, phone=None, nif=None, address=None, pets=None):
        """
        Client class constructor:
        > Creates a client using the provided info about him. If parameters are not passed, sets them to None
        :param first: first name -> string
        :param last: last name -> string
        :param email: email address -> string
        :param phone: list of phone numbers -> list of integers with 9 digits
        :param nif: tax identification number -> 9 digit integer
        :param address: where the client lives -> string
        :param pets: client's pet's names -> list of Animals
        """
        self.first = first if first is not None else ''
        self.last = last if last is not None else ''
        self.email = email if email is not None else ''
        self.phone = phone if phone is not None else []
        self.nif = nif if nif is not None else 0
        self.address = address if address is not None else ''
        self.pets = pets if pets is not None else []
        Client.numberOfClients += 1  # Since we created one more client, we have to increment our status variable

    def __repr__(self):
        """Unambiguous representation of our object. Used mainly for debugging purposes."""
        return f"Client({self.first}, {self.last}, {self.email}, {self.phone}, {self.nif}, {self.address}, {self.pets})"

    def __str__(self):
        """Readable representation of our object. Used mainly to display our object to the user."""
        return f"Name: {self.first} | Phone number: {self.phone} | Pets: {self.pets}"

    def __len__(self):
        """Returns the amount of pets the client has."""
        return len(self.pets)

    def addAnimal(self, animal):
        if animal not in self.pets:
            self.pets.append(animal)

    def removeAnimal(self, animal):
        if animal in self.pets:
            self.pets.remove(animal)
