from sqlite3 import *


def getPetsFromClient(identifier):
    """
    Description:
    Gets a list of the client's pets.

    :param identifier: client id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select * from animals inner join petsClientsLink on clientId == " + str(identifier) + \
                " and animals.ROWID == petId"

        # Executes command and gets a list of pets
        pets = cursor.execute(query).fetchall()

        # Returns pets found during query
        return pets

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getClientFromPets(identifier):
    """
    Description:
    Gets a list of the pet's owners.

    :param identifier: animal id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = "select * from clients inner join petsClientsLink on petId == " + str(identifier) + \
                " and clients.ROWID == clientId"

        # Executes command and gets a list of owners
        owners = cursor.execute(query).fetchall()

        # Returns clients found during query
        return owners

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database
