def sumoflist(list):
    length = len(list)
    sum = 0
    for i in range(length):          #You can also use Python’s built-in function sum(l)
        sum = sum + list[i]
    return sum

l = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    val = int(input("Enter an element: "))
    l.append(val)
print("Sum of elements in a list is", sumoflist(l))

        