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
                    animals.name, animals.type,
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
                return f"animals.type like '%{petType}%'"
            else:
                return f"animals.type like '%{petType}%' and clients.name like '%{clientName}%'"
        else:
            if petType == '':
                if clientName == '':
                    return f"animals.name like '%{petName}%'"
                else:
                    return f"animals.name like '%{petName}%' and clients.name like '%{clientName}%'"
            else:
                if clientName == '':
                    return f"animals.name like '%{petName}%' and animals.type like '%{petType}%'"
                else:
                    return f"animals.name like '%{petName}%' and animals.type like '%{petType}%' " \
                           f"and clients.name like '%{clientName}%'"

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    petsClientsLink.ROWID,
                    animals.name, animals.type,
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
                    animals.name, animals.type
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
                    clients.name,
                    clients.phone
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


def checksIfLinkIsAlreadyInDatabase(link):
    """
    Description:
    > Checks if links is inside our database.

    :return boolean value -> boolean
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select 
                    exists(
                        select 1 from petsClientsLink where petId = {link[0]} and clientId = {link[1]}
                    );
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()[0][0]

        # Returns a boolean value according to the result. Can return an error if is invalid
        if info == 1:
            return True
        elif info == 0:
            return False
        else:
            raise ValueError("Invalid return type")

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
            return f"animals.type like '%{petType}%'"
        elif petType == '':
            return f"animals.name like '%{petName}%'"
        else:
            return f"animals.name like '%{petName}%' and animals.type like '%{petType}%'"

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID, animals.name, animals.type
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


def getsRequestedClients(queryInfo):
    """
    Description:
    > Gets a list of tuples that holds information about clients that is going to be displayed.

    :param queryInfo: list containing the info to query upon -> list of strings
    """

    def getQuery():
        """Checks the type of query that we need to make and gets it."""

        # Extracts components
        [clientName, clientPhone] = queryInfo

        if clientPhone == '':
            return f"clients.name like '%{clientName}%'"
        elif clientName == '':
            return f"clients.phone like '%{clientPhone}%'"
        else:
            return f"clients.name like '%{clientName}%' and clients.phone like '%{clientPhone}%'"

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID, clients.name
                from
                    clients
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


def getsInfoForLinkWindow(linkID):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the link toplevel window.

    :param linkID: link row id -> integer
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
                    petsClientsLink.ROWID = {linkID}
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


def checksIfPetHasMoreThanOneOwner(petID):
    """
    Description:
    > Checks if the input pet more than one owner.
    :param petID: rowid of a pet -> integer
    :return: boolean
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
                    petsClientsLink
                where
                    petsClientsLink.clientId = clients.ROWID and 
                    petsClientsLink.petId = {petID}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Checks we had more than one owner
        if len(info) >= 2:
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


def checksIfClientHasMoreThanOnePet(clientID):
    """
    Description:
    > Checks if the input client has more than one pet.
    :param clientID: rowid of a client -> integer
    :return: boolean
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.ROWID
                from
                    animals
                inner join
                    petsClientsLink
                where
                    petsClientsLink.petId = animals.ROWID and 
                    petsClientsLink.clientId = {clientID}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Checks we had more than one owner
        if len(info) >= 2:
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
