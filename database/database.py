import sqlite3


# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- SQLITE FUNCTIONS ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


def createsAnimalsTable():
    """
    Creates a table of animals inside our database.

    Database inputs:
    > name: animal nickname -> string
    > owners: clients which hold the pet -> list of clients (owners)
    > typeOfAnimal: type of animal -> string
    > weight: animal's weight -> double
    > birthDate: animal's birth date -> datetime
    > history: record of all of the services (with dates) provided to the pet -> list of appointments
    > observations: Notes about the pet -> String
    > appointment: set of services appointed to the pet -> list of appointments
    """
    connection = sqlite3.connect("database/database.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE animals (
        id INTEGER PRIMARY KEY,
        name varchar(255), 
        ownersId foreign key,
        typeOfAnimal varchar(255),
        weight real,
        hairType varchar(255),
        birthDate timestamp,
        observations varchar(255),
        appointmentsId integer,
        history integer
        )""")
    connection.close()


def createsClientsTable():
    """
    Creates a table of clients inside our database.

    Database inputs:
    > name: animal nickname -> string
    > owners: clients which hold the pet -> list of clients (owners)
    > typeOfAnimal: type of animal -> string
    > weight: animal's weight -> double
    > birthDate: animal's birth date -> datetime
    > history: record of all of the services (with dates) provided to the pet -> list of appointments
    > observations: Notes about the pet -> String
    > appointment: set of services appointed to the pet -> list of appointments
    """
    connection = sqlite3.connect("database/database.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE clients (
        id integer PRIMARY KEY,
        name varchar(255), 
        email varchar(255),
        phone integer,
        nif integer,
        address varchar(255),
        petsId integer,
        FOREIGN KEY(petsId) REFERENCES animals(id)
        )""")
    connection.close()
