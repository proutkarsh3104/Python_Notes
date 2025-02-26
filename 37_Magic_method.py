# Magic methods = Dunder methods (double underscore) __init__. __str__, __eq__
#                 They are automatically called by many of Python's built_in operations.
#                 They allow developers to define or ustomize the behavior of objects.

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.num_pages == other.num_pages
    
    def __it__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, item):
        return item in self.title   
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages   
        else:
            return f"Key {key} was not found"
        
book1= Book("Brave New World", "Aldous Huxley", 311)
book2= Book("Onepiece", "Echiro oda", 267)
book3= Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

print(book1)

print(book1 == book2)

print(book2<book3)
print(book1>book3)
print(book1+book2)

print("Brave" in book1) 

print(book1["title"])   
print(book1["author"])
print(book1["num_pages"])
print(book1["genre"])  