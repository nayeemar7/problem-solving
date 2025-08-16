def digits_in_num(num):
    string = str(num)
    length = 0
    for i in string:
        length += 1
    return length

n = int(input("Enter the number: "))
print(digits_in_num(n))

