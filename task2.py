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
        """
        Calculates and returns perimeter of triangle
        :return: Perimeter of the triangle
        """
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        """
        Calculates and returns perimeter of rectangle
        :return: Perimeter of the rectangle
        """
        perim = 2 * (self.a + self.b)
        print("Consider me implemented", perim)
        return perim


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


rectangle = Rectangle(20, 10)
rectangle.calc_perimeter()

square = Square(20)
square.calc_perimeter()
