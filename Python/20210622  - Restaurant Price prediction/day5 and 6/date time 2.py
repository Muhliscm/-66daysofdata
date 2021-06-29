# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:15:34 2021

@author: MUHLIS
"""

import pytz
import datetime

dt = datetime.datetime(2016,7, 27, 12, 30, 45, tzinfo = pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz= pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

print()

for tz in pytz.all_timezones:
    print(tz)
    

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))

print(dt_mtn)
print()
print(dt_east)

print(dt_mtn.isoformat())

print(dt_mtn.strftime('%B %d %Y'))

dt_str = "June 29 2021"
dt = datetime.datetime.strptime(dt_str, "%B %d %Y")
print(dt)