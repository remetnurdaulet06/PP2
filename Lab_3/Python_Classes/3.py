class Shape:
    def __init__(self, shapet):
        self.shapet = shapet
        self.area = 0
    def cur_area(self):
        if self.shapet == "square":
            return f"Area of Square = {self.area}"
        elif self.shapet == "rectangle":
            return f"Area of Rectangle = {self.area}"
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("rectangle")
        self.length = length
        self.width = width
        self.area += self.length * self.width
asd = Rectangle(5, 20)
print("Area of Rectangle l = 5, w = 20")
print(asd.cur_area())
print()