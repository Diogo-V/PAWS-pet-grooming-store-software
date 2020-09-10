from datetime import date
from sqlite3 import *


def dateToString(myDate):
    """Converts a date to a string. Used to serialize dates for the database."""
    return myDate.strftime('%d/%m/%Y')


def stringToDate(myDate):
    """Converts a string date into a datetime.date object."""
    [day, month, year] = myDate.split("/")
    return date(int(year), int(month), int(day))


def timeToString(myDate):
    """Converts a time to a string. Used to serialize dates for the database."""
    return myDate.strftime('%H-%M-%S')


def servicesToString(lstServices):
    """Converts a list of services to a string. Used to serialize a list for the database."""

    strServices = ""  # Holds final service string

    # Iterates over each service and adds an | at the end to separate them
    for service in lstServices:
        strServices += service + " + "

    # Removes last | and returns the final string
    return strServices[0:-3]


def stringToServices(strServices):
    """Converts a string of services into an array. Used to deserialize a string for the database."""
    return strServices.split(" + ")


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
        queryInsertHistory = "insert into history (services, date, time, price, animalId) VALUES (?, ?, ?, ?, ?)"

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
        print(type(Error))
        print(Error.args)
        print(Error)

        mainDBConn.rollback()  # Removes any change made during execution
        historyDBConn.rollback()  # Removes any change made during execution

    finally:

        mainDBConn.close()  # Closes connection with our database
        historyDBConn.close()  # Closes connection with our database
