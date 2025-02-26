#format specifiers={value:flags} fromat a value based on what flags are inserted
price1=3.2232
price2=-3223.2332
price3=12.34

print(f"price1 is ${price1:10}")
print(f"price2 is ${price2:}")
print(f"price3 is ${price3}")