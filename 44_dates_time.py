import datetime

date = datetime.date(2020, 1, 1)
today = datetime.date.today()

time =datetime.time(12,30,0)
now = datetime.datetime.now()

now = now.strftime("%Y-%m-%d %H:%M:%S")

print(time)
print(now)
print(date)
print(today)


target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The target datetime has passed")
else:
    print("The target datetime has not passed yet")
    