import calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022,7)
str1 = c.formatmonth(2022, 8)
str2 = c.formatmonth(2022, 9)
print(str)
print(str1)
print(str2)
