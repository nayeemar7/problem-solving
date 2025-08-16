def median(l):
    l.sort()
    length = len(l)
    if length % 2 != 0:
        med = (length+1)/2 - 1
        removed = l.pop(int(med))
        return removed
    else:
        val1 = l[int(length/2)-1]
        val2 = l[int(length/2)+1-1]
        return int((val1 + val2)/2)

l = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    n = int(input("Enter the element: "))
    l.append(n)
print(median(l))
    