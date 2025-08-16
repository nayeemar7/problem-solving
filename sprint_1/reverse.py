def reverse_function(string):
    reversedstr = ""
    for i in range(len(string)-1,-1,-1):
        reversedstr = reversedstr + string[i]
    return reversedstr

str = input("Enter a string: ")
print(reverse_function(str))

