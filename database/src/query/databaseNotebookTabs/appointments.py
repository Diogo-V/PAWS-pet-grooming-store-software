import datetime
from sqlite3 import *

from database.src.utils.converters import dateToString


def transformsIntegerAppointmentDateToString(app, idxOfDate):
    """
    Description:
    > Changes date inside app from integer to a printable string.
    :param app: tuple with the information about an appointment inside our database -> tuple
    :param idxOfDate: tuple index where date is located -> integer
    :return: tuple with our formatted information -> tuple
    """
    app = list(app)
    app[idxOfDate] = dateToString(datetime.date.fromordinal(app[idxOfDate]))
    return tuple(app)


def getsAllAppointments():
    """
    Description:
    > Gets all the appointments inside our database.
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
                      animals.type,
                      animals.breed,
                      clients.name,
                      clients.phone,
                      appointments.date,
                      appointments.time
                  from
                      appointments
                  inner join
                      animals,
                      clients,
                      petsClientsLink
                  where
                      animals.ROWID = appointments.animalId and
                      animals.ROWID = petsClientsLink.petId and 
                      clients.ROWID = petsClientsLink.clientId
                  """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Converts our date to a string
        if type(info) is list and info != []:
            info = list(map(lambda app: transformsIntegerAppointmentDateToString(app, 6), info))
        elif type(info) is tuple:
            info = transformsIntegerAppointmentDateToString(info, 6)

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsRequestedAppointments(queryInfo):
    """
    Description:
    > Gets a list of tuples that hold all of the requested appointments.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [petName, petType, petBreed, clientName, clientPhone] = queryInfo

        # Holds our query search arguments. Has a space to separate from previous 'and'
        search = " "

        # Populates search
        if petName != '':
            search += f"animals.name like '%{petName}%' and "
        if petType != '':
            search += f"animals.type like '%{petType}%' and "
        if petBreed != '':
            search += f"animals.breed like '%{petBreed}%' and "
        if clientName != '':
            search += f"clients.name like '%{clientName}%' and "
        if clientPhone != '':
            search += f"clients.phone like '%{clientPhone}%' and "

        # Returns our completed search arguments. Removes last 'and'
        return search[:-5]

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                  select
                      appointments.ROWID,
                      animals.name, 
                      animals.type,
                      animals.breed,
                      clients.name,
                      clients.phone,
                      appointments.date,
                      appointments.time
                  from
                      appointments
                  inner join
                      animals,
                      clients,
                      petsClientsLink
                  where
                      animals.ROWID = appointments.animalId and
                      animals.ROWID = petsClientsLink.petId and 
                      clients.ROWID = petsClientsLink.clientId and
                      {getQuery()}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Converts our date to a string
        if type(info) is list and info != []:
            info = list(map(lambda app: transformsIntegerAppointmentDateToString(app, 6), info))
        elif type(info) is tuple:
            info = transformsIntegerAppointmentDateToString(info, 6)

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsRequestedPets(queryInfo):
    """
    Description:
    > Gets a list of tuples that holds information about pets that is going to be displayed.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [petName, petBreed, clientName] = queryInfo

        search = ''

        if petName != '':
            search += f"animals.name like '%{petName}%' and "
        if petBreed != '':
            search += f"animals.breed like '%{petBreed}%' and "
        if clientName != '':
            search += f"clients.name like '%{clientName}%' and "

        return search[:-5]

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID,
                    animals.name, animals.breed, clients.name
                from
                    animals
                inner join 
                    clients, 
                    petsClientsLink
                where 
                    animals.ROWID = petsClientsLink.petId and 
                    clients.ROWID = petsClientsLink.clientId and 
                    {getQuery()}
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


def getsPetsForAppointmentsWindow():
    """
    Description:
    > Gets a list of tuples that hold all of the animals in our database.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID,
                    animals.name, animals.breed, clients.name
                from
                    animals
                inner join 
                    clients, 
                    petsClientsLink
                where 
                    animals.ROWID = petsClientsLink.petId and 
                    clients.ROWID = petsClientsLink.clientId
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


def checksIfPetHasAnOwner(petID):
    """
    Description:
    > Checks if the pet has a client associated to it.
    :param petID: pet rowid -> integer
    :return boolean value
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID
                from
                    clients
                inner join 
                    animals, petsClientsLink
                where
                    petsClientsLink.petId = {petID} and petsClientsLink.clientId = clients.ROWID
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Checks if pet has at least one owner. If so returns True, else, False
        if len(info) > 0:
            return True
        else:
            return False

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsAppointmentsForDayAppTree(myDate):
    """
    Description:
    > Gets a list of tuples that hold all the appointments for the selected day.
    :param myDate: requested date -> date
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    appointments.ROWID,
                    appointments.time, 
                    appointments.services,
                    animals.name
                from
                    appointments
                inner join 
                    animals
                where 
                    animals.ROWID = appointments.animalId and
                    appointments.date = {myDate.toordinal()}
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
