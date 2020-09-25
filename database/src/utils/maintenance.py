from datetime import date
from sqlite3 import *


def movesAppointmentsToHistory():
    """
    Description:
    > Moves past appointments that have been executed to history table. Is executed each time the application is loaded.
    """

    # Creates connections to our databases and cursors to work with it
    mainDBConn = connect("database/database.sqlite")
    mainDBCursor = mainDBConn.cursor()
    historyDBConn = connect("database/history.sqlite")
    historyDBCursor = historyDBConn.cursor()

    try:

        # SQL syntax that gets all the past appointments
        queryGetsPastAppointments = f"select * from appointments where date < {date.today().toordinal()}"

        # SQL syntax that inserts past appointments in the history table
        queryInsertHistory = "insert into history (services, date, time, price, observations, animalId) " \
                             "VALUES (?, ?, ?, ?, ?, ?)"

        # SQL syntax that deletes past appointments from the appointments table
        queryDeleteAppointments = f"delete from appointments where date < {date.today().toordinal()}"

        # Executes query and gets all the appointments that should be moved
        pastApp = mainDBCursor.execute(queryGetsPastAppointments).fetchall()

        # Insert all the results inside our history database. Validates if we only found one match or multiple
        if type(pastApp) is list and pastApp != []:
            historyDBCursor.executemany(queryInsertHistory, pastApp)
        elif type(pastApp) is tuple and pastApp != []:
            historyDBCursor.execute(queryInsertHistory, pastApp)

        # Executes deletion
        mainDBCursor.execute(queryDeleteAppointments)

        # Writes changes in both databases
        mainDBConn.commit()
        historyDBConn.commit()

    except Error:

        # Error information and details processing
        print("ERROR: movesAppointmentsToHistory")

        mainDBConn.rollback()  # Removes any change made during execution
        historyDBConn.rollback()  # Removes any change made during execution

    finally:

        mainDBConn.close()  # Closes connection with our database
        historyDBConn.close()  # Closes connection with our database


def clearsElementsWithNoLinks():
    """
    Description:
    > Eliminates clients with not pets and pets with no clients from the database.
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that deletes clients with no pets
        queryDeleteClients = f"""
                              delete from clients where clients.ROWID not in 
                              (select clients.ROWID from clients inner join petsClientsLink 
                              where petsClientsLink.clientId = clients.ROWID)
                              """

        # SQL syntax that deletes pets with no owners
        queryDeletePets = f"""
                           delete from animals where animals.ROWID not in 
                           (select animals.ROWID from animals inner join petsClientsLink 
                           where petsClientsLink.petId = animals.ROWID)
                           """

        # SQL syntax that deletes links which hold info that doesn't exist
        queryDeleteLinks = f"""
                            delete from petsClientsLink where petsClientsLink.ROWID not in 
                            (select petsClientsLink.ROWID from petsClientsLink inner join clients, animals where
                            petsClientsLink.petId = animals.ROWID and petsClientsLink.clientId = clients.ROWID)
                            """

        # Executes links deletion command
        cursor.execute(queryDeleteLinks)

        # Executes clients deletion command
        cursor.execute(queryDeleteClients)

        # Executes pets deletion command
        cursor.execute(queryDeletePets)

        # Writes changes inside our database
        connection.commit()

    except Error:

        # Error information and details processing
        print("ERROR: clearsElementsWithNoLinks")

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database
