#compound interest
principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("enter the  principle amount:"))
    if principle<=0:
        print("principle cant be less then or equal to zero")

while rate<=0:
    rate=float(input("enter the  rate amount:"))
    if rate<=0:
        print(" intrest rate cant be less then or equal to zero")

while time<=0:
    time=int(input("enter the  time in years:"))
    if time<=0:
        print(" time  cant be less then or equal to zero")

total= principle* pow((1+rate/100), time)

print(f"Balance after {time} year/s: ${total:.2f}")


