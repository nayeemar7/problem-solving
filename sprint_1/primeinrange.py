import math
def primeinrange(start,end):
    primelist = []
    for i in range(start,end):
        if i < 2:
            continue
        isPrime = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            primelist.append(i)    
    return primelist
x = int(input("Enter start range: "))
y = int(input("Enter end range: "))
print(primeinrange(x,y))


