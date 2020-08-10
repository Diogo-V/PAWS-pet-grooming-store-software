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

        # Writes new record in the database
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

        # Writes new record in the database
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

        # Writes new record in the database
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
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from history where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query)

        # Writes new record in the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database


def deleteRecordPetClientLink(identifier):
    """
    Description:
    Deletes a record of a link between a pet and a client in the database.

    :param identifier: link id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"delete from petsClientsLink where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query)

        # Writes new record in the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database
