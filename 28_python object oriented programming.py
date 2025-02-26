#Object=A "bundle" of related attributes(variables) and methods (functions)
#       Ex. phone,cup,book
#       You need a "class" to create many objects

#class=(blueprint) used to design the structure and layout of an object
#you can also import class by creating it in a different python file
class Car:
    def __init__(self, model, year,color, for_sale):   #we need this method to create object its called construtor
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the  {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1= Car("Mustang",2024,"red",False)
# . is used as an attribute access operator
car2= Car("Corvette",2025,"blue",True)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.stop()
car1.describe()
car2.describe()

