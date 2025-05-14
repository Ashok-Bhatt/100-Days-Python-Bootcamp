import time

def delayed_decorator(func):
    def wrapper_function():
        time.sleep(3)
        func()
    return wrapper_function

print("Program execution started")

@delayed_decorator
def say_hello():
    print("hello")

@delayed_decorator
def greeting():
    print("greeting")

def say_bye():
    print("Bye!")

say_hello()
greeting()
say_bye()