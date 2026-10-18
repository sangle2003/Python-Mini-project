import math


class Shape:
    def display(self):
        print("This is a shape")


class Triangle(Shape):
    def tri(self):
        self.base = float(input("Enter base: "))
        self.height = float(input("Enter height: "))

        area = 0.5 * self.base * self.height

        print("Triangle area =", area)


class Circle(Shape):
    def cir(self):
        self.radius = float(input("Enter radius: "))

        area = math.pi * self.radius * self.radius

        print("Circle area =", area)


# Create Triangle object
t1 = Triangle()
t1.display()
t1.tri()


# Create Circle object
c1 = Circle()
c1.display()
c1.cir()