# Meetpy

'''

Main topics:
    - Python Data Model
        - naming: _var vs __var vs __var__
    - class vs instance variables
    - *args and * operator:
        - initialize Point from Tuple
    - kwargs
        - add properties to
    - list comprehensions

'''

class Point:

    def __str__(self) -> str:
        return "(%.2f, %.2f)" % (self.x, self.y)

    def __repr__(self) -> str:
        return "Geometry.Point(%.2f, %.2f)" % (self.x, self.y)

    def __eq__(self, pnt):
        return self.x == pnt.x and self.y == pnt.y

    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.__dict__.update(kwargs)


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.__calculate_slope()

    def __calculate_slope(self):
        self.m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        print("The slope is %.1f" % self.m)


class RedLine(Line):

    def __init__(self, p1, p2):
        self.colour = 'Red'
        super().__init__(p1, p2)

    def __calculate_slope(self):
        self.m = 0
        print("haha... the slope is now %.1f!" % self.m)

