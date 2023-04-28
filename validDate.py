import leapYear as test
import datetime

def isValidDate(year, month, day):

    if month in [1, 3, 5, 7, 8, 10, 12]:
        # January, March, May, July, August, October, and December have 31 days
        return (1 <= day <= 31)
    
    elif month in [4, 6, 9, 11]:
        # September, April, June, and November have 30 days
        return (1 <= day <= 30)

    elif month == 2:
        # February has 28 days normally and 29 days when leapYear is True
        return (1 <= day <= 29) if test.isLeapYear(year) == True else (1 <= day <= 28)
    
    return False

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay