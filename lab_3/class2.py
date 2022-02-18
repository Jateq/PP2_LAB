class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        print("Default area of a shape is 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def area(self):
        print(self.length**2)
        
sh = Shape(5)
sh.area()
sq = Square(5)
sq.area()