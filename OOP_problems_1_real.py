

# OOP stuff

#Problem 1

import math

class Apple():
    def __init__(self, color, weight, stem_length, circumference):
        self.color = color
        self.weight = weight
        self.stem_lenght = stem_length
        self.circumference = circumference

        

ap1 = Apple("red", 30, 90, 10)
print(ap1)


# Problem 2

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi


a_circle = Circle(4)
print(a_circle.calculate_area())

# Problem 3

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.height * self.base / 2

a_triangle = Triangle(20, 30)
print(a_triangle.calculate_area())

# Problem 4

class Hexagon():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

a_hex = Hexagon(60)
print(a_hex.calculate_perimeter())


