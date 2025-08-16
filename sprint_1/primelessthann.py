import math
def primelessthann(num):
    list = []
    for i in range(num):
        if i < 2:
            continue
        isPrime = True    
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            list.append(i)
    return list

n = int(input("Enter the end range: "))
func = primelessthann(n)
print(func)

        