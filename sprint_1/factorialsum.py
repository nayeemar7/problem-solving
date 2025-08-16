def factorialsum(num):
    fact = 1
    if num == 1 or num == 0:
        fact = 1
    else: 
        for i in range(1,num+1):
            fact = fact * i
    sum = 0
    for i in str(fact):
        sum = sum + int(i)
    return sum


n = int(input("Enter a number: "))
print(factorialsum(n))
