from database.src.utils.converters import *


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
                    appointments.time,
                    clients.phone,
                    animals.observations
                from
                    animals
                inner join
                    appointments,
                    clients,
                    petsClientsLink
                where
                    appointments.date = '{dateToString(dateAppointment)}' and
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


def getsInfoForAppointmentsWindow(appointmentID):
    """
    Description:
    Gets a list of the information that is going to be displayed inside the appointments toplevel window.

    :param appointmentID: appointment row id -> integer
    """

    # Creates a connection to our database and a cursor to work with it
    connection = connect("database/database.sqlite")
    cursor = connection.cursor()

    try:

        # SQL syntax that is going to be parsed inside the database console
        query = f"""
                select
                    animals.rowid, animals.name, animals.typeOfAnimal, 
                    animals.weight, animals.hairType, animals.observations,
                    clients.name, clients.nif, clients.phone,
                    appointments.services, appointments.date, appointments.time, appointments.price
                from
                    appointments
                inner join
                    animals,
                    clients,
                    petsClientsLink
                where
                    appointments.ROWID = {appointmentID}
                    and appointments.animalId = petsClientsLink.petId
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
