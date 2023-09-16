# 1) Define a Circle class allowing to create a circle C (O, r) with center O(a,
# b) and radius r using the constructor:
# def __init__(self,a,b,r):
# self.a = a
# self.b = b
# self.r = r
# a. Define a Area() method of the class which calculates the area of ​​the circle
# b. Define a Perimeter() method of the class which allows you to calculate the
# perimeter of the circle.
# c. Define a to_check() method of the class which allows to test whether a point
# A(x, y) belongs to the circle C(O, r) or not.

# Solution:

import math

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def to_check(self, x, y):
        self.d = math.sqrt((x - self.a)**2 + (y - self.b)**2)

        if self.d < self.r:
            print("The point", x, y, "belongs inside the circle")
        elif self.d > self.r:
            print("The point", x, y, "belongs outside the circle")
        else:
            print("The points are on the circle", x, y)

c1 = Circle(0, 1, 2)
print(c1.area())
print(c1.perimeter())
c1.to_check(1, 1)
