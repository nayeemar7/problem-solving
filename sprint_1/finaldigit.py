def final_digit(num):
    sum = 0
    length = len(str(num))
    for i in str(num):
        sum += int(i)
    if len(str(sum)) == 1:
        return sum
    else: 
        return final_digit(sum)


n = int(input("Enter the number: "))
print(final_digit(n))

