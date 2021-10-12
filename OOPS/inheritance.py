# parent class
class vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __private_method_parent(self):
        print("This is a private method!")


# child class
class Car(vehicle):
    def __init__(self, make, model, fuel, air_conditioning, sunroof):
        super(Car, self).__init__(make,model,fuel)

        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    def show_parent_attributes(self):
        print(vehicle.make, " ", vehicle.model, " ", vehicle.fuel)

    def show_private_method_of_parent(self):
        self._vehicle__private_method_parent()
