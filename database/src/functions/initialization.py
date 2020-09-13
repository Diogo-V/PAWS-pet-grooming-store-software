from sqlite3 import *


def createsAnimalsTable():
    """
    Creates a table of animals inside our database.

    Database inputs:
    > id: primary key -> integer
    > name: animal nickname -> string
    > type: type of animal -> string
    > breed: type of breed -> string
    > gender: gender of the animal -> string
    > weight: animal's weight -> double
    > hairType: type of hair -> string
    > hairColor: color of fur -> string
    > age: animal's age -> integer
    > observations: Notes about the pet -> String
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS animals (
        name varchar(255) default '', 
        type varchar(255) default 'Cão',
        breed varchar(255) default '',
        gender varchar(255) default '',
        weight numeric default 0,
        hairType varchar(255) default '',
        hairColor varchar(255) default '',
        age integer default 0,
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
    > date: date of execution in days past 1/1/0-> integer
    > time: time of the day -> time
    > price: amount paid -> double
    > observations: observations relative to this appointment -> string
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS appointments (
        services varchar(255) default '',
        date integer default 0,
        time varchar(255) default '',
        price numeric default 0,
        observations varchar(255) default '',
        animalId integer,
        FOREIGN KEY(animalId) REFERENCES animals(rowid) on delete cascade 
        )""")
    connection.commit()
    connection.close()


def createsHistoryTable():
    """
    Creates a table of past appointments inside our database.

    Database inputs:
    > id: primary key -> integer
    > services: set of services that are going to be provided -> list of strings
    > date: date of execution in days past 1/1/0-> integer
    > time: time of the day -> time
    > price: amount paid -> double
    > observations: observations relative to this appointment -> string
    > animalId: animal that holds this appointment -> integer
    """
    connection = connect("database/history.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS history (
        services varchar(255) default '',
        date integer default 0,
        time varchar(255) default '',
        price numeric default 0,
        observations varchar(255) default '',        
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
