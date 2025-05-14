import math

def paint(h, l, c):
    return math.ceil(h*l/c)

height = int(input("Height of wall:"))
length = int(input("Length of wall:"))
coverage = int(input("Coverage of can:"))

can = paint(h=height,l=length,c=coverage)
print("No of cans required: ", can)