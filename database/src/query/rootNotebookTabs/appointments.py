import datetime
from sqlite3 import *

from database.src.utils.converters import *


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


def getsDayAppointments(dateAppointment):
    """
    Description:
    Gets a list of appointments for a specific day.

    :param dateAppointment: required date -> date
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    appointments.ROWID,
                    animals.name, 
                    clients.name,
                    appointments.services, 
                    appointments.time
                from
                    animals
                inner join
                    appointments,
                    clients,
                    petsClientsLink
                where
                    appointments.date = {dateAppointment.toordinal()} and
                    appointments.animalId = petsClientsLink.petId and
                    animals.ROWID = petsClientsLink.petId and
                    clients.ROWID = petsClientsLink.clientId
                """

        # Executes command and gets a list of appointments
        appointments = cursor.execute(query).fetchall()

        # Returns appointments found during query
        return appointments

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database


def getsInfoForAppointmentsWindow(appointmentID, clientName):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the appointments toplevel window.

    :param appointmentID: appointment row id -> integer
    :param clientName: owner's name -> string
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.rowid, animals.name, animals.type, animals.breed, animals.gender, animals.weight, 
                    animals.hairType, animals.hairColor, animals.age, animals.observations,
                    clients.rowid, clients.name, clients.email, clients.phone, clients.nif, clients.address,
                    appointments.services, appointments.date, appointments.time, 
                    appointments.price, appointments.observations
                from
                    appointments
                inner join
                    animals,
                    clients,
                    petsClientsLink
                where
                    appointments.ROWID = {appointmentID} 
                    and clients.name = '{clientName}'
                    and appointments.animalId = petsClientsLink.petId
                    and animals.ROWID = petsClientsLink.petId
                    and clients.ROWID = petsClientsLink.clientId
                """

        # Gets list containing the requested information
        info = cursor.execute(query).fetchall()

        # Converts our date to a string
        if type(info) is list and info != []:
            info = list(map(lambda app: transformsIntegerAppointmentDateToString(app, 17), info))
        elif type(info) is tuple:
            info = transformsIntegerAppointmentDateToString(info, 17)

        return info

    except Error:

        # Error information and details processing
        print(type(Error))
        print(Error.args)
        print(Error)

    finally:

        connection.close()  # Closes connection with our database
