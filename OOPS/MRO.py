class Car():
    def __init__(self,make,model,fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is ", self.model , " from car class"

class Electric():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_car_details(self):
        return "the make of the car is ", self.model , " from Electric car class"

class Taxi(Car, Electric): #Multiple inheritance
    def __init__(self,make ,model, fuel):
        super().__init__(make,model,fuel)

myobj = Taxi("Tesla",2019, "electric")


"""this will execute the first class first and then come down to the second class
    it can also be defined by the way we define in the Taxi class
    we can check the mro  Taxi.__mro__ or Taxi.mro()
"""