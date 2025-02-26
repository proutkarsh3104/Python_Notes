#dictionary= a collection of {key:value} pairs
# ordered and changeable. no duplicates

capitals={"USA": "Washington.",
          "INDIA": "New Delhi"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA"))

for key, value in capitals.items():
    print(f"{key}:{value}")
