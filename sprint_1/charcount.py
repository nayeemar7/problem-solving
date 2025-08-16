def charcount(string):
    vowels = 0
    consonants = 0
    for i in string.lower():
        if i in "aeiou":
            vowels += 1
        elif i.isalpha():
            consonants += 1
    print("Vowels: ",vowels)
    print("Consonants: ",consonants)

str = input("Enter a string: ")
charcount(str)


