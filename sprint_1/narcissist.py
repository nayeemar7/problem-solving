def narcissistic(num):
    length = len(str(num))
    ans = 0
    for i in str(num):
        ans = ans + int(i)**length
    if ans == num:
        return  "Narcissist number"
    else:
        return "Not a Narcissist num" 
    
n = int(input("Enter the number: "))
print(narcissistic(n))



