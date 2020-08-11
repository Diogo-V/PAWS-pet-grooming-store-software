from sqlite3 import *


def createsAnimalsTable():
    """
    Creates a table of animals inside our database.

    Database inputs:
    > id: primary key -> integer
    > name: animal nickname -> string
    > typeOfAnimal: type of animal -> string
    > weight: animal's weight -> double
    > hairType: type of hair -> string
    > birthDate: animal's birth date -> datetime
    > observations: Notes about the pet -> String
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE animals (
        name varchar(255) default NULL, 
        typeOfAnimal varchar(255) default 'Cão',
        weight numeric default NULL,
        hairType varchar(255) default 'Pelo curto',
        birthDate varchar(255) default NULL,
        observations varchar(255) default NULL
        )""")
    connection.commit()
    connection.close()


def createsClientsTable():
    """
    Creates a table of clients inside our database.

    Database inputs:
    > id: primary key -> integer
    > name: full-name or just first name -> string
    > email: electronic mail -> string
    > phone: 9 digits representing a phone number -> integer
    > nif: 9 digits representing NIF -> integer
    > address: address -> datetime
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE clients (
        name varchar(255) default '',
        email varchar(255) default '',
        phone integer default 0,
        nif integer default 0,
        address varchar(255) default ''
        )""")
    connection.commit()
    connection.close()


def createsAppointmentsTable():
    """
    Creates a table of appointments inside our database.

    Database inputs:
    > id: primary key -> integer
    > services: set of services that are going to be provided -> list of strings
    > dateOfAppointment: date of execution -> date
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE appointments (
        services varchar(255) default '',
        dateOfAppointment varchar(255) default NULL,
        animalId integer,
        FOREIGN KEY(animalId) REFERENCES animals(rowid)
        )""")
    connection.commit()
    connection.close()


def createsHistoryTable():
    """
    Creates a table of past appointments inside our database.

    Database inputs:
    > id: primary key -> integer
    > services: set of services that are going to be provided -> list of strings
    > dateOfAppointment: date of execution -> date
    > price: amount paid -> double
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE history (
        services varchar(255) default '',
        dateOfAppointment varchar(255) default NULL,
        price numeric default 0,        
        animalId integer,
        FOREIGN KEY(animalId) REFERENCES animals(rowid)
        )""")
    connection.commit()
    connection.close()


def createsPetsClientsLinkTable():
    """
        Creates a table that links pets and clients inside our database.

        Database inputs:
        > id: primary key -> integer
        > petId: identifier of the pet -> integer
        > clientId: identifier of the client -> integer
        """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE petsClientsLink (
            petId integer default 0,
            clientId integer default 0
            )""")
    connection.commit()
    connection.close()


def initAllTables():
    """Creates and initiates all tables."""
    createsAnimalsTable()
    createsClientsTable()
    createsPetsClientsLinkTable()
    createsAppointmentsTable()
    createsHistoryTable()


def deleteAllTables():
    """Deletes all existing tables inside our database."""
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE animals")
    cursor.execute("DROP TABLE clients")
    cursor.execute("DROP TABLE petsClientsLink")
    cursor.execute("DROP TABLE appointments")
    cursor.execute("DROP TABLE history")
    connection.commit()
    connection.close()
