#temprature conversion
unit=input("is this temprature in celsius or frahenheit(C/F):")
temp=float(input("enter the temprature:"))

if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"the temprature in frahenheit is: {temp}°F")
elif unit=="F":
    temp= round((temp-32)*5/9,1)
    print(f"the temprature in celcius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurementC")

