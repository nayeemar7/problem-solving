def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b 
        a = b 
        b = c
    return b

num = int(input("Enter the term you want to find: "))
print(fibonacci(num))