#!python3

from datetime import datetime
from datetime import timedelta
import calendar

t = timedelta(days=4, hours=10)

t.days
#4

t.seconds
#36000

t.hours
#Traceback (most recent call last):
    #File "<pyshell#119>", line 1, in <module> t.hours
#AttributeError: 'datetime.timedelta' object has no attribute 'hours'

t.seconds / 60 / 60
#10.0

t.seconds / 3600
#10.0


#########

eta = timedelta(hours=6)

today = datetime.today()

today
#datetime.datetime(2018, 2, 19, 14, 55, 19, 197404

today + eta
#datetime.datetime(2018, 2, 19, 20, 55, 19, 197404)

str(today + eta)
#'2018-02-19 20:55:19.197404'

# leap year
day = datetime(2016, 2, 28, 23, 0)
str(day)
str(day + timedelta(0, hours=2))

# daylight savings
day = datetime(2019, 3, 10, 1, 0)
str(day)
str(day + timedelta(0, hours=2))

# get name of day
day.weekday()
day.strftime('%A')
calendar.day_name[day.weekday()]