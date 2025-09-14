def gcd_euclidean(num1,num2):
    remainder = 1
    while remainder != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter second number: "))
print(gcd_euclidean(num1,num2))

