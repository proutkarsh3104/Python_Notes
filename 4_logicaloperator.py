#logial operators=evalutate multiple conditions(or,and,not)
#or=at least one conditon is must be true
#and= both conditon must be true
#not=inverts the conditon (not false,not true)

temp= 26
is_raining=False

if temp>35 or temp<0 or is_raining:
    print("the outdoor event is canceeled")
else:
    print("the outdoor event is still scheduled")


tempe=20
is_sunny=False
if tempe>=28 and is_sunny:
    print("its hot outside")
    print("it is sunny")
elif tempe<=0 and is_sunny:
    print("its cold outside")
    print("it is sunny")
elif tempe<28 and temp>0 and is_sunny:
    print("its warm outside")
    print("it is sunny")
elif tempe>=28 and not is_sunny:
    print("its hot outside")
    print("it is cloudy")
elif tempe<=0 and not is_sunny:
    print("its cold outside")
    print("it is cloudy")
elif tempe<28 and temp>0 and not is_sunny:
    print("its warm outside")
    print("it is cloudy")

