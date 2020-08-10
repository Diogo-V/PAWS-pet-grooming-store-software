from database.src.utils.querying import *

# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------- CONSTANTS ------------------------------------------------------ #
# -------------------------------------------------------------------------------------------------------------------- #


# Services provided by this store
services = ['Dar banho', 'Cortar as unhas', 'Cortar o pelo', 'Outro']

# Pets received by this store
typeOfAnimal = ['Cão', 'Gato', 'Coelho', 'Outro']

# Type of hair held by the animal
typeOfHair = ['Pelo longo', 'Pelo curto']

connection = connect("database/database.sqlite")
cursor = connection.cursor()

print(getClientFromPets(3))
