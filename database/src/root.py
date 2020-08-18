from database.src.functions.initialization import *
from database.src.utils.converters import *


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

    # Creates tables
    createsAllTables()


def deleteAllTables():
    """Deletes all existing tables inside our database."""
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE animals")
    cursor.execute("DROP TABLE clients")
    cursor.execute("DROP TABLE petsClientsLink")
    cursor.execute("DROP TABLE appointments")
    cursor.execute("DROP TABLE history")
    connection.commit()
    connection.close()
