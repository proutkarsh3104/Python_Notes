#function=A block of resuable code
#     place()after the function name to invoke it


def happy_birthday(name, age):
    print(f"happy birthday to {name}")
    print(f"you are {age}!")
    print()

happy_birthday("bro",20)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"your bll of ${amount:.2f} is due : {due_date}")

display_invoice("pro",32.45,"01/02")

