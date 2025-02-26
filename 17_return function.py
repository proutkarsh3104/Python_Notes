#return=statement used to edn a function
#        and send a  result back to the caller
# the data you sent to a function is called arguments
# def add(x,y):
#     z=x+y
#     return z
#
# def subtract(x,y):
#     z=x-y
#     return z
#
# def multiply(x,y):
#     z=x*y
#     return z
#
# def divide(x,y):
#     z=x/y
#     return z
# print(add)

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()

    return first+" "+last

full_name= create_name("utkarsh","tiwari")

print(full_name)