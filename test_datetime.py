# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone,timedelta

def to_timestamp(dt_str, tz_str):
    x = re.match(r'^[0-9]{4}\-[0-9]|1[0-2]\-[0-9]|[1-2][0-9]|3[0-1]\s[0-9]|1[0-9]|2[0-3]\:0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]\:0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]$',dt_str)
    y = re.match(r'^UTC(.[0-9]{1,2})\:00$',tz_str)
    if x and y:
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#       print(y.group(1))
        tz = timezone(timedelta(hours=int(y.group(1))))
        d = dt.replace(tzinfo=tz)
        ts = d.timestamp()
        return (ts)
    else:
        print('date error')

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print(t2)
print('Pass')
