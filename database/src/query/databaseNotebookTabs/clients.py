from sqlite3 import *


def getsInfoForClientWindow(clientID, petName):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the client toplevel window.

    :param clientID: client row id -> integer
    :param petName: client's pet name -> string
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.rowid, animals.name, animals.type, animals.breed, animals.gender, animals.weight, 
                    animals.hairType, animals.hairColor, animals.age, animals.observations,
                    clients.name, clients.nif, clients.phone, clients.email, clients.address
                from
                    animals
                inner join
                    clients,
                    petsClientsLink
                where
                    clients.ROWID = {clientID}
                    and animals.name = '{petName}'
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


def getsAllClients():
    """
    Description:
    > Gets a list of the information that is going to be displayed inside the clients main tree.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID,
                    clients.name, 
                    clients.phone,
                    animals.name, 
                    animals.type,
                    animals.breed
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


def getsRequestedClients(queryInfo):
    """
    Description:
    > Gets a list of tuples that hold all of the requested clients.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [clientName, clientPhone, petName, petBreed] = queryInfo

        myQuery = ''

        if petName != '':
            myQuery += f"animals.name like '%{petName}%' and "
        if clientName != '':
            myQuery += f"clients.name like '%{clientName}%' and "
        if clientPhone != '':
            myQuery += f"clients.phone like '%{clientPhone}%' and "
        if petBreed != '':
            myQuery += f"animals.breed like '%{petBreed}%' and "

        return myQuery[:-5]

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID,
                    clients.name, 
                    clients.phone,
                    animals.name, 
                    animals.type,
                    animals.breed
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
