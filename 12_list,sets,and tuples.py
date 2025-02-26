# collectionn=single"variable" userd to store multiple values
#list=[] ordered and changeable, duplicates ok
#set={} unordered and inmutable, but add/remove ok, no duplicates
#tuple=() ordered and unchaable, duplicates ok, faaster


fruits=["apple","orange", "banana", "coconut"]
print(dir(fruits))
print(help(fruits))
#print(fruits[1])
#fruits.append(add elemnt)
#fruits.remove(remove element)

for fruit in fruits:
    print(fruit)