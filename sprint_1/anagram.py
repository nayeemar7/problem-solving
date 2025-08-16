def anagram(string1,string2):
    list1 = []
    list2 = []
    for i in string1:
        list1.append(i)
    for j in string2:
        list2.append(j)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "Anagrams!"
    else: 
        return "Not anagrams!"
    
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
print(anagram(str1,str2))