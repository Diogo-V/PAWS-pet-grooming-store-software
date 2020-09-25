from sqlite3 import *


def deleteRecordAnimal(identifier):
    """
    Description:
    Deletes a record of an animal in the database.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connectionDB = connect("database/database.sqlite")
    cursorDB = connectionDB.cursor()
    connectionHistory = connect("database/history.sqlite")
    cursorHistory = connectionDB.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from animals where ROWID = {identifier}"

        # Deletes pet history inside history.sqlite
        queryDeleteHistory = f"delete from history where animalId = {identifier}"

        # Executes commands
        cursorDB.execute(query)
        cursorHistory.execute(queryDeleteHistory)

        # Deletes record from the database
        connectionDB.commit()
        connectionHistory.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connectionDB.rollback()  # Removes any change made during execution
        connectionHistory.rollback()  # Removes any change made during execution

    finally:

        connectionDB.close()  # Closes connection with our database
        connectionHistory.close()  # Closes connection with our database


def deleteRecordClient(identifier):
    """
    Description:
    Deletes a record of a client in the database.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from clients where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteRecordAppointment(identifier):
    """
    Description:
    Deletes a record of an appointment in the database.

    :param identifier: appointment id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from appointments where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteRecordHistory(identifier):
    """
    Description:
    Deletes a record of a past appointment in the database.

    :param identifier: history id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/history.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from history where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteRecordPetClientLink(tupleOfID):
    """
    Description:
    Deletes a record of a link between a pet and a client in the database.

    :param tupleOfID: tuple of ids -> tuple of integers
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from petsClientsLink where petId = {tupleOfID[0]} and clientId = {tupleOfID[1]}"

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteClientsLinks(identifier):
    """
    Description:
    Deletes links records which are connected to this client.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from petsClientsLink where clientId = {identifier}"

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deletePetsLinks(identifier):
    """
    Description:
    Deletes links records which are connected to this pet.

    :param identifier: pet id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from petsClientsLink where petId = {identifier}"

        # Executes command
        cursor.execute(query)

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteClientsPets(identifier):
    """
    Description:
    Deletes pets that don't have any more owners and their links.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # Gets all the pets of this client
        queryGetsPets = f"""select petId from petsClientsLink where petsClientsLink.clientId = {identifier}"""
        pets = cursor.execute(queryGetsPets).fetchall()

        # For each pet, we check if it has more than one owner, if not, we delete it since it's only link is this client
        for pet in pets:
            queryCountsPetsOwners = f"""select count() from petsClientsLink where petId = {pet[0]}"""
            numberOfClients = cursor.execute(queryCountsPetsOwners).fetchall()
            if numberOfClients[0][0] is 1:
                deleteRecordAnimal(pet[0])
                deletePetsLinks(pet[0])

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deletePetsClients(identifier):
    """
    Description:
    Eliminates owners of only this animal and their links.

    :param identifier: pet id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # Gets all the owners of this pet
        queryGetsOwners = f"""select clientId from petsClientsLink where petsClientsLink.petId = {identifier}"""
        owners = cursor.execute(queryGetsOwners).fetchall()

        # For each owner, we check if he has more than one pet, if not, we delete him since it's only link is this pet
        for owner in owners:
            queryCountsOwnersPets = f"""select count() from petsClientsLink where clientId = {owner[0]}"""
            numberOfPets = cursor.execute(queryCountsOwnersPets).fetchall()
            if numberOfPets[0][0] is 1:
                deleteRecordClient(owner[0])
                deleteClientsLinks(owner[0])

        # Deletes record from the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database
