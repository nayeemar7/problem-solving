def second_max_num(l):
    l = list(set(l))
    l.sort()
    return l[-2]

length = int(input("Enter number of elements in the array: "))
l = []
for i in range(length):
    val = int(input("Enter the element in the array: "))
    l.append(val)
print(second_max_num(l))