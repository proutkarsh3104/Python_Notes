#concession stand program

menu={"pizza":3.00,
      "nachos":4.50,
      "popcorn":6.00}

cart=[]
total=0

print("--------------MENU--------------")
for key, value in menu.items():
    print(f"{key}:${value:.2f}")

print("-----------------------------")

while True:
    food=input("select an item (q to quit)").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----------YOUR ORDER---------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")

print()

print(f"Total is :${total:.2f}")
