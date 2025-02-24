import datetime

date=datetime.date(2025,5,10)

print(date)
today=datetime.date.today()
print(today)

now=datetime.datetime.now()
current_time=now.strftime("%H:%M:%S %m-%d-%y")
print(current_time)


target_datetime=datetime.datetime(2020,1,2,12,30,1)
current_time1=datetime.datetime.now()

if target_datetime < current_time1:
    print("Target is missed ")
else:
    print("Target is remaining ")



