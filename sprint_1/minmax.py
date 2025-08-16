def minmax(numbers):
    print("Maximum element is", max(numbers))
    print("Minimum element is", min(numbers))

n = int(input("Enter number of elements in list: "))
l = []
for i in range(n):
    val = int(input("Enter a value: "))
    l.append(val)
minmax(l)
