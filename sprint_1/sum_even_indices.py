def sum_at_even_indices(arr):
    sum = 0
    for i in range(0,len(arr),2):
        sum += arr[i]
    return sum

n = int(input("Enter number of elements in the list: "))
arr = []
for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)
print(sum_at_even_indices(arr))