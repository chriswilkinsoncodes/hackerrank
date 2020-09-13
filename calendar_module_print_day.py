#!/usr/bin/env python3

# input date as MM DD YYYY

import calendar

month, day, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
