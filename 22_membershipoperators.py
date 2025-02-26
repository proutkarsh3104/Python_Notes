#membership operators= used to test wheather a value or a variable found in a sequence
#                      (string,list,tuple,set,or dictionary)
#                      1.in
#                      2.not in

word="apple"

letter=input("guess a letter in a secret word:")

if letter in word:
    print(f"there is a {letter}")
else:
    print(f"{letter} was not found")


students={"andy","mandy","sandy"}
student=input("enter the name of a student:")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")



grades={"andy":"A",
        "mandy":"B",
        "sandy":"C"
        }

student=input("enter a name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email="prout@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")