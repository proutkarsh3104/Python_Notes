#conditonal expression= a one-line shortut for the if_statement (terenary operaor)
# print or assign one of two values based ona conditioon
#X if condition else Y



num=5
a=6
b=7
user_role="admin"
print("positive"  if num >0  else "negetive")
result="even" if num%2==0 else"odd"
print(result)
max_num=a if a>b else b
min_num=a if a<b else b
print(max_num)
print(min_num)
access_level="full acess" if user_role == "admin" else "limited acess"
print(access_level)