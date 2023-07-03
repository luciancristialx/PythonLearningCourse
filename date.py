# Datetime
import datetime

x = datetime.datetime.now()
print(x.day)
print(x.month)
print(x.year)

# Date objects

y = datetime.datetime(2025, 3, 28)
print(y)

# Strf time() - string formatting (https://stackabuse.com/how-to-format-dates-in-python/)

print(y.strftime("%A %a/ %B "))
