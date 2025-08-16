def factorial_i(n):       #iterative
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact 

def factorial_r(n):       #recursive
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial_r(n-1)

num = int(input("Enter a number: "))
print(factorial_i(num))
print(factorial_r(num))




        