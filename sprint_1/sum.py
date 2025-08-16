def sum_of_first_n(n):
    sum = 0 
    for i in range(1,n+1):
        sum = sum + i 
    return sum

def sum_using_formula(n):
    sum = (n*(n+1))/2
    return sum

num = int(input("Enter the number:"))
print(sum_of_first_n(num))
print(sum_using_formula(num))

    