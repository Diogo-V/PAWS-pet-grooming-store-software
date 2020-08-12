from sqlite3 import *


def insertRecordAnimal(animal):
    """
    Description:
    Creates a new record of an animal in the database.

    :param animal: set of information that represents an animal -> tuple
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into animals (name, typeOfAnimal, weight, hairType, birthDate, observations) " \
                "values (?, ?, ?, ?, ?, ?)"

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


def insertRecordClient(client):
    """
    Description:
    Creates a new record of a client in the database.

    :param client: set of information that represents a client -> tuple
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into clients (name, email, phone, nif, address) VALUES (?, ?, ?, ?, ?)"

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


def insertRecordAppointment(appointment):
    """
    Description:
    Creates a new record of an appointment in the database.

    :param appointment: set of information that represents an appointment -> tuple
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into appointments (services, date, time, animalId) VALUES (?, ?, ?, ?)"

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


def insertRecordHistory(history):
    """
    Description:
    Creates a new record of a past appointment in the database.

    :param history: set of information that represents a past appointment -> tuple
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into history (services, date, time, price, animalId) VALUES (?, ?, ?, ?, ?)"

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


def insertRecordPetClientLink(link):
    """
    Description:
    Creates a new record of a link in the database.

    :param link: combo of two integers that represents a link -> tuple
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into petsClientsLink (petId, clientId) VALUES (?, ?)"

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
