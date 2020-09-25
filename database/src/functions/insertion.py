from sqlite3 import *


def transformsDateAppointmentToInteger(app, idxOfDate):
    """
    Description:
    > Changes input date into an integer so that we can insert it inside our database.
    :param app: tuple with the information about an appointment inside our database -> tuple
    :param idxOfDate: tuple index where date is located -> integer
    :return: tuple with our formatted information -> tuple
    """
    app = list(app)
    app[idxOfDate] = app[idxOfDate].toordinal()
    return tuple(app)


def insertRecordAnimal(animal):
    """
    Description:
    Creates a new record of an animal in the database.

    :param animal: set of information that represents an animal -> tuple
    :return newly created pet's rowid -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into animals (name, type, breed, gender, weight, hairType, hairColor, age, observations) " \
                "values (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        # Executes command
        cursor.execute(query, animal)

        # Writes new record in the database
        connection.commit()

        # Returns rowid of the just inserted pet
        return cursor.lastrowid

    except Error:

        # Error information and details processing
        print("ERROR: insertRecordAnimal")

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

        # Returns rowid of the just inserted pet
        return cursor.lastrowid

    except Error:

        # Error information and details processing
        print("ERROR: insertRecordClient")

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

    # Transforms date into an integer so that it can be stored in our database
    appointment = transformsDateAppointmentToInteger(appointment, 1)

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into appointments (services, date, time, price, observations, animalId) " \
                "values (?, ?, ?, ?, ?, ?)"

        # Executes command
        cursor.execute(query, appointment)

        # Writes new record in the database
        connection.commit()

    except Error:

        # Error information and details processing
        print("ERROR: insertRecordAppointment")

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
    connection = connect("database/history.sqlite")
    cursor = connection.cursor()

    # Transforms date into an integer so that it can be stored in our database
    history = transformsDateAppointmentToInteger(history, 1)

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "insert into history (services, date, time, price, observations, animalId) VALUES (?, ?, ?, ?, ?, ?)"

        # Executes command
        cursor.execute(query, history)

        # Writes new record in the database
        connection.commit()

    except Error:

        # Error information and details processing
        print("ERROR: insertRecordHistory")

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
        print("ERROR: insertRecordPetClientLink")

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database
