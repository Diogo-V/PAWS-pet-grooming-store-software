from database.functions.dbInit import *
from database.functions.database import *
from datetime import datetime


# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- CONSTANTS ------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


# Services provided by this store
services = [
    'Dar banho',
    'Cortar as unhas',
    'Cortar o pelo',
    'Outro'
]

# Pets received by this store
typeOfAnimal = [
    'Cão',
    'Gato',
    'Coelho'
    'Outro'
]

# Type of hair held by the animal
typeOfHair = [
    'Pelo longo',
    'Pelo curto'
]




# initAllTables()
# deleteAllTables()





animal1 = ('Nossa', typeOfAnimal[0], 20.112, '', datetimeToString(datetime(2000, 8, 5, 14, 5, 0)), 'amigável')
animal2 = ('Boris Alberto', typeOfAnimal[0], 40.12, typeOfHair[1], datetimeToString(datetime(2010, 7, 21)), 'baboso')
animal3 = ('Pérola', typeOfAnimal[1], 15, typeOfHair[0], None, 'arranha muito')

client1 = ('Nuno Venancio', 'nuno@gmail.com', 121211221342, 73823228932, None)
client2 = ('Isabel', 'isabel@gmail.com', None, None, 'quinta')

q1 = "insert into animals (name, typeOfAnimal, weight, hairType, birthDate, observations) values (?, ?, ?, ?, ?, ?);"
s1 = f"select * from animals where birthDate = {datetimeToString(datetime(2000, 8, 5, 14, 5, 0))}"
s2 = "select birthDate from animals where ROWID = 3"

# connection = connect("database/database.sqlite")
# cursor = connection.cursor()

# cursor.execute(q1, animal1)
# connection.commit()

# connection.close()

# insertRecordAnimal(animal1)
