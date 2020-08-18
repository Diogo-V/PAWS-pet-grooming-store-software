from datetime import time

from main import *
from database.src.utils.converters import *
from database.src.utils.constants import *
from database.src.functions.insertion import *
from database.src.functions.initialization import *


animal1 = ('Nossa', typeOfAnimal[0], 20.112, '', dateToString(date(2000, 8, 5)),  'amigável')
animal2 = ('Boris Alberto', typeOfAnimal[0], 40.12, typeOfHair[1], dateToString(date(2010, 7, 21)), 'baboso')
animal3 = ('Pérola', typeOfAnimal[1], 15, typeOfHair[0], None, 'arranha muito')

client1 = ('Nuno Venancio', 'nuno@gmail.com', 121211221342, 73823228932, None)
client2 = ('Isabel', 'isabel@gmail.com', None, None, 'quinta')

appointment1 = (servicesToString(services[0:-1]), dateToString(date(2003, 4, 1)), timeToString(time(14, 0, 5)), 1)
appointment2 = (servicesToString(services[0:-2]), dateToString(date(2002, 4, 1)), timeToString(time(14, 0, 5)), 1)
appointment3 = (servicesToString(services[0:-3]), dateToString(date(2001, 4, 1)), timeToString(time(14, 0, 5)), 1)
appointment4 = (servicesToString(services[0:-1]), dateToString(date(2001, 5, 8)), timeToString(time(14, 0, 5)), 2)
appointment5 = (servicesToString(services[0:-2]), dateToString(date(2020, 8, 12)), timeToString(time(13, 0, 0)), 2)

link1 = (1, 1)
link2 = (3, 1)
link3 = (2, 2)

initDatabase()

insertRecordAnimal(animal1)
insertRecordAnimal(animal2)
insertRecordAnimal(animal3)

insertRecordClient(client1)
insertRecordClient(client2)

insertRecordPetClientLink(link1)
insertRecordPetClientLink(link2)
insertRecordPetClientLink(link3)

insertRecordAppointment(appointment1)
insertRecordAppointment(appointment2)
insertRecordAppointment(appointment3)
insertRecordAppointment(appointment4)
