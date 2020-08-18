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
    cursor.execute("""CREATE TABLE IF NOT EXISTS animals (
        name varchar(255) default '', 
        typeOfAnimal varchar(255) default 'Cão',
        weight numeric default 0,
        hairType varchar(255) default 'Pelo curto',
        birthDate varchar(255) default '',
        observations varchar(255) default ''
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
    cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
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
    > date: date of execution -> date
    > time: time of the day -> time
    > price: amount paid -> double
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS appointments (
        services varchar(255) default '',
        date varchar(255) default '',
        time varchar(255) default '',
        price numeric default 0,
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
    > date: date of execution -> date
    > time: time of the day -> time
    > price: amount paid -> double
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS history (
        services varchar(255) default '',
        date varchar(255) default NULL,
        time varchar(255) default NULL,
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
    cursor.execute("""CREATE TABLE IF NOT EXISTS petsClientsLink (
            petId integer default 0,
            clientId integer default 0
            )""")
    connection.commit()
    connection.close()
