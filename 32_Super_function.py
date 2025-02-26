# super()= Function used in a child class to call methods from a parent class (superclass).
#          Allows you to extend the fuctionality of the inherited methods

# If  a chld class share the same function as a parent then the child function is used unless we use the super function
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled=is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14*self.radius * self.radius}cm^2")
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
class Triangle(Shape):
    def __init__(self, color, filled, width,height):
        self.color = color
        self.filled = filled
        self.width = width
        self.height= height
        
circle= Circle(color="red", is_filled=True, radius=5)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

circle.describe()