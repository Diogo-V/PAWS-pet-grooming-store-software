animal1 = ('Nossa', typeOfAnimal[0], 20.112, '', datetimeToString(datetime(2000, 8, 5, 14, 5, 0)), 'amigável')
animal2 = ('Boris Alberto', typeOfAnimal[0], 40.12, typeOfHair[1], datetimeToString(datetime(2010, 7, 21)), 'baboso')
animal3 = ('Pérola', typeOfAnimal[1], 15, typeOfHair[0], None, 'arranha muito')

client1 = ('Nuno Venancio', 'nuno@gmail.com', 121211221342, 73823228932, None)
client2 = ('Isabel', 'isabel@gmail.com', None, None, 'quinta')

appointment1 = (servicesToString(services[0:-1]), datetimeToString(datetime(2003, 4, 1)), 1)
appointment2 = (servicesToString(services[0:-2]), datetimeToString(datetime(2002, 4, 1)), 1)
appointment3 = (servicesToString(services[0:-3]), datetimeToString(datetime(2001, 4, 1)), 1)
appointment4 = (servicesToString(services[0:-1]), datetimeToString(datetime(2001, 5, 8)), 2)

initAllTables()

insertRecordAnimal(animal1)
insertRecordAnimal(animal2)
insertRecordAnimal(animal3)

insertRecordClient(client1)
insertRecordClient(client2)

insertRecordAppointment(appointment1)
insertRecordAppointment(appointment2)
insertRecordAppointment(appointment3)
insertRecordAppointment(appointment4)
