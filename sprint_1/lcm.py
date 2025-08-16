def lcm(a,b):
    maximum = max(a,b)
    while True:
        if maximum % a == 0 and maximum % b == 0:
            return maximum
        maximum += 1

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(lcm(x,y))