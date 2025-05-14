name1 = input("Enter first name:")
n1 = name1.lower();
name2 = input("Enter second name:")
n2 = name2.lower();

first = 0
second = 0

for i in "true":
    first = first + n1.count(i)
    first = first + n2.count(i)

for i in "love":
    second = second + n1.count(i)
    second = second + n2.count(i)

print(first, second)

percentage = (first%10)*10 + second%10
print("Love Percentage: ", percentage)