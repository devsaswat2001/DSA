class Vehicle():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_value(self):
        try:
            age = 2021 - self.model
            return 1000 * (1 / age)
        except TypeError:
            try:
                age = 2021 - int(self.model)
                return 1000 * (1 / age)
            except ZeroDivisionError:
                age = 2021 - int(self.model)
                return 1000 * (1)
            except: #if 2019 is input as a string #new,#old
                return "You have entered model year in string , it requries int"

obj = Vehicle("tesla","2019","electric")

"""
here the model is in str so we handle multiple errors

"""