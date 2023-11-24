import abc


class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = (self.a * 2) + (self.b * 2)
        print("Consider me implemented", perim)
        return perim


class Sqaure(Rectangle):
    def __init__(self, a):
        self.a = a


rectangle = Rectangle(10, 20)
print(rectangle.calc_perimeter())

sqaure = Sqaure(10)
print(sqaure.calc_perimeter())
