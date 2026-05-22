day = int(input())
month = int(input())
year = int(input())

def leap(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

valid = True

# Year validation
if year <= 0:
    valid = False

# Month validation
if month < 1 or month > 12:
    valid = False

# Days in month
if valid:

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31

    elif month in [4, 6, 9, 11]:
        max_day = 30

    elif month == 2:
        if leap(year):
            max_day = 29
        else:
            max_day = 28

    if day < 1 or day > max_day:
        valid = False

if not valid:
    print("Invalid Date")

else:
    day += 1

    if day > max_day:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    print(day, month, year)
