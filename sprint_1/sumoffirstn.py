def sum_of_first_n(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

n = int(input("Enter the number: "))
print("Sum of first",n,"natural numbers is: ",sum_of_first_n(n))