# Static Method = A method that belong to a class rather than any object from that class(instance)
#                  Usually used for general utility fumctions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility function that do not need acess to class data


class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Assistant Manager", "Supervisor", "Team Lead", "Developer", "Intern"]
        return position in valid_positions
    
employee1= Employee("John", "Manager")
employee2= Employee("Jane", "Cook") 
    
print(Employee.is_valid_position("Cookc"))
print(employee1.get_info())