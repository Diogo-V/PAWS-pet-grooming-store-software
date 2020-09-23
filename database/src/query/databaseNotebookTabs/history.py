import datetime
from sqlite3 import *

from database.src.utils.converters import dateToString


def transformsIntegerAppointmentDateToString(app, idxOfDate):
    """
    Description:
    > Changes date inside app from integer to a printable string.
    :param app: tuple with the information about an appointment inside our database -> tuple
    :param idxOfDate: tuple index where date is located -> integer
    :return: tuple with our formatted information -> tuple
    """
    app = list(app)
    app[idxOfDate] = dateToString(datetime.date.fromordinal(app[idxOfDate]))
    return tuple(app)


def getsPetHistory(animalID):
    """
    Description:
    > Gets all the past appointments of this pet.

    :param animalID: animal rowid inside the database -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/history.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    history.ROWID,
                    history.date,
                    history.time,
                    history.services,
                    history.observations
                from
                    history
                where
                    history.animalId = {animalID}
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Converts our date to a string
        if type(info) is list and info != []:
            info = list(map(lambda app: transformsIntegerAppointmentDateToString(app, 1), info))
        elif type(info) is tuple:
            info = transformsIntegerAppointmentDateToString(info, 1)

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsInfoForHistoryWindow(historyID):
    """
    Description:
    > Gets all the appointments inside our database.

    :param historyID: history rowid inside the database -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/history.sqlite")
    cursor = connection.cursor()

    query = f"""
                select
                    history.services,
                    history.date,
                    history.time,
                    history.price,
                    history.observations
                from
                    history
                where
                    history.ROWID = {historyID}
                """
    try:

        # SQL syntax that is going to be parsed inside the database console

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Converts our date to a string
        if type(info) is list and info != []:
            info = list(map(lambda app: transformsIntegerAppointmentDateToString(app, 1), info))
        elif type(info) is tuple:
            info = transformsIntegerAppointmentDateToString(info, 1)

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database
