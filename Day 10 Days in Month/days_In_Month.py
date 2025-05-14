def isLeapYear(year):
    """
    This function returns 1 if the year is leap year else 0
    """
    if (year%400==0 or (year%4==0 and year%100!=0)):
        return 1
    return 0

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(f"No of days in Month {month} of {year}: {days_in_month[month-1]+isLeapYear(year)}")