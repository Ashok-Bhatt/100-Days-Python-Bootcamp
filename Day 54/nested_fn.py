
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculate(calc_function, num1, num2):
    return calc_function(num1, num2)

print(calculate(add, 5, 7))


""" 
# nested function
def outer():
    print("Outer")

    def inner():
        print("Inner")
    
    inner()

outer()
 """


def outer():
    print("Outer")

    def inner():
        print("Inner")
    
    return inner

print("\nNew Output: ")
x = outer()
x()