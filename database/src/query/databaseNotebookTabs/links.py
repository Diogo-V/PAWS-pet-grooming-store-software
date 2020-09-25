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
                    animals.name, 
                    animals.type,
                    animals.breed,
                    clients.name,
                    clients.phone
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
        print("ERROR: getsAllLinks")
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
                    petsClientsLink.ROWID,
                    animals.name, 
                    animals.type,
                    animals.breed,
                    clients.name,
                    clients.phone
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
        print("ERROR: getsRequestedLinks")

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
                    animals.name, 
                    animals.type,
                    animals.breed,
                    clients.name
                from
                    animals
                inner join 
                    clients, 
                    petsClientsLink
                where
                    animals.ROWID = petsClientsLink.petId and clients.ROWID = petsClientsLink.clientId
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        return info

    except Error:

        # Error information and details processing
        print("ERROR: getsPetsForLinksWindow")

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
                    clients.phone,
                    animals.name
                from
                    clients
                inner join 
                    animals, petsClientsLink
                where 
                    petsClientsLink.clientId = clients.ROWID and petsClientsLink.petId = animals.ROWID
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        return info

    except Error:

        # Error information and details processing
        print("ERROR: getsClientsForLinksWindow")

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
        print("ERROR: checksIfLinkIsAlreadyInDatabase")

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
        [petName, petType, petBreed] = queryInfo

        myQuery = ''

        # Gets query
        if petName != '':
            myQuery += f"animals.name like '%{petName}%' and "
        if petType != '':
            myQuery += f"animals.type like '%{petType}%' and "
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
                    animals.ROWID, animals.name, animals.type, animals.breed, clients.name
                from
                    animals
                inner join 
                    clients, petsClientsLink
                where
                    animals.ROWID = petsClientsLink.petId and clients.ROWID = petsClientsLink.clientId and 
                    {getQuery()}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        return info

    except Error:

        # Error information and details processing
        print("ERROR: getsRequestedPets")
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

        search = ''

        if clientName != '':
            search += f"clients.name like '%{clientName}%' and "
        if clientPhone != '':
            search += f"clients.phone like '%{clientPhone}%' and "

        return search[:-5]

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    clients.ROWID, clients.name, clients.phone, animals.name
                from
                    clients
                inner join 
                    animals, 
                    petsClientsLink
                where
                    animals.ROWID = petsClientsLink.petId and clients.ROWID = petsClientsLink.clientId and 
                    {getQuery()}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        return info

    except Error:

        # Error information and details processing
        print("ERROR: getsRequestedClients")

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
                    animals.rowid, animals.name, animals.type, animals.breed, animals.gender, animals.weight, 
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
        print("ERROR: getsInfoForLinkWindow")

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
        print("ERROR: checksIfPetHasMoreThanOneOwner")

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
        print("ERROR: checksIfClientHasMoreThanOnePet")

    finally:

        connection.close()  # Closes connection with our database
