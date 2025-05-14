height = 2
weight = 40

if height > 3:
    raise ValueError ("Human Height cannot exceed 3 m.")

bmi = weight/(height*height)
print(f"BMI: {bmi}")