import sqlite3


# Create a table of customers holding their names and emails. Both of them are considered text data types
def creates_table():
    connection = sqlite3.connect("database.sqlite")  # Creates a connection between this python file and our database
    cursor = connection.cursor()  # Creates a cursor. It is used to do everything in our table
    cursor.execute("CREATE TABLE customers (first_name text, last_name text, email text)")
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
