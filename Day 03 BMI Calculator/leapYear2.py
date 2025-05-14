year = int(input("Enter the year: "))

if ((year%100==0 and year%400!=0) or year%4!=0):
    print("Not a leap year")
else:
    print("Leap Year")