# Jingxiang - 0312132939

year = int(input("Year: "))
while year < 1583 or year > 10000:
    print("Out of allowed range 1583 to 9999")
    year = int(input("Year: "))

month = int(input("Month: "))
MONTH_GLOBAL = month
while month < 1 or month > 12:
    print("Out of allowed range 1 to 12")
    month = int(input("Month: "))

    # ?Zellers kongruensformel
    if int(month) == 1 or int(month) == 2:
        month += 12
        year -= 1

day = int(input("Day: "))
# !Månaden är 1, 3, 5, 7, 8, ,10 ,12 = dagnummer i intervallet 1-31
while month in (1, 3, 5, 7, 8, 10, 12) and day < 1 or day > 31:
    print("Out of allowed range 1 to 31")
    day = int(input("Day: "))

else:
    # !Det är feb, och skottår = dagnummer i intervallet 1-29
    if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0):
        while month == 2 and day < 1 or day > 29:
            print("Out of allowed range 1 to 29")
            day = int(input("Day: "))

    else:
        # !Det är feb, och ingen skottår = dagnummer i intervallet 1-28
        while month == 2 and day < 1 or day > 28:
            print("Out of allowed range 1 to 28")
            day = int(input("Day: "))

    while month in (4, 6, 9, 11) and day < 1 or day > 30:
        print("Out of allowed range 1 to 30")
        day = int(input("Day: "))

# !Zellers kongruensformel
weekday = (day + 13*(month+1)//5 + year + year//4
           - year//100 + year//400) % 7

if weekday == 0:
    print("It is a Saturday")
elif weekday == 1:
    print("It is a Sunday")
elif weekday == 2:
    print("It is a Monday")
elif weekday == 3:
    print("It is a Tuesday")
elif weekday == 4:
    print("It is a Wednsday")
elif weekday == 5:
    print("It is a Thursday")
elif weekday == 6:
    print("It is a Friday")


# year = int(input("Year: "))
# while year < 1583 or year > 9999:
#     print("Out of allowed range 1583 to 9999")
#     year = int(input("Year: "))

# month = int(input("Month: "))
# while month < 1 or month > 12:
#     print("Out of allowed range 1 to 12")
#     month = int(input("Month: "))

# day = int(input("Day: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     while month == 2 and day < 1 or day > 29:
#         print("Out of allowed range 1 to 29")
#         day = int(input("Day: "))

# while month in (1, 3, 5, 7, 8, 10, 12) and day < 1 or day > 31:
#     print("Out of allowed range 1 to 32")
#     day = int(input("Day: "))

# while month in (4, 6, 9, 11) and day < 1 or day > 30:
#     print("Out of allowed range 1 to 30")
#     day = int(input("Day: "))

# else:
#     while month == 2 and day < 1 or day > 28:
#         print("Out of allowed range 1 to 28")
#         day = int(input("Day: "))

# while month in (1, 3, 5, 7, 8, 10, 12) and day < 1 or day > 31:
#     print("Out of allowed range 1 to 31")
#     day = int(input("Day: "))
