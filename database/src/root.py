from database.src.functions.initialization import *
from database.src.utils.maintenance import movesAppointmentsToHistory, clearsElementsWithNoLinks


def createsAllTables():
    """Creates and initiates all tables of our database."""
    createsAnimalsTable()
    createsClientsTable()
    createsPetsClientsLinkTable()
    createsAppointmentsTable()
    createsHistoryTable()


def initDatabase():
    """Updates appointments and creates all tables if needed."""

    # Updates appointments
    movesAppointmentsToHistory()

    # Eliminates unnecessary entries inside our database
    clearsElementsWithNoLinks()

    # Creates tables
    createsAllTables()


def deleteAllTables():
    """Deletes all existing tables inside our database."""

    # Creates connections to our databases and cursors to work with it
    mainDBConn = connect("database/database.sqlite")
    mainDBCursor = mainDBConn.cursor()
    historyDBConn = connect("database/history.sqlite")
    historyDBCursor = historyDBConn.cursor()

    mainDBCursor.execute("DROP TABLE animals")
    mainDBCursor.execute("DROP TABLE clients")
    mainDBCursor.execute("DROP TABLE petsClientsLink")
    mainDBCursor.execute("DROP TABLE appointments")
    historyDBCursor.execute("DROP TABLE history")

    mainDBConn.commit()
    historyDBConn.commit()
    mainDBConn.close()
    historyDBConn.close()
