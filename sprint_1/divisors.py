def divisors(num):
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

n = int(input("Enter a number: "))
func = divisors(n)
print(func)

