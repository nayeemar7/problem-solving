def fibonacci_fast(n):
    a,b = 0,1
    binary_n = bin(n)[2:]
    for bit in binary_n:
        c = a*(2*b-a)
        d = a**2 + b**2
        if bit == "1":
            a = d
            b = c+d
        else:
            a = c
            b = d
    return a

n = int(input("Enter the fibonacci term you want: "))
print(fibonacci_fast(n))

    