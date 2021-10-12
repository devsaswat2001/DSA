class Circle(object):
    def __init__(self,radius):
        self.__radius = radius

    def __str__(self):
        return "this is a circle class!"

c = Circle(3)
print(c)
