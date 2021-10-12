from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def get_value(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, fare):
        self.make = make
        self.model = model
        self.fare = fare

    def get_value(self):
        return 1000*self.fare

myobj = Car("Tesla", 2019, 40)


"""
INTERFACE is the Vehicle class
IMPLEMENTATION is the Car class

basically that is the blueprint to which other developers have to follow and write further code.

"""

"""######### ANOTHER EXAMPLE ################"""

class TextReaderAbstract(ABC):

    def __init__(self,path, filename):
        self.path = path
        self.filename = filename

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass

class TextReader(TextReaderAbstract):

    def get_path(self):
        return self.path

    def get_filename(self):
        return self.filename

myobj = TextReader("path/of/file", "filename")


"""   DJ KHALED ANOTHER ONE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

class Bank(ABC):

    @abstractmethod
    def get_interest_rate(self):
        pass
class HdfcBank(Bank):
    def get_interest_rate(self):
        return 8.9

myobj = HdfcBank()
myobj.get_interest_rate()
