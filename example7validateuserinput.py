#validate user input
username=input("enter a username")
if len(username)>12:
    print("your username cant be more then 12 charachter")
elif not username.find(" ")==-1:
    print("your username cant contain spaces")
elif not username.isalpha():
    print("your username cant contain number")
else:
    print(f"welcome{username}")