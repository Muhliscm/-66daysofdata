from datetime  import datetime
import time
#timestamp = 1527051855673000000
#dt = time.strftime("%Y-%m-%d %H:%M:%S.%f",time.localtime(int(dt_str)))
#print(dt)

dt_str = "2013-03-07 05:29:47.890"
datetime_ob = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")
#timestamp = datetime_ob.timestamp()
timestamp = 1527051855.673000000
print(timestamp)
print(datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f"))
#print(dt_str.strftime('%B %d %Y'))

#dt = datetime.strptime(dt_str, format)
#print(datetime.utcfromtimestamp(dt_str).strftime("%Y-%m-%d %H:%M:%S.%f"))