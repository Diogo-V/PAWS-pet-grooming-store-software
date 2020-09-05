from sqlite3 import *


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
                      animals.typeOfAnimal,
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
        [petName, petType, clientName, clientPhone] = queryInfo

        # Holds our query search arguments. Has a space to separate from previous 'and'
        search = " "

        # Populates search
        if petName != '':
            search += f"animals.name like '%{petName}%' and "
        if petType != '':
            search += f"animals.typeOfAnimal like '%{petType}%' and "
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
                      animals.typeOfAnimal,
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
        [petName, petType] = queryInfo

        if petName == '':
            return f"animals.typeOfAnimal like '%{petType}%'"
        elif petType == '':
            return f"animals.name like '%{petName}%'"
        else:
            return f"animals.name like '%{petName}%' and animals.typeOfAnimal like '%{petType}%'"

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID, animals.name, animals.typeOfAnimal
                from
                    animals
                where
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
                    animals.name, animals.typeOfAnimal
                from
                    animals
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
