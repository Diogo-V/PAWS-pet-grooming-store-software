from sqlite3 import *
from database.src.utils.converters import *
from datetime import date


def getsClientPets(identifier):
    """
    Description:
    Gets a list of the client's pets.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select * from animals inner join petsClientsLink on clientId == " + str(identifier) + \
                " and animals.ROWID == petId"

        # Executes command and gets a list of pets
        pets = cursor.execute(query).fetchall()

        # Returns pets found during query
        return pets

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsPetOwners(identifier):
    """
    Description:
    Gets a list of the pet's owners.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select * from clients inner join petsClientsLink on petId == " + str(identifier) + \
                " and clients.ROWID == clientId"

        # Executes command and gets a list of owners
        owners = cursor.execute(query).fetchall()

        # Returns clients found during query
        return owners

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsPetAppointments(identifier):
    """
    Description:
    Gets a list of the pet's appointments.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select ROWID,* from appointments where animalId = " + str(identifier)

        # Executes command and gets a list of appointments
        appointments = cursor.execute(query).fetchall()

        # Returns appointments found during query
        return appointments

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsPetHistory(identifier):
    """
    Description:
    Gets a list of the pet's past appointments.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select ROWID,* from history where animalId = " + str(identifier)

        # Executes command and gets a list of history
        history = cursor.execute(query).fetchall()

        # Returns history found during query
        return history

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsDayAppointments(dateAppointment):
    """
    Description:
    Gets a list of appointments for a specific day.

    :param dateAppointment: required date -> date
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    appointments.ROWID,
                    animals.name, 
                    clients.name,
                    appointments.services, 
                    appointments.time,
                    clients.phone,
                    animals.observations
                from
                    animals
                inner join
                    appointments,
                    clients,
                    petsClientsLink
                where
                    appointments.date = '{dateToString(dateAppointment)}' and
                    appointments.animalId = petsClientsLink.petId and
                    animals.ROWID = petsClientsLink.petId and
                    clients.ROWID = petsClientsLink.clientId
                """

        # Executes command and gets a list of appointments
        appointments = cursor.execute(query).fetchall()

        # Returns appointments found during query
        return appointments

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsInfoForAppointmentsWindow(appointmentID):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the appointments toplevel window.

    :param appointmentID: appointment row id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.rowid, animals.name, animals.typeOfAnimal, 
                    animals.weight, animals.hairType, animals.observations,
                    clients.name, clients.nif, clients.phone,
                    appointments.services, appointments.date, appointments.time, appointments.price
                from
                    appointments
                inner join
                    animals,
                    clients,
                    petsClientsLink
                where
                    appointments.ROWID = {appointmentID}
                    and appointments.animalId = petsClientsLink.petId
                    and animals.ROWID = petsClientsLink.petId
                    and clients.ROWID = petsClientsLink.clientId
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database
