height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

bmi = weight/height**2
print("BMI: ", bmi)

if bmi<18.5:
    print("You are underweight. ")
elif (bmi>=18.5 and bmi<25):
    print("You are normal weight. ")
elif (bmi>=18.5 and bmi<25):
    print("You are overweight. ")
elif (bmi>=18.5 and bmi<25):
    print("You are obese. ")
else:
    print("You are clinically obese. ")