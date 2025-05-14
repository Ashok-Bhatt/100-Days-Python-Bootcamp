bill = int(input("Enter the bill amount: "))
tip = int(input("Enter the percentage of tip: "))
person = int(input("Enter the number of peoples: "))

pay_per_person = (bill + bill*tip/100)/person
print(f"Each person will pay {round(pay_per_person,2)} rupees.")