def prime_range_sieve(end):
    check_prime = [True] * (end+1)
    check_prime[0] = check_prime[1] = False
    for i in range(2,int((end**0.5)+1)):
        if check_prime[i]:
            for j in range(i*i,end+1,i):
                check_prime[j] = False
    primes = []
    for k in range(len(check_prime)):
        if check_prime[k]:
            primes.append(k)
    return primes

l = []
start = int(input("Enter start range: "))
end = int(input("Enter the end range: "))
sieve = prime_range_sieve(end)
for i in sieve:
    if i >= start:
        l.append(i)
print(l)




