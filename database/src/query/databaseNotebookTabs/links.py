from sqlite3 import *


def getsAllLinks():
    """
    Description:
    Gets a list of tuples that hold all of the relationships between animals and owners.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    petsClientsLink.ROWID,
                    animals.name, animals.typeOfAnimal,
                    clients.name
                from
                    petsClientsLink
                inner join
                    animals,
                    clients
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


def getsRequestedLinks(queryInfo):
    """
    Description:
    > Gets a list of tuples that hold all of the relationships between animals and owners.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [petName, petType, clientName] = queryInfo

        if petName == '':
            if petType == '':
                return f"clients.name like '%{clientName}%'"
            elif clientName == '':
                return f"animals.typeOfAnimal like '%{petType}%'"
            else:
                return f"animals.typeOfAnimal like '%{petType}%' and clients.name like '%{clientName}%'"
        else:
            if petType == '':
                if clientName == '':
                    return f"animals.name like '%{petName}%'"
                else:
                    return f"animals.name like '%{petName}%' and clients.name like '%{clientName}%'"
            else:
                if clientName == '':
                    return f"animals.name like '%{petName}%' and animals.typeOfAnimal like '%{petType}%'"
                else:
                    return f"animals.name like '%{petName}%' and animals.typeOfAnimals like '%{petType}%' " \
                           f"and clients.name like '%{clientName}%'"

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    petsClientsLink.ROWID,
                    animals.name, animals.typeOfAnimal,
                    clients.name
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


def getsPetsForLinksWindow():
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


def getsClientsForLinksWindow():
    """
    Description:
    > Gets a list of tuples that hold all of the clients in our database.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID,
                    clients.name
                from
                    clients
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
