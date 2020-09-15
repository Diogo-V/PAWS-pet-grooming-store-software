from datetime import date, time


def dateToString(myDate):
    """Converts a date to a string. Used to serialize dates for the database."""
    return myDate.strftime('%d/%m/%Y')


def stringToDate(myDate):
    """Converts a string date into a datetime.date object."""
    [day, month, year] = myDate.split("/")
    return date(int(year), int(month), int(day))


def timeToString(myTime):
    """Converts a time to a string. Used to serialize dates for the database."""
    return myTime.strftime('%H-%M-%S')


def stringToTime(myTime):
    """Converts a string time into a datetime.time object."""
    [hours, minutes, seconds] = myTime.split("-")
    return time(int(hours), int(minutes), int(seconds))


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
