# Polymorphism = Greek Word to have many form or faces
#                poly= many
#                morph= form

                # Two ways to achive polymorphism
                # 1. Inheritance=AN object could be treated of the same types as a parent class
                # 2.Duck typing = obhect must have necesssarry atributes/methods

from abc import ABC, abstractmethod                
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

class Square(Shape):    
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side*self.side

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        return 0.5*self.base*self.height
class Pizza(Circle):
    def __init__(self, topping, radius):
        super(). __init__(radius)
        self.topping=topping
        
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)]

for shape in shapes:
    print(shape.area())