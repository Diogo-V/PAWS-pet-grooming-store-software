from sqlite3 import *


def updateRecordAnimal(animal, identifier):
    """
    Description:
    Updates a record of an animal in the database.

    :param animal: new set of information that will represent an animal -> tuple
    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"update animals set (name, typeOfAnimal, weight, hairType, birthDate, observations) = " \
                "(?, ?, ?, ?, ?, ?) where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query, animal)

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


def updateRecordClient(client, identifier):
    """
    Description:
    Updates a record of an animal in the database.

    :param client: new set of information that will represent a client -> tuple
    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"update clients set (name, email, phone, nif, address) = " \
                "(?, ?, ?, ?, ?) where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query, client)

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


def updateRecordAppointment(appointment, identifier):
    """
    Description:
    Updates a record of an appointment in the database.

    :param appointment: new set of information that will represent an appointment -> tuple
    :param identifier: appointment id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"update appointments set (services, dateOfAppointment, animalId) = " \
                "(?, ?, ?) where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query, appointment)

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


def updateRecordHistory(history, identifier):
    """
    Description:
    Updates a record of a past appointment in the database.

    :param history: new set of information that will represent a past appointment -> tuple
    :param identifier: history id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"update history set (services, dateOfAppointment, price, animalId) = " \
                "(?, ?, ?, ?) where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query, history)

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


def updateRecordPetClientLink(link, identifier):
    """
    Description:
    Updates a record of a link in the database.

    :param link: combo of two integers that represent a link between a client and a pet -> tuple
    :param identifier: link id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"update petsClientsLink set (petId, clientId) = (?, ?) where ROWID = " + str(identifier)

        # Executes command
        cursor.execute(query, link)

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
