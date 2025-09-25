import datetime

date = datetime.date(2025, 1, 2)
print(date)
today = datetime.date.today()
print(today)

time = datetime.time(11, 50, 50)
print(time)
now = datetime.datetime.now()
print(now)

timeNow = now.strftime("%H:%M:%S")
print(timeNow)

dayNow = now.strftime("%d-%m-%Y")
print(dayNow)

targetDate = datetime.datetime(2030, 1, 2, 12, 7, 30)
currentDate = datetime.datetime.now()

if(targetDate < currentDate):
    print("target date has passed")
else:
    print("target day has not been reached yet")