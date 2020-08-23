from sqlite3 import *


def getsInfoForClientWindow(clientID):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the client toplevel window.

    :param clientID: client row id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.name, animals.typeOfAnimal, animals.weight, 
                    animals.hairType, animals.birthDate, animals.observations,
                    clients.name, clients.nif, clients.phone, clients.email, clients.address
                from
                    animals
                inner join
                    clients,
                    petsClientsLink
                where
                    clients.ROWID = {clientID}
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
