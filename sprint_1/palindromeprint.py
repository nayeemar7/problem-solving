def palindromeprint(string):
    rev = string[::-1]
    print("Encoded message is :", string)
    print("Decoded message is", rev)
    if string == rev:
        print("Palindrome!")
    else:
        print("Not a palindrome")
str = input("Enter a string: ")
palindromeprint(str)
