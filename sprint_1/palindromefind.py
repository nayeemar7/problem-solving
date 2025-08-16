def palindrome_find(string):
    length = len(string)
    check = ""
    list = []
    for i in string:
        check += i
        if check == check[::-1]:
            list.append(check)
    max = ""
    for j in list:
        if len(j) > len(j+1):
            max = j
    return max

str = input("Enter a string: ")
n = palindrome_find(str)
print(n)