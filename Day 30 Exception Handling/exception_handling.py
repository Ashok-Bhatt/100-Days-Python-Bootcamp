numbers = [1,1,1,2,4,2,3]

try:
    x = numbers[2]
except IndexError:      # Except should be written with name of exception
    print(f"Length of list: {len(numbers)}")
else:   # Excuted if no exception occured
    print(x)
finally:
    print("I will execute for sure")