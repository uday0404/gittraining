import time

localtime = time.localtime(time.time())
print("Local current time :", localtime)


import time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)


import calendar

cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)


import datetime

x = datetime.datetime.now()
print(x)

print(x.year)



Library/Module

