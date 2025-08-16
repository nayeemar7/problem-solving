def gcd(a,b):
    while b!= 0:
        remainder = a % b
        a = b
        b = remainder
    return a

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(gcd(num1,num2))

