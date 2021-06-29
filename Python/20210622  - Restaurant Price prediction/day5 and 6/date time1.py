# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:36:03 2021

@author: MUHLIS
"""

import datetime

d = datetime.date(2016, 7, 24)
print(d)

print(datetime.date.today())

tday = datetime.date.today()
print(tday.day)

print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days= 7)
print(tday + tdelta)

print(tday - tdelta)

# date 2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2022, 6, 5)
till_tday = bday - tday
print(till_tday.total_seconds())


t = datetime.time(9, 30, 45, 100000)
print(t.minute)


dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)

print(dt.year)
print(dt.timestamp())
print(dt.date())
print(dt.time())

tdelta = datetime.timedelta(hours = 7)
print(dt+ tdelta)
print()
dt_now  = datetime.datetime.now()
dt_today  = datetime.datetime.today()
dt_utcnow = datetime.datetime.utcnow()
print(dt_now)
print(dt_today)
print(dt_utcnow)
print()

