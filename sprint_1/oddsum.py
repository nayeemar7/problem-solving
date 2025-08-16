def oddsum(start,end):
    sum = 0
    for i in range(start,end+1):
        if i % 2 == 0:
            pass
        else:
            sum = sum + i
    return sum
x = int(input("Enter start range: "))
y = int(input("Enter end range: "))
print("Sum of odd numbers is: ",oddsum(x,y))

