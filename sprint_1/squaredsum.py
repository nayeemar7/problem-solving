def squared_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)**2
    return sum
    
n = int(input("Enter a number: "))
print(squared_sum(n))



