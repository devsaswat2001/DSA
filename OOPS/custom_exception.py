class NegativeCarValue(Exception):
    def __init__(self, value, message="Car value can not be negative"):
        self.value = value
        self.message = message

    def __str__(self):
        return f'{self.message} --> {self.value}'


a = -1
if a < 0:
    raise NegativeCarValue(a)


class Vehicle:
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
        self.current_year = 2021

    def get_value(self):
        age = self.current_year - self.model
        if age < 0:
            raise NegativeCarValue(age)
        else:
            return 1000 * (1 / age)

obj = Vehicle("tesla", 2023, "electric")

"""
as the value of model is greater than the current year so the age would be in negative 
hence this will raise our own custom exception error

"""