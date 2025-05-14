import time

def time_telling_decorator(func):
    def wrapper():
        starting_time = time.time()
        func()
        ending_time = time.time()
        return f"Total time taken: {ending_time-starting_time}"
    return wrapper

@time_telling_decorator
def printNumbers():
    for i in range(1000):
        print(i+1, end =" ")
    print()

@time_telling_decorator
def addNumbers():
    print("2 + 3 = 5")

printNumbers()
addNumbers()