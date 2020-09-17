from sqlite3 import *


def getsInfoForPetWindow(petID):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the pet toplevel window.

    :param petID: pet row id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.name, animals.type, animals.breed, animals.gender, animals.weight, 
                    animals.hairType, animals.hairColor, animals.age, animals.observations,
                    clients.name, clients.nif, clients.phone, clients.email, clients.address
                from
                    animals
                inner join
                    clients,
                    petsClientsLink
                where
                    animals.ROWID = {petID}
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


def getsAllPets():
    """
    Description:
    > Gets a list of the information that is going to be displayed inside the pet main tree.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID,
                    animals.name, 
                    clients.name,
                    animals.type, 
                    animals.breed,
                    animals.weight, 
                    animals.hairType
                from
                    animals
                inner join
                    clients,
                    petsClientsLink
                where
                    animals.ROWID = petsClientsLink.petId
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


def getsRequestedPets(queryInfo):
    """
    Description:
    > Gets a list of tuples that hold all of the requested animals.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [petName, petType, petBreed, clientName] = queryInfo

        myQuery = ''

        # Gets query
        if petName != '':
            myQuery += f"animals.name like '%{petName}%' and "
        if petType != '':
            myQuery += f"animals.type like '%{petType}%' and "
        if petBreed != '':
            myQuery += f"animals.breed like '%{petBreed}%' and "
        if clientName != '':
            myQuery += f"clients.name like '%{clientName}%' and "

        return myQuery[:-5]

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID,
                    animals.name, 
                    clients.name,
                    animals.type, 
                    animals.breed,
                    animals.weight, 
                    animals.hairType
                from
                    petsClientsLink
                inner join
                    animals,
                    clients
                where
                    animals.ROWID = petsClientsLink.petId
                    and clients.ROWID = petsClientsLink.clientId and
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
