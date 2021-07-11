
# Defining a class for rectangles
class Rectangle:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.__private_attr = None
    def describe(self):
        print(f"I am a Rectangle at ({self.x}, {self.y}) of length {self.length} and width {self.width}")

# Creating rectangle objects
my_first_rectange = Rectangle(100, 100, 50, 80)
other_rectangle = Rectangle(10, 20, 30, 40)

# Calling methods
my_first_rectange.describe()
other_rectangle.describe()

# Getting out data
print(my_first_rectange.x)
