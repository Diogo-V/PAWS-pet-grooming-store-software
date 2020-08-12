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
