def palindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

str = input("Enter the string: ")
if palindrome(str):
    print("It is a palindrome!")
else:
    print("Not a palindrome")