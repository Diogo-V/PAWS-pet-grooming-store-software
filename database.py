import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# -------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------- SQLITE FUNCTIONS ---------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# Create a table of customers holding their names and emails. Both of them are considered text data types
def createsAnimalsTable():
    """
    Creates a table of animals inside our database.

    Database inputs:
    > name: animal nickname -> string
    > owners: clients which hold the pet -> list of clients (owners)
    > typeOfAnimal: type of animal -> string
    > weight: animal's weight -> double
    > birthDate: animal's birth date -> datetime
    > history: record of all of the services (with dates) provided to the pet -> list of appointments
    > observations: Notes about the pet -> String
    > appointment: set of services appointed to the pet -> list of appointments
    """
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE animals (
        name text, 
        owners text,
        typeOfAnimal text,
        weight real,
        birthDate blob,
        history blob
        )""")
    connection.close()


# Show contents of the table
def showTable():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM customers")
    for item in cursor.fetchall():
        print(item)
    connection.close()


# Adds a new record to the table
def addRecord(first, last, email):
    connection = sqlite3.connect("database.sqlite")  # Creates a connection between this python file and our database
    cursor = connection.cursor()  # Creates a cursor. It is used to do everything in our table
    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    connection.commit()
    connection.close()


# Deletes a record from the database. ID has to be passed as a string when calling function
def deleteRecord(rowId):
    connection = sqlite3.connect("database.sqlite")  # Creates a connection between this python file and our database
    cursor = connection.cursor()  # Creates a cursor. It is used to do everything in our table
    cursor.execute("DELETE from customers WHERE rowid = (?)", rowId)
    connection.commit()
    connection.close()


# Adds a lot of records at the same time
def addManyRecords(recordsList):
    connection = sqlite3.connect("database.sqlite")  # Creates a connection between this python file and our database
    cursor = connection.cursor()  # Creates a cursor. It is used to do everything in our table
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", recordsList)
    connection.commit()
    connection.close()


# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------- SQL ALCHEMY ------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


engine = create_engine('sqlite:///database.db', echo=False)  # Creates an engine to interact with our sqlite database
Session = sessionmaker(bind=engine)  # Create a configured "Session" class
Base = declarative_base(bind=engine)  # Creates a base class. Will be inherited by the other classes

# Base.metadata.create_all(engine)  # Generate database schema

# session = Session()  # Opens a session so that we can change things on our database
