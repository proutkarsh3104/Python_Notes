#list comprehesnion=  A conise way to create lists in python
#                     compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# doubles=[]
# for x in range(1,11): # in range funtcion the seocnd number is exculsive
#     doubles.append(x*2)
#
# print(doubles)

doubles=[x*2 for x in range(1,11)]
triples=[y*3 for y in range(1,11)]
squares=[z*z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)


fruits=["apple","orange", "banana"]
fruits=[fruit.upper() for fruit in fruits]
fruit_chars=[fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

numbers=[1,-2,-3,-4,5,-6]
positive_nums=[num for num in numbers if num >=0]
negetive_nums=[num for num in numbers if num <=0]
even_nums=[num for num in numbers if num%2==0]
odd_nums=[num for num in numbers if num%2==1]


print(positive_nums)
print(negetive_nums)
print(even_nums)
print(odd_nums)

grades=[85,42,79,90,56,6,30]
passing_grades=[grade for grade in grades if grade>=60]
print(passing_grades)