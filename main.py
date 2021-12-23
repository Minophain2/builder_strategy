from abc import ABC,abstractmethod
#билдер
class builder(ABC):

    @abstractmethod
    def setSeats(self,number:int):
        pass

    @abstractmethod
    def setEngine(self, st:str):
        pass

    @abstractmethod
    def setAirbags(self,number:int):
        pass

    @abstractmethod
    def setGPS(self, flag:bool):
        pass

    @abstractmethod
    def getResult(self):
        pass

    @abstractmethod
    def getAirbags(self):
        pass

    @abstractmethod
    def getEngine(self):
        pass

    @abstractmethod
    def getGPS(self):
        pass

    @abstractmethod
    def getSeats(self):
        pass

class Car_Builder(builder):

    def __init__(self):
        self.seats = 0
        self.engine = ''
        self.airbags = 0
        self.gps = False

    def setSeats(self,number):
        self.seats = number
        return self

    def setEngine(self, st:str):
        self.engine = st
        return self

    def setAirbags(self,number:int):
        self.airbags = number
        return self

    def setGPS(self, flag:bool):
        self.gps = flag
        return self

    def getResult(self):
        return self

    def getAirbags(self):
        return self.airbags

    def getEngine(self):
        return self.engine

    def getGPS(self):
        return self.gps

    def getSeats(self):
        return self.seats


class Director:
    def create_car(self,seats,engine,airbags,gps):
        self.car = Car_Builder().setGPS(gps).setSeats(seats).setAirbags(airbags).setEngine(engine).getResult()
        return self.car


class Car:
    def __init__(self,created_car:Car_Builder):
        self.new_car = created_car

class car_creator:

    def create_toyota_land_cruiser(self):
        director = Director()
        result = director.create_car(8,'V8 4.5',8,True)
        new_car = Car(result)
        return new_car

    def create_Peugeot_107(self):
        director = Director()
        result = director.create_car(2, 'V3 1.4', 2, False)
        new_car = Car(result)
        return new_car

    def create_custom_car(self,seats,engine,airbags,gps):
        director = Director()
        result = director.create_car(seats,engine,airbags,gps)
        new_car = Car(result)
        return new_car



dir = Director()
dir_car = dir.create_car(4,'z-turbo',6,True)
print(dir_car.getSeats())

creator = car_creator()
car = creator.create_toyota_land_cruiser()
print(car.new_car.getSeats())