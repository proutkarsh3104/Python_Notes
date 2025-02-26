# *args=allows you to pass multiple non-key arguments
#**kwargs=allows you to pass multiple keyword-arguments
#         *unpacking operator
#         1.positional 2.default 3.keyword 4.arbitrary


#args give tuple and kwargs give dictionary
def add(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(add(1,2,3,4,5,6))


def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("utkarsh","tiwari")



def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="betta",
              city="noida",
              state="up",
               zip="124")

def shipping_label(*args,**kwargs):
   for arg in args:
       print(arg,end=" ")
   print()
   for value in kwargs.values():
       print(value,end=" ")
#args are always put before kwargs
shipping_label("dr.","utkarsh","tiwari",
                street = "betta",
                city = "noida",
                state = "up",
                zip = "124")
