import math
def prime_range_sum(start,end):
    l = []
    sum = 0
    for i in range(start,end+1):
        if i > 1:
            is_prime = True
            for j in range(2,int(math.sqrt(i))+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                l.append(i)
    for i in range(len(l)):
        sum += l[i]
    return sum

st = int(input("Enter start range: "))
end = int(input("Enter end range: "))
print(prime_range_sum(st,end))

