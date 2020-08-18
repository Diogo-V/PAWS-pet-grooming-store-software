from sqlite3 import *
from datetime import date


def dateToString(myDate):
    """Converts a date to a string. Used to serialize dates for the database."""
    return myDate.strftime('%d/%m/%Y')


def timeToString(myDate):
    """Converts a time to a string. Used to serialize dates for the database."""
    return myDate.strftime('%S-%M-%H')


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

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that moves past appointments into history table
        queryMoveAppointments = f"""insert into 
                                        history (services, date, time, price, animalId) 
                                    select * from 
                                        appointments 
                                    where 
                                        date < '{dateToString(date.today())}'"""

        # Executes motion
        cursor.execute(queryMoveAppointments)

        # SQL syntax that deletes past appointments from the appointments table
        queryDeleteAppointments = f"delete from appointments where date < '{dateToString(date.today())}'"

        # Executes deletion
        cursor.execute(queryDeleteAppointments)

        # Writes changes in the database
        connection.commit()

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

        connection.rollback()  # Removes any change made during execution

    finally:

        connection.close()  # Closes connection with our database
