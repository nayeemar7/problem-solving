def string_length(str):
    char = 0
    for i in str:
        char += 1
    return char

str = input("Enter the string: ")
print("Number of characters: ",string_length(str))
