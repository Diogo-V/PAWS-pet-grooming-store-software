from clients import *
from animals import *
from services import *
from datetime import date

# Sqlite-implementation-well

Base.metadata.create_all(engine)  # Generate database schema

session = Session()  # Opens a session so that we can change things on our database

service1 = Service(description="Cortar o pelo", price=20)
service2 = Service(description="Banho", price=100.2)

animal1 = Animal(name="Rocky", typeOfAnimal="Dog", weight=24.5, birthDate=date(2000, 12, 17))
animal2 = Animal(name="Nossa", typeOfAnimal="Dog", weight=90.2)
animal3 = Animal(name="Blacky", typeOfAnimal="Cat", weight=20.1, observations="Very strong")

appointment1 = Appointment([service1, service2], dateOfAppointment=date(2020, 3, 3), animal=animal1)
appointment2 = Appointment([service1], date(2019, 4, 5), animal2)

client1 = Client(first="Diogo", last="Venancio", nif=245002134)
client2 = Client(first="Martim", last="Venancio", phone=939611491)


# session.add_all([service1, service2])
# session.add(animal1)
# session.add_all([animal1, animal2, animal3])
# session.add(appointment2)

print('All services:')
for service in session.query(Service).all():
    print(service)
print('\n')

print("All appointments:")
for appointment in session.query(Appointment).all():
    print(appointment)
print("\n")

print("All clients:")
for client in session.query(Client).all():
    print(client)
print("\n")

print("All animals:")
for animal in session.query(Animal).all():
    print(animal)
print("\n")

# Commit changes
session.flush()
session.commit()
session.close()
