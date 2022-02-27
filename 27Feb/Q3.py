class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

a = Square(10)
print(a.area())
print(Square().area())
