import calendar

year = int(input("Enter year:"))
month = int(input("Enter month (1-12):"))

day_index = calendar.weekday(year, month, 1)

days = ["Monday","Tuesday","Wednesday","Thursday",
"Friday","Saturday","Sunday&"]

print(f"\nThe first day of {month}/{year} is {days[day_index]}")

print("\nHere is the calendar:")
print(calendar.month(year, month))
