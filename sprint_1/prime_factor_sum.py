import math
def prime_factor_sum(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        l = []
        for i in range(2,num+1):
            is_prime = True
            for j in range(2,int(math.sqrt(i)+1)):
                if i % j == 0:
                    is_prime =  False
                    break
            if is_prime:
                l.append(i)
    L = []
    for i in l:
        if num % i == 0:
            L.append(i)
    return sum(L)


num = int(input("Enter the number: "))
print(prime_factor_sum(num))