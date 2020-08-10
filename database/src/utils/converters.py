from datetime import datetime


def datetimeToString(myDate):
    """Converts a datetime to a string. Used to serialize dates for the database."""
    return myDate.strftime("%m/%d/%Y&%H-%M-%S")


def servicesToString(lstServices):
    """Converts a list of services to a string. Used to serialize a list for the database."""
    return lstServices.join("|")


def stringToServices(strServices):
    """Converts a string of services into an array. Used to deserialize a string for the database."""
    return strServices.split("|")
