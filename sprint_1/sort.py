def sort(list):
    list.sort()
    return list

l = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input("Enter a element: "))
    l.append(val)
print(sort(l))

        
        
        