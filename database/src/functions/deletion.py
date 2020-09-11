from sqlite3 import *


def deleteRecordAnimal(identifier):
    """
    Description:
    Deletes a record of an animal in the database.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from animals where ROWID = " + str(identifier)

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
    Deletes pets associated with this client.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                delete from
                    animals
                where
                    animals.ROWID in (select animals.ROWID from animals inner join clients, petsClientsLink where 
                                      animals.ROWID = petsClientsLink.petId and petsClientsLink.clientId = {identifier})
                """

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


def deletePetsClients(identifier):
    """
    Description:
    Deletes pets associated with this pet.

    :param identifier: pet id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                delete from
                    clients
                where
                    clients.ROWID in (select clients.ROWID from clients inner join animals, petsClientsLink where 
                                      animals.ROWID = {identifier} and petsClientsLink.clientId = clients.ROWID)
                """

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
