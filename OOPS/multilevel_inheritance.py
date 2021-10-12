"""This is an example of multilevel inheritance"""


class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel


class Car(Vehicle):
    def __init__(self, make, model, fuel, ac, sunroof):
        super(Car, self).__init__(make, model, fuel)
        self.ac = ac
        self.sunroof = sunroof


class ElectricVehicle(Car):
    def __init__(self, make, model, fuel, ac, sunroof, distance):
        super(ElectricVehicle).__init__(make, model, fuel, ac, sunroof)
        self._distance = distance
