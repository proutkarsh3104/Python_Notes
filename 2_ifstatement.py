# if= do some code only IF condition is True
#   Else do something else

age=int(input("enter your age:"))

if age>=100:
    print("you are too old to sign up")
elif age>=18:
    print("you are now signed up")
elif age<0:
    print("you havent been born yet")
else:
    print("you must be 18+ to sign up")



response= input("would you like food?(Y/N)")


if response =="Y":
    print("have some food")
else:
    print("no food for you")


name=input("enter your name")

if name=="":
    print("you did not type in your name")
else:
    print(f"hello{name}")