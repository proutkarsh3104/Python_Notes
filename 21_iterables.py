#iterables=an object/collection that can return its elements one at a time
#             allowing it to be iterated over in a loop

numbers=[1,2,3,4,5]

# for number in numbers:
for number in reversed(numbers):
    print(number, end=" ")


#sets are not reversable
name="utkarsh"
for charachter in name:
    print(charachter, end=" ")

my_dictionary={"A":1, "B":2, "C":3}

for value in my_dictionary.values():
    print(value)

for key in my_dictionary:
    print(key)

for key,value in my_dictionary.items():
    print(f"{key}={value}")