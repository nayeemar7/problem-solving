def array_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

length = int(input("Enter number of elements: "))
nums = []
for i in range(length):
    n = int(input("Enter the number: "))
    nums.append(n)

func = array_average(nums)
print("Average is:", func)

    
