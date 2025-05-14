
def about_function(func):
    def wrapper(*args):
        ans = "Name of function: " + func.__name__ + "\n" + "Function arguments: "
        if len(args)==0:
            ans += "0"
        else:
            for arg in args:
                ans += str(arg) + "\t"
        ans += "\nFunction output: " + str(func(*args)) + "\n"
        return ans
    return wrapper

@about_function
def addNumbers(n1, n2):
    return n1 + n2

@about_function
def printHelloWorld():
    return "Hello World"

print(addNumbers(6,7))
print(printHelloWorld())