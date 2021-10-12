class vehicle():
    current_year = 2021
    base_price = 1000
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __private_method_parent(self):
        print("This is a private method!")

    def get_value(self):
        age = vehicle.current_year - self.model
        return vehicle.base_price*(1/age)

# child class
class Car(vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        super(Car, self).__init__(make,model,fuel)
        #protected members
        self._air_conditioning = air_conditioning
        self._sunroof = sunroof

    #protected method
   def _get_value(self):
       vehicle.base_price = 5000
       age = vehicle.current_year - self.model
       print("the child is over riding parent class! this is polymorphism")
       return vehicle.base_price*(1/age)

myobj = Car("tesla",2019, "electric", True, True)


