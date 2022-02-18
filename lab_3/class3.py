class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Default area of a shape is 0")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print(self.length * self.width)

sh = Shape(5, 6)
sh.area()
sq = Rectangle(6, 6)
sq.area()